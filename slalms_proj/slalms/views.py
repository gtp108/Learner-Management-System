from django.shortcuts import render, redirect ,get_object_or_404
from django.contrib import messages
from .models import Teacher, Student,Course
def home(request):
    return render(request, 'home.html')

def student_login(request):
    if request.method == 'POST':
        reg_number = request.POST['registration_number']
        password = request.POST['password']
        try:
            student = Student.objects.get(registration_number=reg_number, password=password)
            courses = Course.objects.filter(student=student)
            return render(request, 'student_dashboard.html', {'student': student,'courses':courses})
        except Student.DoesNotExist:
            return render(request, 'student_login.html')
            messages.error(request, 'Login Failed. Try Again.')
    else:
        return render(request, 'student_login.html')

def teacher_login(request):
    if request.method == 'POST':
        employee_id = request.POST['employee_id']
        password = request.POST['password']
        try:
            teacher = Teacher.objects.get(employee_id=employee_id, password=password)
            courses = Course.objects.filter(teacher=teacher)
            return render(request, 'teacher_dashboard.html', {'teacher': teacher, 'courses': courses})
        except Teacher.DoesNotExist:
            return render(request, 'teacher_login.html')
            messages.error(request, 'Login Failed. Try Again.')
    return render(request, 'teacher_login.html')

def assign_marks(request):
    if request.method == 'POST':
        registration_number = request.POST.get('registration_number') 
        employee_id=request.POST.get('employee_id')
        marks = int(request.POST.get('marks'))
        # Retrieve student object
        student = get_object_or_404(Student, registration_number=registration_number)
        teacher= get_object_or_404(Teacher, employee_id=employee_id)
        # Retrieve course for the student
        courses, created = Course.objects.get_or_create(student=student,teacher=teacher)

        # Assign marks
        
        if marks >100 & marks<0:
            courses.save()
        else :
            courses.marks = marks
            courses.save()
        

        # Assign learner type based on marks
        learner_type = 'fast_learner' if courses.marks > 60 else 'slow_learner'
        courses.learner_type = learner_type
        courses.save()

        messages.success(request, f'Marks assigned successfully for {student.full_name}')

    # Retrieve all students with their courses and marks after updating
    courses = Course.objects.filter(teacher=teacher)
    # Render teacher_dashboard.html with updated data
    return render(request, 'teacher_dashboard.html', {'teacher': teacher, 'courses': courses})
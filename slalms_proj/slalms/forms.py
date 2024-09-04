from django import forms
from .models import Teacher, Student,Course
class TeacherForm(forms.ModelForm):
    full_name = forms.CharField(max_length=100)
    employee_id = forms.CharField(max_length=20)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)
    subject_taken = forms.CharField(max_length=100)

class StudentForm(forms.ModelForm):
    full_name = forms.CharField(max_length=100)
    registration_number = forms.CharField(max_length=20)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)
    semester = forms.IntegerField()

class CourseForm(forms.ModelForm):
    student = forms.ModelChoiceField(queryset = Student.objects.all())
    teacher = forms.ModelChoiceField(queryset = Teacher.objects.all())
    subject = forms.CharField(max_length=100)
    marks=forms.IntegerField()
    learner_type=forms.CharField(max_length=20)
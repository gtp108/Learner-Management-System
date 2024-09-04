from django.contrib import admin
from .models import Teacher, Student,Course
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'employee_id', 'subject_taken','password')

class StudentAdmin(admin.ModelAdmin):
     list_display = ('full_name', 'registration_number','password','semester')

class CourseAdmin(admin.ModelAdmin):
    list_display = ('student', 'teacher','marks','learner_type')

admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Course, CourseAdmin)
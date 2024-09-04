from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Teacher(models.Model):
    full_name = models.CharField(default=None, max_length=100, null=True)
    employee_id = models.CharField(default=None, max_length=20, primary_key=True)
    password = models.CharField(default=None, max_length=50, null=True)
    subject_taken = models.CharField(default=None, max_length=100, null=True)

class Student(models.Model):
    full_name = models.CharField(default=None, max_length=100, null=True)
    registration_number = models.CharField(default=None, max_length=20, primary_key=True)
    password = models.CharField(default=None, max_length=50, null=True)
    semester = models.IntegerField(default=None, null=True)

class Course(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    marks = models.IntegerField(null=True, default=None, validators=[MinValueValidator(0), MaxValueValidator(100)])
    learner_type = models.CharField(max_length=20, null=True, default=None)

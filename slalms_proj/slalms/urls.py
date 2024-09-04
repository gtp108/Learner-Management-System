from django.urls import path
from .views import home, student_login, teacher_login,assign_marks

urlpatterns = [
    path('', home, name='home'),
   path('student_login/', student_login, name='student_login'),
   path('teacher_login/', teacher_login, name='teacher_login'),
   path('assign_marks', assign_marks, name='assign_marks'),
]
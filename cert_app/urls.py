# cert_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('students_for_teacher/<int:teacher_id>/', views.students_for_teacher, name='students_for_teacher'),
    path('teachers_for_student/<int:student_id>/', views.teachers_for_student, name='teachers_for_student'),
    path('certificate_list/', views.certificate_list, name='certificate_list'),
    path('generate_certificate/', views.generate_certificate, name='generate_certificate'),
]

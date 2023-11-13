# admin.py
from django.contrib import admin
from .models import Student, Teacher, Certificate

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    filter_horizontal = ('teachers',)  # This will display teachers as checkboxes in Student admin

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    filter_horizontal = ('students',)  # This will display students as checkboxes in Teacher admin

admin.site.register(Certificate)
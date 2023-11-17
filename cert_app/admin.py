from django.contrib import admin
from .models import Student, Teacher, Certificate

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    filter_horizontal = ('teachers',)
    list_display = ('id', 'name', 'display_teachers')

    def display_teachers(self, obj):
        return ", ".join([teacher.name for teacher in obj.teachers.all()])
    
    display_teachers.short_description = 'Teachers'

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    filter_horizontal = ('students',)
    list_display = ('id', 'name', 'display_students')

    def display_students(self, obj):
        return ", ".join([student.name for student in obj.students.all()])
    
    display_students.short_description = 'Students'

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('id', 'teacher', 'student', 'text')

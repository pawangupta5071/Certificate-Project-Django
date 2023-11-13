from django.shortcuts import render, redirect
from .forms import CertificateForm
from .models import Teacher,Student,Certificate
# Create your views here.


def home(request):
    teachers = Teacher.objects.all()
    students = Student.objects.all()
    return render(request, 'home.html', {'teachers': teachers, 'students': students})

def students_for_teacher(request,teacher_id):
    teacher = Teacher.objects.get(pk=teacher_id)
    return render(request,"students_for_teacher.html",{"teacher":teacher})


def teachers_for_student(request,student_id):
    student = Student.objects.get(pk=student_id)
    return render(request,"teachers_for_student.html",{'student':student})

def certificate_list(request):
    certificates = Certificate.objects.all()
    return render(request, 'certificate_list.html', {'certificates': certificates})

def generate_certificate(request):
    if request.method == 'POST':
        form = CertificateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('certificate_list')
    else:
        form = CertificateForm()
    return render(request, 'generate_certificate.html', {'form': form})
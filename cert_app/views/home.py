def home(request):
    from cert_app.models import Teacher,Student
    from django.shortcuts import render

    teachers = Teacher.objects.all()
    students = Student.objects.all()
    return render(request, 'home.html', {'teachers': teachers, 'students': students})
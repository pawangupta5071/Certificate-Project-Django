def teachers_for_student(request,student_id):
    from django.shortcuts import render
    from cert_app.models import Student
    
    student = Student.objects.get(pk=student_id)
    return render(request,"teachers_for_student.html",{'student':student})

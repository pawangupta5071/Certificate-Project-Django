def students_for_teacher(request,teacher_id):
    from django.shortcuts import render
    from cert_app.models import Teacher

    teacher = Teacher.objects.get(pk=teacher_id)
    return render(request,"students_for_teacher.html",{"teacher":teacher})

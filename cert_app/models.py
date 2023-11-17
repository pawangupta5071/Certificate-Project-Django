from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    teachers = models.ManyToManyField("Teacher",blank=True)

    def __str__(self):
        return self.name
    
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    students = models.ManyToManyField(Student,blank=True)

    def __str__(self):
        return self.name
    
class Certificate(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f"Certificate for {self.student.name} from {self.teacher.name}"



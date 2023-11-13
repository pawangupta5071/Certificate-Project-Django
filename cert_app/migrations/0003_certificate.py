# Generated by Django 4.2.2 on 2023-11-12 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cert_app', '0002_remove_teacher_students_alter_student_teachers_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cert_app.student')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cert_app.teacher')),
            ],
        ),
    ]
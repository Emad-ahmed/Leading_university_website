from django.db import models


class Faculty(models.Model):
    course_name = models.CharField(max_length=120)
    teacher_name = models.CharField(max_length=100)
    Phone = models.IntegerField()
    biography = models.TextField()
    area_of_study = models.TextField()
    teacherimg = models.ImageField(
        upload_to='images/', default="myimg", blank=True)

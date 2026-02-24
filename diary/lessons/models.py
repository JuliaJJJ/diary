from django.db import models
from users.models import User
from school.models import SchoolClass, Subject


class Lesson(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)


class Grade(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    value = models.IntegerField()

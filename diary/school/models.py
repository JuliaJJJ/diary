from django.db import models
from django.conf import settings


class SchoolClass(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    school_class = models.ForeignKey(
        SchoolClass,
        on_delete=models.CASCADE
    )
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE
    )
    teacher = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'teacher'}
    )
    date = models.DateField()

    def __str__(self):
        return f"{self.subject} - {self.school_class} ({self.date})"


class Attendance(models.Model):
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE
    )
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'student'}
    )
    is_present = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.student} - {self.lesson}"
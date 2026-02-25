from django.db import models
from django.conf import settings


class Lesson(models.Model):
    subject = models.CharField(max_length=100)
    school_class = models.CharField(max_length=50)
    date = models.DateField()
    teacher = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='lessons_taught'
    )

    def __str__(self):
        return f"{self.subject} - {self.date}"


class Attendance(models.Model):
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        related_name='attendances'
    )
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='lesson_attendance'
    )
    is_present = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.student} - {self.lesson}"
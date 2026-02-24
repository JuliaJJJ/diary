from django.db import models

class SchoolClass(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
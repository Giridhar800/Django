from django.db import models

# Create your models here.
class StudentModel(models.Model):
    name = models.CharField(max_length=20)
    mail = models.EmailField(max_length=30)
    msg = models.CharField(max_length=30)

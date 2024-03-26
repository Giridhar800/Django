from django.db import models

# Create your models here.
class Student1(models.Model):
    name = models.CharField(max_length=20)
    mail = models.EmailField(max_length=20)
    address = models.CharField(max_length=30)

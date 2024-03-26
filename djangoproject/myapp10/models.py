from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=20)
    mailid = models.EmailField(max_length=30)
    address = models.CharField(max_length=20)
    password = models.CharField(max_length=10)

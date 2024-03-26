from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=20)
    eid = models.EmailField(unique=True, null=False)
    eaddress = models.CharField(max_length=20)
    age = models.IntegerField()
    dob = models.DateField()

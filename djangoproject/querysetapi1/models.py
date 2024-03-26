from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=20)
    eid = models.IntegerField(unique=True,null=False)
    eaddress = models.CharField(max_length=30)
    age = models.IntegerField()
    dob = models.DateField()

class Manager(models.Model):
    mname = models.CharField(max_length=20)
    eaddress = models.CharField(max_length=30)
    salary = models.IntegerField()
    dob = models.DateField()

class Student(models.Model):
    name = models.CharField(max_length=20)
    sid = models.IntegerField()
    address = models.CharField(max_length=30)
    marks = models.IntegerField()
    passdate = models.DateField()
    admitdate = models.DateTimeField()


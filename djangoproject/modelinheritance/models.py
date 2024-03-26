from django.db import models

# Create your models here.
# abstract base class model inheritance
class Commoninfo(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    date = models.DateField()
    class Meta:
        abstract = True

class Trainer(Commoninfo):
    address = models.CharField(max_length=30)
    date = None

class Teacher(Commoninfo):
    date = models.DateTimeField()
    salary = models.IntegerField()

# Multi TABLE Inheretence
class Bank(models.Model):
    bname = models.CharField(max_length=20)
    baddress = models.CharField(max_length=30)
class BankManager(Bank):
    name = models.CharField(max_length=20)
    age = models.IntegerField()

# Proxy model Inheritance
class University(models.Model):
    uname = models.CharField(max_length=20)
    ulocation = models.CharField(max_length=30)
class College(University):
    class Meta:
        proxy = True




from django.db import models


# Create your models here.
class Mydata(models.Model):
    name = models.CharField(max_length=20)
    mno = models.IntegerField()

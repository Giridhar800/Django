from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, primary_key=True)
    bookn = models.CharField(max_length=20)
    booka = models.CharField(max_length=30)
    bookpd = models.DateField()

class Post(models.Model):
    user =models.ForeignKey(User, on_delete=models.CASCADE)
    p_title = models.CharField(max_length=20)
    p_category = models.CharField(max_length=20)
    p_publishdate = models.DateField()

class Dance(models.Model):
    user = models.ManyToManyField(User)
    dance_name = models.CharField(max_length=20)
    dance_duration = models.IntegerField()
    def dance_by(self):
        return ",".join([str(d) for d in self.user.all()])
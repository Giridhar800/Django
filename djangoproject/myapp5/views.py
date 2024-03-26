from django.shortcuts import render
from django.http import HttpResponse
import datetime

#Create your views here.

def date_time(request):
    dt = datetime.datetime.now()
    return render(request, "h18.html", {"dt": dt})


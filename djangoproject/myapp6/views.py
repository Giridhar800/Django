from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee


# Create your views here.
def displayemp(request):
    emp = Employee.objects.all()
    return render(request, 'h19.html', {'emp': emp})



from django.shortcuts import render
from django.http import HttpResponse
from myapp8 import forms

# Create your views here.
def Studentview(request):
    form = forms.StudentForms()

    myform = {"form": form}
    return render(request, "h21.html", context=myform)



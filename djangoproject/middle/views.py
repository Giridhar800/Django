from django.shortcuts import render, HttpResponse


# Create your views here.
def home_view(request):
    # print(10/0)
    return HttpResponse('This is home page')
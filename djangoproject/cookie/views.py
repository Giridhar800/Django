from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def setcookie(request):
    response = HttpResponse("Cookie is set")
    response.set_cookie("name", "Giri")
    return response

def getcookie(request):
    n = request.COOKIES["name"]
    return HttpResponse("Your name is:"+n)

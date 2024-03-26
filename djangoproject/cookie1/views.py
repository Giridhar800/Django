from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, timedelta

# Create your views here.
def setcookie(request):
    response = render(request, "set.html")
    response.set_cookie("name", "Giridhar", max_age=60)
    return response

def getcookie(request):
    n = request.COOKIES.get("name", "Cookie is deleted")
    return render(request, "get.html", {"name": n})

def delcookie(request):
    response = render(request, "del.html")
    response.delete_cookie("name")
    return response
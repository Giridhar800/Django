from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def count_view(request):
    if 'count' in request.COOKIES:
        newcount = int(request.COOKIES['count'])+1
    else:
        newcount = 1

    response = render(request, "count.html", {'count': newcount})
    response.set_cookie("count", newcount)
    return response

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def page_count_view(request):
    count = request.session.get('count', 0)
    newcount = count+1
    request.session['count'] = newcount
    return render(request, "pagecount.html", {"count": count})


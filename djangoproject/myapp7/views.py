from django.shortcuts import render
from myapp7.models import Mydata


# Create your views here.
def Mydetails(request):
    myobj = Mydata.objects.all()
    return render(request, "h20.html", {"myobj": myobj})

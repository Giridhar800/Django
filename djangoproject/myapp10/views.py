from django.shortcuts import render
from myapp10.forms import StudentForm
from myapp10.models import Students


# Create your views here.
def studentinputview(request):
    if request == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            nm = form.cleaned_data["name"]
            ml = form.cleaned_data["mailid"]
            ad = form.cleaned_data["address"]
            pw = form.cleaned_data["password"]
            s = Students(name=nm, mailid=ml, address=ad, password=pw)
            s.save()
    else:
        form = StudentForm()
    return render(request, "h24.html", {"form": form})


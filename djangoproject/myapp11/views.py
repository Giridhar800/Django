from django.shortcuts import render
from myapp11.forms import UserForm
from myapp11.models import User

# Create your views here.
def studentinputview(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            nm = form.cleaned_data["name"]
            pw = form.cleaned_data["password"]
            ad = form.cleaned_data["address"]
            s = User(name=nm, password=pw, address=ad)
            s.save()
    else:
        form = UserForm()
    return render(request, 'h25.html', {"form": form})






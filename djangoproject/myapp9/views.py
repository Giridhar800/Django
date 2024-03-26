from django.shortcuts import render
from myapp9.forms import StudentForm

# Create your views here.
def studentviewinput(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            print("Form validation is sucuss and printing data")
            print("student name:", form.cleaned_data["name"])
            print("student marks:",  form.cleaned_data["marks"])
            print("password:", form.cleaned_data["password"])
            print("rpassword:", form.cleaned_data["rpassword"])
    else:
        form = StudentForm()
    return render(request, 'h22.html', {"form": form})
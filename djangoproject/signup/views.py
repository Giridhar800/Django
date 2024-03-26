from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from signup.forms import signupForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect

# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        fm = signupForm(request.POST)
        if fm.is_valid():
            messages.success(request, "user creation successfully")
            fm.save()
    else:
        fm = signupForm()
    return render(request, 'signup.html', {'form': fm})

def user_login(request):
    if request.method == 'POST':
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            pwd = fm.cleaned_data['password']
            user = authenticate(username=uname, password=pwd)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/profile/')
        else:
            messages.info(request, 'invalid usser or pass')
    else:
        fm = AuthenticationForm()
    return render(request, 'login.html', {"form": fm})


def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html', {'name': request.user})
    else:
        return HttpResponseRedirect('/login/')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')




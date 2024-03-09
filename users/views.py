from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .forms import RegisterForm, LoginForm

def register(request):
    if request.user.is_authenticated:
        return redirect("quotes_app:index")
    
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("quotes_app:index")
        else:
            return render(request, "users/register.html", {"form": form})
        
    return render(request, "users/register.html", {"form": RegisterForm()})


def loginuser(request):
    if request.user.is_authenticated:
        return redirect("quotes_app:index")
    
    if request.method == "POST":
        user = authenticate(username=request.POST["username"], password=request.POST["password"])
        if user is None:
            messages.error(request, "Username or password is incorrect")
            return redirect(to="users:login")
        
        login(request, user)
        return redirect(reverse("quotes_app:index"))
    
    return render(request, "users/login.html", context={"form": LoginForm()})
            
            
@login_required
def logoutuser(request):
    logout(request)
    return redirect(reverse("quotes_app:index"))
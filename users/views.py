from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth import authenticate, login


# Create your views here.


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            messages.success(request, f"Welcome {username}, your account is created.")
            form.save()
            username = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password1"],
            )
            login(request, username)
            return redirect("/")
    else:
        form = RegisterForm()
    return render(request, "users/register.html", {"form": form})

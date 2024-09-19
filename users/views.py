from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth
from django.urls import reverse

from users.forms import UserLoginForm

# from django.contrib.auth import LoginView

# class LoginView(LoginView):
#     pass


def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid:
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)

            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse("main:index"))
        else:
            form = UserLoginForm()

    context = {"title": "Авторизация"}

    return render(request, "user/login.html", context=context)

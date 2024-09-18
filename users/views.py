from django.shortcuts import render


def login(request):
    context = {
        "title": "Авторизация"
    }

    return render(request, "user/login.html", context=context)

from django.urls import path
from users.views import *

app_name = "users"

urlpatterns = [
    path("login/", LoginAPI.as_view(), name="login"),
    # path("registration/", views.registration, name="registration"),
    # path("logout/", views.logout, name="logout"),
]

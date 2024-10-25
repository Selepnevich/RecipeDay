from django.urls import path
from main.views import *

app_name = "main"

urlpatterns = [
    path("", RecipeAPIList.as_view(), name="index"),
]

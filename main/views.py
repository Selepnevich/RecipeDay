from rest_framework import generics
from main.serializer import RecipeSerializer
from main.models import Recipe


class RecipeAPIList(generics.ListAPIView):
    "Отображает список рецептов"
    queryset=Recipe.objects.all()
    serializer_class = RecipeSerializer

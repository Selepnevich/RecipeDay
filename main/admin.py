from django.contrib import admin
from .models import Recipe, Category

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    ...
    # list_editable = ["name", "category","type_meal"]


@admin.register(Category)
class Category(admin.ModelAdmin):
    ...

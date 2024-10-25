from django.db import models
from django.utils.translation import gettext_lazy as _


class TypeMeal(models.TextChoices):
    BREAKFAST = "BREAKFAST", _("завтрак")
    LUNCH = "LUNCH", _("обед")
    DINNER = "DINNER", _("ужин")
    SNACK = "SNACK", _("перекус")
    BRUNCH = "BRUNCH", _("бранч")
    SUPPER = "SUPPER", _("поздний ужин")
    TEA = "TEA", _("чаепитие")
    OTHER = "OTHER", _("другое")


class Difficulty(models.TextChoices):
    EASY = "EASY", _("легкий")
    MEDIUM = "MEDIUM", _("средний")
    HARD = "HARD", _("сложный")
    EXPERT = "EXPERT", _("эксперт")


class Category(models.Model):
    name = models.CharField(max_length=225, verbose_name=_("наименование категории"))
    description = models.CharField(max_length=255, verbose_name=_("описание"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("категорию")
        verbose_name_plural = _("категории")


class Recipe(models.Model):
    name = models.CharField(max_length=225, verbose_name=_("название рецепта"))
    calories = models.IntegerField(blank=True, null=True, verbose_name=_("калории"))
    time_cooking = models.TimeField(
        blank=True, null=True, verbose_name=_("время приготовления")
    )
    description = models.CharField(
        max_length=255,
        verbose_name=_("описание"),
        blank=True,
        null=True,
    )

    category = models.ForeignKey(
        to=Category,
        on_delete=models.CASCADE,
        verbose_name=_("категория"),
        blank=True,
        null=True,
    )
    type_meal = models.CharField(
        max_length=10,
        choices=TypeMeal.choices,
        blank=True,
        null=True,
        verbose_name=_("тип приема пищи"),
    )
    difficulty = models.CharField(
        max_length=10,
        choices=Difficulty.choices,
        blank=True,
        null=True,
        verbose_name=_("сложность"),
    )

    def __str__(self):
        return f"{self.name} | {self.category}"

    class Meta:
        verbose_name = _("рецепт")
        verbose_name_plural = _("рецепты")

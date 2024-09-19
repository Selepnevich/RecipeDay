from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(
            upload_to="user_images", blank=True, null=True, verbose_name="Аватар"
    )

    phone_number = models.CharField(max_length=10, blank=True, null=True, verbose_name="номер телефона")

    class Meta:
        verbose_name = "Пользователя"
        verbose_name_plural = "Пользователи"

    def __str__(self) -> str:
        return self.username

    


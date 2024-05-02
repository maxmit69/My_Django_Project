from django.contrib.auth.models import AbstractUser
from django.db import models

from catalog.models import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="почта", )

    phone = models.CharField(max_length=30, verbose_name="телефон", **NULLABLE)
    avatar = models.ImageField(upload_to='users/', **NULLABLE, verbose_name="аватар")
    country = models.CharField(max_length=150, verbose_name="страна", **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"

    def __str__(self):
        return self.email

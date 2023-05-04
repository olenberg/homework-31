from django.db import models
from django.contrib.auth.models import AbstractUser
from users.validators import check_min_age, not_rambler_email


class Location(models.Model):
    name = models.CharField(max_length=150)
    lat = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True)
    lng = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True)

    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"

    def __str__(self):
        return self.name


class UserRoles(models.TextChoices):
    ADMIN = "admin", "Администратор"
    MODERATOR = "moderator", "Модератор"
    MEMBER = "member", "Пользователь"


class User(AbstractUser):
    role = models.CharField(max_length=100, choices=UserRoles.choices, default=UserRoles.MEMBER)
    age = models.PositiveIntegerField(null=True, blank=True, validators=[check_min_age])
    location = models.ManyToManyField(Location)
    email = models.EmailField(unique=True, null=True, blank=True, validators=[not_rambler_email])

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username

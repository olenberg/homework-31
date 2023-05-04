from django.db import models
from users.models import User
from categories.models import Category
from django.core.validators import MinLengthValidator


class Ad(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False, validators=[MinLengthValidator(10)])
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    price = models.PositiveIntegerField()
    description = models.TextField(max_length=2000, null=True, blank=True)
    is_published = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to="ads/", null=True, blank=True)


    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

    def __str__(self):
        return self.name

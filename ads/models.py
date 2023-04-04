from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Ads(models.Model):
    name = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    price = models.PositiveIntegerField()
    description = models.TextField(max_length=2000, null=True)
    address = models.CharField(max_length=150)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.name

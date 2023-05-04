import factory.django
from ads.models import Ad
from categories.models import Category
from users.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("name")
    password = "123qwe"
    role = "admin"
    email = factory.Faker("email")


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker("name")


class AdFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ad

    name = "test name ad"
    description = "test description"
    author = factory.SubFactory(UserFactory)
    category = factory.SubFactory(CategoryFactory)
    price = 1000



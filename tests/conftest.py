import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "avito.settings")
django.setup()


from pytest_factoryboy import register
from tests.factories import UserFactory, AdFactory, CategoryFactory


pytest_plugins = ["tests.fixtures"]


register(UserFactory)
register(CategoryFactory)
register(AdFactory)

import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'avito.settings')
application = get_wsgi_application()
import csv
from pathlib import Path
from ads.models import Ad
from categories.models import Category
from users.models import Location, User


PATH_TO_DATA = Path.cwd() / "datasets"
CSV_ADS = "ad.csv"
CSV_CATEGORIES = "category.csv"
CSV_LOCATION = "location.csv"
CSV_USER = "user.csv"


with open(PATH_TO_DATA / CSV_ADS, "r", encoding="utf-8") as f:
    for i in csv.DictReader(f):
        user = User.objects.get(pk=i["author_id"])
        category = Category.objects.get(pk=i["category_id"])
        Ad.objects.create(
            name=i["name"],
            author=user,
            price=i["price"],
            description=i["description"],
            is_published=True if i["is_published"] == "TRUE" else False,
            image=i["image"],
            category=category
        )

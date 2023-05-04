# import os
# from django.core.wsgi import get_wsgi_application
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'avito.settings')
# application = get_wsgi_application()
import csv
import json
from pathlib import Path
# from ads.models import Ad
# from categories.models import Category
# from users.models import Location, User
#
#
# PATH_TO_DATA = Path.cwd() / "datasets"
# CSV_ADS = "ad.csv"
# CSV_CATEGORIES = "category.csv"
# CSV_LOCATION = "location.csv"
# CSV_USER = "user.csv"
#
#
# with open(PATH_TO_DATA / CSV_ADS, "r", encoding="utf-8") as f:
#     for i in csv.DictReader(f):
#         user = User.objects.get(pk=i["author_id"])
#         category = Category.objects.get(pk=i["category_id"])
#         Ad.objects.create(
#             name=i["name"],
#             author=user,
#             price=i["price"],
#             description=i["description"],
#             is_published=True if i["is_published"] == "TRUE" else False,
#             image=i["image"],
#             category=category
#         )
# def convert(csv_file, json_file, model):
#     result = []
#     with open(PATH_TO_DATA / csv_file, "r", encoding="utf-8") as csv_f:
#         for row in csv.DictReader(csv_f):
#             if "is_published" in row:
#                 if row["is_published"] == "TRUE":
#                     row["is_published"] = True
#                 else:
#                     row["is_published"] = False
#
#             if "location_id" in row:
#                 row["locations"] = [row["location_id"]]
#                 del row["location_id"]
#
#             result.append({"model": model, "fields": row})
#     with open(PATH_TO_DATA / json_file, "w", encoding="utf-8") as json_f:
#         json_f.write(json.dumps(result, ensure_ascii=False))


# if __name__ == "__main__":
    # convert("category.csv", "category.json", "categories.category")
    # convert("ad.csv", "ad.json", "ads.ad")
    # convert("location.csv", "location.json", "users.location")
    # convert("user.csv", "user.json", "users.user")

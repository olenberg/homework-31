from avito.wsgi import *
import csv
import json
from ads.models import Ad, Category


with open("datasets/ads.json", "r", encoding="utf-8") as f:
    for row in json.load(f):
        Ad.objects.create(
                            pk=row["pk"],
                            name=row["fields"]["name"],
                            author=row["fields"]["author"],
                            price=row["fields"]["price"],
                            description=row["fields"]["description"],
                            address=row["fields"]["address"],
                            is_published=row["fields"]["is_published"]
)

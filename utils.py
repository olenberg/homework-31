import json
import csv
from pathlib import Path


PATH_TO_DATA = Path.cwd() / "datasets"
CSV_ADS = "ads.csv"
JSON_ADS = "ads.json"
CSV_CATEGORIES = "categories.csv"
JSON_CATEGORIES = "categories.json"


def csv_to_json(csvfile, jsonfile, model_name):
    with open(PATH_TO_DATA / csvfile, mode="r", encoding="utf-8") as f:
        result = []
        for row in csv.DictReader(f):
            to_add = {"model": model_name, "pk": int(row["Id"] if "Id" in row else row["id"])}
            if "Id" in row:
                del row["Id"]
            else:
                del row["id"]
            if "price" in row:
                row["price"] = int(row["price"])
            if "is_published" in row:
                if row["is_published"] == "TRUE":
                    row["is_published"] = True
                else:
                    row["is_published"] = False
            to_add["fields"] = row
            result.append(to_add)

    with open(PATH_TO_DATA / jsonfile, mode="w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=4)


csv_to_json(CSV_CATEGORIES, JSON_CATEGORIES, "ads.category")
csv_to_json(CSV_ADS, JSON_ADS, "ads.ad")

import os
import json

from app.data import list_files


if not os.path.exists(list_files.products):
    with open(list_files.products, "w", encoding="utf-8") as fh:
        json.dump([], fh)


def get_products(path: str = list_files.products) -> list:
    with open(path, "r", encoding="utf-8") as fh:
        products = json.load(fh)

    return products
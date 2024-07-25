import os
import json

from app.data import list_files


if not os.path.exists(list_files.products):
    with open(list_files.products, "w", encoding="utf-8") as fh:
        json.dump([], fh)

if not os.path.exists(list_files.sold_products):
    with open(list_files.sold_products, "w", encoding="utf-8") as file:
        json.dump([], file)

if not os.path.exists(list_files.reviews):
    with open(list_files.reviews, "w", encoding="utf-8") as file:
        json.dump([], file)


def get_products(path: str = list_files.products) -> list:
    with open(path, "r", encoding="utf-8") as fh:
        products = json.load(fh)

    return products


def get_sold_products(path: str = list_files.sold_products) -> list:
    with open(path, "r", encoding="utf-8") as file:
        sold_products = json.load(file)

    return sold_products


def get_reviews(path: str = list_files.reviews) -> list:
    with open(path, "r", encoding="utf-8") as file:
        reviews = json.load(file)

    return reviews
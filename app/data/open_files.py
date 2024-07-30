import os
import json

from app.data import list_files


if not os.path.exists(list_files.animals):
    with open(list_files.animals, "w", encoding="utf-8") as fh:
        json.dump([], fh)

if not os.path.exists(list_files.animals_cured):
    with open(list_files.animals_cured, "w", encoding="utf-8") as file:
        json.dump([], file)

if not os.path.exists(list_files.reviews):
    with open(list_files.reviews, "w", encoding="utf-8") as file:
        json.dump([], file)


def get_animals(path: str = list_files.animals) -> list:
    with open(path, "r", encoding="utf-8") as fh:
        animals = json.load(fh)

    return animals


def get_animals_cured(path: str = list_files.animals_cured) -> list:
    with open(path, "r", encoding="utf-8") as file:
        get_animals_cured = json.load(file)

    return get_animals_cured


def get_reviews(path: str = list_files.reviews) -> list:
    with open(path, "r", encoding="utf-8") as file:
        reviews = json.load(file)

    return reviews
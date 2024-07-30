import json

from app.data import list_files, open_files



def add_animal(animal: str) -> str:
    animals = open_files.get_animals()

    if not animal in animals:
        animals.append(animal)

        with open(list_files.animals, "w", encoding="utf-8") as file:
            json.dump(animals, file)

        msg = f"Тварину '{animal}' успішно додано."
    else:
        msg = f"Тварина '{animal}' вже є у списку."

    return msg


def animals_cured(animal: str) -> str:
    animals = open_files.get_animals()
    animals_cured = open_files.get_animals_cured()

    if animal in animals:
        animals.remove(animal)
        animals_cured.append(animal)

        with open(list_files.animals, "w", encoding="utf-8") as file:
            json.dump(animals, file)

        with open(list_files.animals_cured, "w", encoding="utf-8") as file:
            json.dump(animals_cured, file)

        msg = f"Тварина '{animal}' успішно вилікувана."
    else:
        msg = f"Тварина '{animal}' відсутна у списку"

    return msg


def remove_animal(animal: str) -> str:
    animals = open_files.get_animals()

    if animal in animals:
        animals.remove(animal)

        with open(list_files.animals, "w", encoding="utf-8") as file:
            json.dump(animals, file)

        msg = f"Тварину '{animal}' успішно видалено зі списку"
    else:
        msg = f"Тварина '{animal}' відсутна у списку"

    return msg
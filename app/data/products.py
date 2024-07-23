import json

from app.data import list_files, open_files



def add_product(product: str) -> str:
    products = open_files.get_products()

    if not product in products:
        products.append(product)

        with open(list_files.products, "w", encoding="utf-8") as file:
            json.dump(products, file)

        msg = f"Товар '{product}' успішно додано."
    else:
        msg = f"Товар '{product}' вже є у списку."

    return msg


def sold_product(product: str) -> str:
    products = open_files.get_products()
    sold_products = open_files.get_sold_products()

    if product in products:
        products.remove(product)
        sold_products.append(product)

        with open(list_files.products, "w", encoding="utf-8") as file:
            json.dump(products, file)

        with open(list_files.sold_products, "w", encoding="utf-8") as file:
            json.dump(sold_products, file)

        msg = f"Товар '{product}' успішно продано."
    else:
        msg = f"Товар '{product}' відсутній у списку"

    return msg


def remove_product(product: str) -> str:
    products = open_files.get_products()

    if product in products:
        products.remove(product)

        with open(list_files.products, "w", encoding="utf-8") as file:
            json.dump(products, file)

        msg = f"Товар '{product}' успішно видалено"
    else:
        msg = f"Товар '{product}' відсутній у списку"

    return msg
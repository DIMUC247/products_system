from aiogram.utils.keyboard import InlineKeyboardBuilder


def build_products_keyboard(products: list):
    builder = InlineKeyboardBuilder()
    for product in products:
        builder.button(text=product, callback_data=f"product_{product}")

    builder.adjust(4)
    return builder.as_markup()


def build_prod_action_keyboard(product: str):
    builder = InlineKeyboardBuilder()
    builder.button(text="Продати товар", callback_data=f"sold_prod_{product}")
    builder.button(text="Видалити товар", callback_data=f"remove_prod_{product}")
    return builder.as_markup()
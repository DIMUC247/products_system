from aiogram.utils.keyboard import InlineKeyboardBuilder


def build_products_keyboard(products: list):
    builder = InlineKeyboardBuilder()
    for product in products:
        builder.button(text=product, callback_data=product)

    builder.adjust(4)
    return builder.as_markup()
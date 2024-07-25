from aiogram.utils.keyboard import ReplyKeyboardBuilder


def build_global_menu_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.button(text="Список товарів")
    builder.button(text="Додати новий товар")
    builder.button(text="Показати список проданий товарів")
    builder.button(text="Показати всі відгуки")
    builder.button(text="Додати відгук")
    builder.adjust(1)
    return builder.as_markup()

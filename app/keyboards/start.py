from aiogram.utils.keyboard import ReplyKeyboardBuilder


def build_global_menu_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.button(text="Список тварин")
    builder.button(text="Додати нову тварину до списку")
    builder.button(text="Показати список вилікуваних тварин")
    builder.button(text="Показати всі відгуки")
    builder.button(text="Додати відгук")
    builder.adjust(1)
    return builder.as_markup()

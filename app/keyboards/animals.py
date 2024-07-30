from aiogram.utils.keyboard import InlineKeyboardBuilder


def build_animals_keyboard(animals: list):
    builder = InlineKeyboardBuilder()
    for animal in animals:
        builder.button(text=animal, callback_data=f"animal_{animal}")

    builder.adjust(4)
    return builder.as_markup()


def build_anim_action_keyboard(animal: str):
    builder = InlineKeyboardBuilder()
    builder.button(text="Вилікувати тварину", callback_data=f"cured_anim_{animal}")
    builder.button(text="Видалити тварину зі списку", callback_data=f"remove_anim_{animal}")
    return builder.as_markup()
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from app.data import animals, open_files
from app.keyboards.animals import build_animals_keyboard, build_anim_action_keyboard
from app.forms.animal import AnimalForm


animal_router = Router()


async def edit_or_answer(message: Message, text: str, keyboard=None, *args, **kwargs):
   if message.from_user.is_bot:
       await message.edit_text(text=text, reply_markup=keyboard, **kwargs)
   else:
       await message.answer(text=text, reply_markup=keyboard, **kwargs)


@animal_router.message(F.text == "Список тварин")
async def show_animals(message: Message, state: FSMContext):
    animals = open_files.get_animals()
    keyboard = build_animals_keyboard(animals)
    text = "Список тварин"
    return await edit_or_answer(message=message, text=text, keyboard=keyboard)


@animal_router.callback_query(F.data.startswith("animal_"))
async def animal_actions(call_back: CallbackQuery, state: FSMContext):
    animal = call_back.data.split("_")[-1]
    keyboard = build_anim_action_keyboard(animal)
    return await edit_or_answer(
        message=call_back.message,
        text=animal,
        keyboard=keyboard
        )


@animal_router.message(F.text == "Додати нову тварину")
async def add_animals(message: Message, state: FSMContext):
    await state.clear()
    await state.set_state(AnimalForm.name)
    await message.answer(text="Введіть назву тварини")


@animal_router.message(AnimalForm.name)
async def add_animal_action(message: Message, state: FSMContext):
    data = await state.update_data(name=message.text)
    await state.clear()
    msg = animals.add_animal(data.get("name"))
    await message.answer(text=msg)


@animal_router.callback_query(F.data.startswith("cured_anim_"))
async def animals_cured(call_back: CallbackQuery, state: FSMContext):
    animal = call_back.data.split("_")[-1]
    msg = animals.animals_cured(animal)
    await call_back.message.answer(text=msg)


@animal_router.callback_query(F.data.startswith("remove_prod_"))
async def remove_animal(call_back: CallbackQuery, state: FSMContext):
    animal = call_back.data.split("_")[-1]
    msg = animals.remove_animal(animal)
    await call_back.message.answer(text=msg)


@animal_router.message(F.text == "Показати список вилікуваних тварин")
async def show_animals_cured(message: Message, state: FSMContext):
    animals_cured = open_files.get_animals_cured()
    msg = ""

    for i, animal in enumerate(animals_cured, start=1):
        msg += f"{i}. {animal}\n"

    await message.answer(text=msg)
from aiogram import Router, F
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from aiogram.fsm.context import FSMContext

from app.data import open_files
from app.keyboards.products import build_products_keyboard


product_router = Router()


async def edit_or_answer(message: Message, text: str, keyboard=None, *args, **kwargs):
   if message.from_user.is_bot:
       await message.edit_text(text=text, reply_markup=keyboard, **kwargs)
   else:
       await message.answer(text=text, reply_markup=keyboard, **kwargs)



@product_router.message(F.text == "Список товарів")
async def show_products(message: Message, state: FSMContext):
    products = open_files.get_products()
    keyboard = build_products_keyboard(products)
    text = "Список товарів"
    return await edit_or_answer(message=message, text=text, keyboard=keyboard)
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from app.data import open_files, products
from app.keyboards.products import build_products_keyboard, build_prod_action_keyboard
from app.forms.product import ProductForm


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


@product_router.callback_query(F.data.startswith("product_"))
async def product_actions(call_back: CallbackQuery, state: FSMContext):
    product = call_back.data.split("_")[-1]
    keyboard = build_prod_action_keyboard(product)
    return await edit_or_answer(
        message=call_back.message,
        text=product,
        keyboard=keyboard
        )


@product_router.message(F.text == "Додати новий товар")
async def add_products(message: Message, state: FSMContext):
    await state.clear()
    await state.set_state(ProductForm.name)
    await message.answer(text="Введіть назву товару")


@product_router.message(ProductForm.name)
async def add_product_action(message: Message, state: FSMContext):
    data = await state.update_data(name=message.text)
    await state.clear()
    msg = products.add_product(data.get("name"))
    await message.answer(text=msg)


@product_router.callback_query(F.data.startswith("sold_prod_"))
async def sold_product(call_back: CallbackQuery, state: FSMContext):
    product = call_back.data.split("_")[-1]
    msg = products.sold_product(product)
    await call_back.message.answer(text=msg)


@product_router.callback_query(F.data.startswith("remove_prod_"))
async def remove_product(call_back: CallbackQuery, state: FSMContext):
    product = call_back.data.split("_")[-1]
    msg = products.remove_product(product)
    await call_back.message.answer(text=msg)


@product_router.message(F.text == "Показати список проданий товарів")
async def show_sold_products(message: Message, state: FSMContext):
    sold_products = open_files.get_sold_products()
    msg = ""

    for i, product in enumerate(sold_products, start=1):
        msg += f"{i}. {product}\n"

    await message.answer(text=msg)
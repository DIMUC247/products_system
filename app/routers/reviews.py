from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from app.data import open_files, reviews
from app.forms.review import ReviewForm


review_router = Router()


@review_router.message(F.text == "Показати всі відгуки")
async def show_reviews(message: Message, state: FSMContext):
    reviews = open_files.get_reviews()
    msg = ""

    for i, review in enumerate(reviews, start=1):
        msg += f"{i}. {review}\n"

    await message.answer(text=msg)


@review_router.message(F.text == "Додати відгук")
async def add_review(message: Message, state: FSMContext):
    await state.clear()
    await state.set_state(ReviewForm.text)
    await message.answer(text="Напишіть свій відгук")


@review_router.message(ReviewForm.text)
async def add_review_action(message: Message, state: FSMContext):
    data = await state.update_data(text=message.text)
    await state.clear()
    msg = reviews.add_review(data.get('text'))
    await message.answer(text=msg)
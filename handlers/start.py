from aiogram import Router, types
from aiogram.filters import Command
from keyboards import menu_keyboard

router = Router()

@router.message(Command("start"))
async def start_handler(message: types.Message):
    text = (
        "Привет, я Мария и помогаю людям решать проблемы через нейрографику.\n\n"
        "Выбери, что ты хочешь:\n"
        "1. Курс по нейрографике\n"
        "2. Вытянуть карту"
    )
    await message.answer(text, reply_markup=menu_keyboard)

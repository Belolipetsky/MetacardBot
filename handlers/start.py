from aiogram import Router, types
from aiogram.filters import Command
from keyboards import menu_keyboard
from handlers.admin import admin_data  # Можно использовать админ-настройки для приветствия

router = Router()

@router.message(Command("start"))
async def start_handler(message: types.Message):
    # Используем настраиваемое приветствие из админ-панели (если оно изменено)
    greeting_text = admin_data.get("greeting_text", "Привет, я Мария и помогаю людям решать проблемы через нейрографику.")
    text = (
        f"{greeting_text}\n\n"
        "Выбери, что ты хочешь:\n"
        "1. Курс по нейрографике\n"
        "2. Вытянуть карту"
    )
    await message.answer(text, reply_markup=menu_keyboard)

# handlers/start.py
# Дополнительный обработчик для возврата в главное меню (если требуется)
from aiogram import Router, types
from aiogram.filters import Command
from utils.keyboards import main_menu_keyboard

router = Router()

@router.message(Command("home"))
async def home_handler(message: types.Message):
    await message.answer("Главное меню:", reply_markup=main_menu_keyboard)


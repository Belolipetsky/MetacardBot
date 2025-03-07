# handlers/start.py
from aiogram import Router, types
from aiogram.filters import Command
from utils.keyboards import main_menu_keyboard

router = Router()

@router.message(Command("home"))
async def home_handler(message: types.Message):
    text = "Главное меню:"
    await message.answer(text, reply_markup=main_menu_keyboard)

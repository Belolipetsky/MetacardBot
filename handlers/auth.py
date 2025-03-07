# handlers/auth.py
from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from utils.storage import register_user
from utils.spreadsheet import log_registration
from utils.keyboards import main_menu_keyboard

router = Router()

# Временное хранилище для номера телефона
pending_phones = {}

# Клавиатура для отправки номера
phone_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📱 Отправить номер", request_contact=True)]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

@router.message(Command("start"))
async def start_handler(message: types.Message):
    text = (
        "✨ Привет! Добро пожаловать в бота для нейрографики и метафорических карт.\n"
        "Чтобы начать, пожалуйста, отправьте свой номер телефона."
    )
    await message.answer(text, reply_markup=phone_keyboard)

@router.message(content_types=types.ContentType.CONTACT)
async def contact_handler(message: types.Message):
    contact = message.contact
    phone = contact.phone_number
    user_id = message.from_user.id
    pending_phones[user_id] = phone
    text = "Спасибо! Теперь, пожалуйста, введите своё имя:"
    await message.answer(text)

@router.message()
async def name_handler(message: types.Message):
    user_id = message.from_user.id
    if user_id not in pending_phones:
        return  # Сообщение не связано с авторизацией
    name = message.text.strip()
    phone = pending_phones.pop(user_id)
    username = message.from_user.username or ""
    register_user(user_id, username, name, phone)
    # Логируем регистрацию в Google Таблицы (заглушка)
    log_registration({
        "user_id": user_id,
        "username": username,
        "name": name,
        "phone": phone
    })
    text = (
        f"Спасибо, {name}! Вы успешно авторизованы.\n\n"
        "Выберите действие из меню ниже."
    )
    await message.answer(text, reply_markup=main_menu_keyboard)

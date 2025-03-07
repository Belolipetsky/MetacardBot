# handlers/auth.py
from aiogram import Router, types
from aiogram.filters import Command
from utils.storage import register_user
from utils.spreadsheet import log_registration
from utils.keyboards import phone_keyboard, main_menu_keyboard
import logging

router = Router()

# Временное хранилище для номера телефона
pending_phones = {}

@router.message(Command("start"))
async def start_handler(message: types.Message):
    welcome_text = (
        "✨ Привет, я Маша!\n"
        "Я эксперт по нейрографике и знаю, как через специальные алгоритмы и метафорические карты помочь тебе увидеть скрытые решения и получить инсайт.\n\n"
        "Что это даёт?\n"
        "🖊 Помогает взглянуть на ситуацию под другим углом\n"
        "🔮 Достаёт из подсознания ключевые послания и ответы\n"
        "⚡ Даёт ясность, уверенность и энергию для действий\n\n"
        "💡 Давай начнём! Чтобы я могла лучше помочь тебе, нужно немного информации.\n"
        "📌 Нажми на кнопку ниже и отправь свой номер телефона:"
    )
    await message.answer(welcome_text, reply_markup=phone_keyboard)

@router.message(lambda message: message.contact is not None)
async def contact_handler(message: types.Message):
    contact = message.contact
    phone = contact.phone_number
    user_id = message.from_user.id
    pending_phones[user_id] = phone
    await message.answer("✨ Отлично! Теперь скажи, как тебя зовут?")

@router.message(lambda message: message.contact is None)
async def name_handler(message: types.Message):
    user_id = message.from_user.id
    if user_id not in pending_phones:
        return  # Сообщение не связано с авторизацией
    name = message.text.strip()
    phone = pending_phones.pop(user_id)
    username = message.from_user.username or ""
    register_user(user_id, username, name, phone)
    log_registration({
        "user_id": user_id,
        "username": username,
        "name": name,
        "phone": phone
    })
    await message.answer(
        f"✨ Спасибо, {name}! Теперь всё готово! Давай посмотрим, что подскажет тебе твоя карта сегодня или попробуем освоить нейрографику.",
        reply_markup=main_menu_keyboard
    )


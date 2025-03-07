from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from utils.storage import register_user
from utils.spreadsheet import log_registration
from utils.keyboards import main_menu_keyboard, phone_keyboard

router = Router()
pending_phones = {}  # Временное хранилище для номера телефона

@router.message(Command("start"))
async def start_handler(message: types.Message):
    text = (
        "✨ Привет, я Маша!\n"
        "Я эксперт по нейрографике и знаю, как через специальные алгоритмы и метафорические карты помочь тебе увидеть скрытые решения и получить инсайт.\n"
        "Что это даёт?\n"
        "🖊 Помогает взглянуть на ситуацию под другим углом\n"
        "🔮 Достаёт из подсознания ключевые послания и ответы\n"
        "⚡ Даёт ясность, уверенность и энергию для действий\n"
        "💡 Давай начнём! Чтобы я могла лучше помочь тебе, нужно немного информации.\n"
        "📌 Нажми на кнопку ниже и отправь свой номер телефона:"
    )
    await message.answer(text, reply_markup=phone_keyboard)

@router.message(lambda message: message.contact is not None)
async def contact_handler(message: types.Message):
    contact = message.contact
    phone = contact.phone_number
    user_id = message.from_user.id
    pending_phones[user_id] = phone
    text = "✨ Отлично! Теперь скажи, как тебя зовут?"
    await message.answer(text)

@router.message()
async def name_handler(message: types.Message):
    user_id = message.from_user.id
    if user_id not in pending_phones:
        return  # Сообщение не относится к регистрации
    name = message.text.strip()
    phone = pending_phones.pop(user_id)
    username = message.from_user.username or ""
    register_user(user_id, username, name, phone)
    # Заглушка для логирования регистрации в Google Таблицы
    log_registration({"user_id": user_id, "username": username, "name": name, "phone": phone})
    text = (
        f"✨ Спасибо, {name}! Теперь всё готово! Давай посмотрим, что подскажет тебе твоя карта сегодня или попробуем освоить нейрографику.\n"
        "🔹 Выбери, что хочешь сделать:\n"
        "🔮 Вытянуть метафорическую карту – получи ответ от подсознания прямо сейчас\n"
        "🎓 Записаться на сессию – открой для себя метод, который меняет мышление"
    )
    await message.answer(text, reply_markup=main_menu_keyboard)



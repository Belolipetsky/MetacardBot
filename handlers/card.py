from aiogram import Router, types, exceptions
from aiogram.filters import Text
from utils.storage import get_attempts, use_attempt, add_attempts
from utils.keyboards import buy_keyboard, card_options_keyboard
router = Router()

# Словарь с описаниями карт
card_descriptions = {
    "1": "🔮 Карта 1: Символизирует новые начинания и свежий взгляд на ситуацию.",
    "2": "🔮 Карта 2: Говорит о завершении цикла и готовности к переменам.",
    "3": "🔮 Карта 3: Указывает на твою внутреннюю силу и уверенность."
}

# При нажатии кнопки "🔮 Вытянуть карту" выводится интро с предложением вытянуть карту
@router.message(Text(text="🔮 Вытянуть карту", ignore_case=True))
async def card_intro(message: types.Message):
    text = (
        "🔮 Метафорические карты – это способ получить ответ от подсознания.\n"
        "Каждая карта несёт послание, которое поможет тебе взглянуть на ситуацию с новой точки зрения.\n"
        "💡 Готов узнать, что тебе подскажет твоя карта?\n"
        "Нажми кнопку ниже:"
    )
    # Клавиатура с кнопкой "Да, вытянуть карту!"
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=[[types.KeyboardButton(text="Да, вытянуть карту!")]],
        resize_keyboard=True
    )
    await message.answer(text, reply_markup=keyboard)

# Обработка нажатия кнопки "Да, вытянуть карту!"
@router.message(Text(text="Да, вытянуть карту!", ignore_case=True))
async def pull_card_handler(message: types.Message):
    user_id = message.from_user.id
    if get_attempts(user_id) > 0:
        text = (
            "Чтобы выбрать карту, перейди в наш закрытый канал с картинками карт:\n"
            "👉 https://t.me/+Io5-yW5dgyEyNjhi\n\n"
            "После выбора карты вернись в бот и отправь номер выбранной карты (например, 1, 2 или 3)."
        )
        await message.answer(text)
    else:
        text = (
            "У тебя нет попыток для вытягивания карты.\n"
            "💳 Для вытягивания карты нужно пополнить баланс.\n"
            "Что выберешь?\n"
            "🔹 1 карта – 89₽ (Попробовать)\n"
            "🔹 5 карт – 356₽ (Экономия 20%)\n"
            "🔹 10 карт – 699₽ (Самая выгодная цена!)"
        )
        await message.answer(text, reply_markup=buy_keyboard)

# При получении номера карты (цифра)
@router.message(lambda message: message.text.isdigit())
async def card_choice(message: types.Message):
    user_id = message.from_user.id
    if get_attempts(user_id) <= 0:
        await message.answer("У тебя нет попыток. Попробуй получить бесплатную карту или пополни баланс.")
        return
    card_number = message.text.strip()
    description = card_descriptions.get(card_number, "❌ Карта с таким номером не найдена. Попробуй ещё раз.")
    if use_attempt(user_id):
        await message.answer(description)
        follow_text = (
            "🔮 Получил карту? Как думаешь, что она значит?\n"
            "Часто истинные ответы приходят через связь нескольких карт.\n"
            "🌟 Попробуй вытянуть ещё одну карту – это может дать более полное понимание ситуации."
        )
        await message.answer(follow_text, reply_markup=card_options_keyboard)
    else:
        await message.answer("Ошибка: не удалось списать попытку. Попробуй ещё раз.")

# Обработка получения бонусной бесплатной карты, если попыток нет
@router.message(Text(text="Получить бесплатную карту", ignore_case=True))
async def bonus_card(message: types.Message):
    user_id = message.from_user.id
    if get_attempts(user_id) == 0:
        add_attempts(user_id, 1)
        await message.answer("📢 Дарю тебе 1 карту бесплатно!")
    else:
        await message.answer("У тебя уже есть попытки для вытягивания карты.")


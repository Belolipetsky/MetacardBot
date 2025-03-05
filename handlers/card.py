from aiogram import Router, types
from aiogram.filters import Text

router = Router()

# Словарь с описаниями карт
card_descriptions = {
    "1": "🔮 Карта 1: Символизирует новые начинания и свежий взгляд на ситуацию.",
    "2": "🔮 Карта 2: Говорит о завершении цикла и готовности к переменам.",
    "3": "🔮 Карта 3: Указывает на вашу внутреннюю силу и уверенность в себе."
}

@router.message(Text(text="🔮Вытянуть карту", ignore_case=True))
async def card_intro(message: types.Message):
    text = (
        "✨ Метафорические карты — ключ к подсознанию! ✨\n\n"
        "Каждая карта содержит глубокие смыслы и может помочь вам найти ответы на важные вопросы.\n\n"
        "🔹 Как выбрать карту?\n"
        "1️⃣ Перейдите в наш закрытый канал, где вы увидите все доступные карты: [📲 Смотреть карты](https://t.me/+Io5-yW5dgyEyNjhi)\n"
        "2️⃣ Почувствуйте, какая карта вас притягивает, и запомните её номер.\n"
        "3️⃣ Вернитесь в этот бот и введите номер карты.\n\n"
        "✨ Доверьтесь своему внутреннему голосу — ответы уже рядом! 🔮"
    )
    await message.answer(text, parse_mode="Markdown", disable_web_page_preview=True)

@router.message(lambda message: message.text and message.text.isdigit())
async def card_choice(message: types.Message):
    card_number = message.text.strip()
    description = card_descriptions.get(card_number, "❌ Карта с таким номером не найдена. Попробуйте ещё раз.")
    await message.answer(description)

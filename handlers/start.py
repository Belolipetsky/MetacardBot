from aiogram import Router, types
from aiogram.filters import Command
from keyboards import menu_keyboard

router = Router()

# Жёстко зашитый текст приветствия и картинка (замени `GREETING_IMAGE_ID` на реальный file_id)
GREETING_IMAGE_ID = "AgADAgADq6cxG9JYZAcgbH2..."  # Вставь свой file_id

@router.message(Command("start"))
async def start_handler(message: types.Message):
    text = (
        "✨ **Привет, я Мария!**\n"
        "Я помогаю людям находить решения жизненных ситуаций с помощью **нейрографики и метафорических карт**.\n\n"
        "🖊 **Нейрографика** — это мощный инструмент, который раскрывает ваш потенциал, помогает снять блоки и обрести ясность.\n"
        "🃏 **Метафорические карты** — это уникальный способ получить инсайты и ответы на важные вопросы.\n\n"
        "🔹 **Выберите, что хотите сегодня:**\n"
        "1️⃣ **Погрузиться в мир нейрографики** (курс, который поможет вам лучше понять себя).\n"
        "2️⃣ **Вытянуть метафорическую карту** (узнать, что подсказывает ваше подсознание).\n\n"
        "⚡ Давайте вместе найдём лучшие решения и новые пути! 🚀"
    )


    await message.answer(text, reply_markup=menu_keyboard)

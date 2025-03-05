from aiogram import Router, types
from aiogram.filters import Text
from handlers.admin import admin_data  # Используем админ-настройки для описания курса

router = Router()

@router.message(Text(text="✨Курс по нейрографике", ignore_case=True))
async def course_handler(message: types.Message):
    course_text = admin_data.get("course_text", (
        "✨Курс по нейрографике:\n"
        "В этом курсе вы узнаете, как использовать нейрографику для решения жизненных проблем."
    ))
    await message.answer(course_text)

from aiogram import Router, types
from aiogram.filters import Text

router = Router()

@router.message(Text(text="Курс по нейрографике", ignore_case=True))
async def course_handler(message: types.Message):
    text = (
        "Курс по нейрографике:\n"
        "В этом курсе вы узнаете, как использовать нейрографику для решения жизненных проблем.\n"
        "Подробнее об обучении можно узнать в следующих сообщениях."
    )
    await message.answer(text)

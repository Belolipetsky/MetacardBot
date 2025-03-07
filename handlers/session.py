from aiogram import Router, types
from aiogram.filters import Text

router = Router()

@router.message(Text(text="🎓 Записаться на сессию", ignore_case=True))
async def book_session(message: types.Message):
    text = (
        "💡 Я могу провести личную сессию по нейрографике, чтобы помочь тебе осознать и трансформировать ситуацию.\n"
        "🎁 Бонус для тебя! Вживую я предложу вытащить карту из уникальных колод, которых нет в этом боте.\n"
        "🔹 Что будет на сессии?\n"
        "✨ Мы разберём твой запрос с помощью нейрографики и метафорических карт.\n"
        "🔮 Я помогу тебе увидеть скрытые смыслы и найти решения.\n"
        "🎨 Ты сможешь сам создать свой символический рисунок, который запустит нужные изменения.\n"
        "📌 Готов попробовать?"
    )
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text="🎓 Записаться на сессию")],
            [types.KeyboardButton(text="🔄 Подумать позже")]
        ],
        resize_keyboard=True
    )
    await message.answer(text, reply_markup=keyboard)


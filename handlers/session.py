# handlers/session.py
from aiogram import Router, types
from aiogram.filters import Text
from utils.storage import log_action
from utils.keyboards import session_keyboard

router = Router()

@router.message(Text(text="🎓 Записаться на сессию по нейрографике", ignore_case=True))
async def session_info(message: types.Message):
    session_text = (
        "💡 Я могу провести личную сессию по нейрографике, чтобы помочь тебе осознать и трансформировать ситуацию.\n"
        "Вживую я предложу вытащить карту из уникальных колод, которых нет в этом боте.\n\n"
        "🔹 Что будет на сессии?\n"
        "✨ Мы разберём твой запрос с помощью нейрографики и метафорических карт.\n"
        "🔮 Я помогу тебе увидеть скрытые смыслы и найти решения.\n"
        "🎨 Ты сможешь сам создать свой символический рисунок, который запустит нужные изменения.\n\n"
        "📌 Готов попробовать?"
    )
    await message.answer(session_text, reply_markup=session_keyboard)
    log_action(message.from_user.id, "session_info_requested", "User requested session info.")

@router.message(Text(text="🎓 Записаться на личную сессию", ignore_case=True))
async def book_session(message: types.Message):
    # Здесь можно реализовать сбор дополнительных данных для записи на сессию
    await message.answer("✅ Ваша заявка на личную сессию принята! Мы свяжемся с вами в ближайшее время.")
    log_action(message.from_user.id, "session_booked", "User booked a session.")

@router.message(Text(text="🔄 Подумать позже", ignore_case=True))
async def session_decline(message: types.Message):
    await message.answer("❌ Хорошо, если передумаете – всегда можете вернуться в главное меню.")
    log_action(message.from_user.id, "session_declined", "User chose to think later.")

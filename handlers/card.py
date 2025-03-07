# handlers/card.py
from aiogram import Router, types, exceptions
from aiogram.filters import Text
from utils.storage import get_attempts, use_attempt, add_attempts
from utils.keyboards import buy_keyboard, card_options_keyboard

router = Router()

card_descriptions = {
    "1": "🔮 Карта 1: Символизирует новые начинания и свежий взгляд на ситуацию.",
    "2": "🔮 Карта 2: Говорит о завершении цикла и готовности к переменам.",
    "3": "🔮 Карта 3: Указывает на вашу внутреннюю силу и уверенность в себе."
}

@router.message(Text(text="🔮 Вытянуть карту", ignore_case=True))
async def card_intro(message: types.Message):
    user_id = message.from_user.id
    attempts = get_attempts(user_id)
    if attempts > 0:
        text = (
            "✨ Метафорические карты — ключ к подсознанию! ✨\n\n"
            "У вас есть попытки для вытягивания карт.\n"
            "Пожалуйста, введите номер карты, которую хотите вытянуть:"
        )
        await message.answer(text)
    else:
        text = (
            "❌ У вас недостаточно попыток для вытягивания карты.\n"
            "Вы можете купить дополнительные попытки:\n"
            "💳 1 карта – 89₽\n"
            "💳 5 карт – 356₽ (экономия 20%)\n"
            "💳 10 карт – 699₽\n"
            "Выберите вариант ниже:"
        )
        await message.answer(text, reply_markup=buy_keyboard)

@router.message(lambda message: message.text and message.text.isdigit())
async def card_choice(message: types.Message):
    user_id = message.from_user.id
    if get_attempts(user_id) <= 0:
        await message.answer("❌ У вас нет попыток. Пожалуйста, купите дополнительные попытки.")
        return
    card_number = message.text.strip()
    description = card_descriptions.get(card_number, "❌ Карта с таким номером не найдена. Попробуйте ещё раз.")
    if use_attempt(user_id):
        await message.answer(description)
        follow_text = (
            "🔮 Получили карту? Как думаете, что она значит?\n"
            "Попробуйте вытянуть ещё одну карту для более полного понимания, или попробуйте позже."
        )
        await message.answer(follow_text, reply_markup=card_options_keyboard)
    else:
        await message.answer("❌ У вас недостаточно попыток. Пожалуйста, купите дополнительные попытки.")

@router.message(Text(text="Получить бесплатную карту", ignore_case=True))
async def bonus_card(message: types.Message):
    user_id = message.from_user.id
    BONUS_CHANNEL = "@your_channel_username"  # Замените на настоящий username вашего канала
    try:
        member = await message.bot.get_chat_member(BONUS_CHANNEL, user_id)
        if member.status in ["member", "creator", "administrator"]:
            add_attempts(user_id, 1)
            await message.answer("✅ Вы получили 1 бесплатную попытку за подписку на канал!")
        else:
            await message.answer("❌ Вы не подписаны на канал. Пожалуйста, подпишитесь и попробуйте снова.")
    except exceptions.TelegramBadRequest:
        await message.answer("❌ Ошибка проверки подписки. Попробуйте позже.")

# handlers/card.py
from aiogram import Router, types, exceptions
from aiogram.filters import Text
from utils.storage import get_attempts, use_attempt, add_attempts, log_action
from utils.keyboards import pull_card_confirmation_keyboard, buy_keyboard, card_options_keyboard
from utils.storage import log_action

router = Router()

# Словарь описаний карт
card_descriptions = {
    "1": "🔮 Карта 1: Символизирует новые начинания и свежий взгляд на ситуацию.",
    "2": "🔮 Карта 2: Говорит о завершении цикла и готовности к переменам.",
    "3": "🔮 Карта 3: Указывает на вашу внутреннюю силу и уверенность в себе."
}

@router.message(Text(text="🔮 Вытянуть метафорическую карту", ignore_case=True))
async def initiate_card_flow(message: types.Message):
    user_id = message.from_user.id
    text = (
        "🔮 Метафорические карты – это способ получить ответ от подсознания.\n"
        "Каждая карта несёт послание, которое поможет тебе взглянуть на ситуацию с новой точки зрения.\n"
        "💡 Готов узнать, что тебе подскажет твоя карта?"
    )
    await message.answer(text, reply_markup=pull_card_confirmation_keyboard)

@router.message(Text(text="Да, вытянуть карту", ignore_case=True))
async def pull_card(message: types.Message):
    user_id = message.from_user.id
    attempts = get_attempts(user_id)
    if attempts > 0:
        instruction = (
            "📌 Для вытягивания карты перейди в закрытый Telegram-канал с картинками карт:\n"
            "https://t.me/your_channel_link\n"
            "Выбери карту, запомни её номер и вернись в бот, чтобы отправить номер карты."
        )
        await message.answer(instruction)
        log_action(user_id, "pull_card_initiated", "User has attempts and was sent instructions.")
    else:
        purchase_text = (
            "💳 Для вытягивания карты нужно пополнить баланс.\n"
            "🔹 1 карта – 89₽ (Попробовать)\n"
            "🔹 5 карт – 356₽ (Экономия 20%)\n"
            "🔹 10 карт – 699₽ (Самая выгодная цена!)\n"
            "Выберите вариант ниже:"
        )
        await message.answer(purchase_text, reply_markup=buy_keyboard)

@router.message(lambda message: message.text and message.text.isdigit())
async def process_card_choice(message: types.Message):
    user_id = message.from_user.id
    if get_attempts(user_id) <= 0:
        await message.answer("❌ У вас нет попыток. Пожалуйста, купите дополнительные попытки или получите бесплатную карту.")
        return
    card_number = message.text.strip()
    description = card_descriptions.get(card_number, "❌ Карта с таким номером не найдена. Попробуйте ещё раз.")
    if use_attempt(user_id):
        await message.answer(description)
        follow_up = (
            "🔮 Получил карту? Как думаешь, что она значит?\n"
            "Часто истинные ответы приходят через связь нескольких карт.\n"
            "🌟 Попробуй вытянуть ещё одну карту – это может дать более полное понимание твоей ситуации."
        )
        await message.answer(follow_up, reply_markup=card_options_keyboard)
        log_action(user_id, "card_pulled", f"Card number: {card_number}")
    else:
        await message.answer("❌ У вас недостаточно попыток. Пожалуйста, купите дополнительные попытки или получите бесплатную карту.")

@router.message(Text(text="Получить бесплатную карту", ignore_case=True))
async def bonus_free_card(message: types.Message):
    user_id = message.from_user.id
    BONUS_CHANNEL = "your_channel_username"  # Укажите username канала без символа @
    try:
        member = await message.bot.get_chat_member(f"@{BONUS_CHANNEL}", user_id)
        if member.status in ["member", "creator", "administrator"]:
            add_attempts(user_id, 1)
            await message.answer("📢 Дарю тебе 1 карту бесплатно!")
            log_action(user_id, "bonus_card", "User received a free card for subscription.")
        else:
            await message.answer("❌ Вы не подписаны на канал. Подпишитесь и попробуйте снова.")
    except exceptions.TelegramBadRequest:
        await message.answer("❌ Ошибка проверки подписки. Попробуйте позже.")

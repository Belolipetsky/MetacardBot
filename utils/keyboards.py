# utils/keyboards.py
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🔮 Вытянуть карту")],
        [KeyboardButton(text="🎓 Записаться на личную сессию")],
        [KeyboardButton(text="Получить бесплатную карту")]
    ],
    resize_keyboard=True
)

buy_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Купить 1 карту")],
        [KeyboardButton(text="Купить 5 карт"), KeyboardButton(text="Купить 10 карт")]
    ],
    resize_keyboard=True
)

card_options_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🃏 Вытянуть ещё одну"), KeyboardButton(text="🔄 Попробовать позже")]
    ],
    resize_keyboard=True
)

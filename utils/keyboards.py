# utils/keyboards.py
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Главное меню после авторизации
main_menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🔮 Вытянуть метафорическую карту")],
        [KeyboardButton(text="🎓 Записаться на сессию по нейрографике")]
    ],
    resize_keyboard=True
)

# Клавиатура для отправки номера телефона
phone_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📱 Отправить номер", request_contact=True)]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

# Клавиатура для подтверждения вытягивания карты
pull_card_confirmation_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Да, вытянуть карту")]
    ],
    resize_keyboard=True
)

# Клавиатура для покупки попыток
buy_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Купить 1 карту")],
        [KeyboardButton(text="Купить 5 карт"), KeyboardButton(text="Купить 10 карт")]
    ],
    resize_keyboard=True
)

# Клавиатура для повторного вытягивания карты
card_options_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🃏 Вытянуть ещё одну"), KeyboardButton(text="🔄 Попробовать позже")]
    ],
    resize_keyboard=True
)

# Клавиатура для подтверждения записи на сессию
session_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🎓 Записаться на личную сессию"), KeyboardButton(text="🔄 Подумать позже")]
    ],
    resize_keyboard=True
)


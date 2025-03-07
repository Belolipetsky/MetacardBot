from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

phone_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📱 Отправить номер", request_contact=True)]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

main_menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🔮 Вытянуть карту"), KeyboardButton(text="🎓 Записаться на сессию")],
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



from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Курс по нейрографике"), KeyboardButton(text="Вытянуть карту")]
    ],
    resize_keyboard=True
)

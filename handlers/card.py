from aiogram import Router, types
from aiogram.filters import Text

router = Router()

# Словарь с описаниями карт
card_descriptions = {
    "1": "Описание карты 1: Символизирует новые начинания.",
    "2": "Описание карты 2: Означает завершение и переход к новому.",
    "3": "Описание карты 3: Показывает внутреннюю силу и уверенность."
}

@router.message(Text(text="Вытянуть карту", ignore_case=True))
async def card_intro(message: types.Message):
    text = (
        "Для выбора метафорической карты, пожалуйста, ознакомьтесь с картами в нашем закрытом канале.\n"
        "После этого вернитесь сюда и введите номер выбранной карты."
    )
    await message.answer(text)

@router.message(lambda message: message.text.isdigit())
async def card_choice(message: types.Message):
    card_number = message.text.strip()
    description = card_descriptions.get(card_number)
    if description:
        await message.answer(description)
    else:
        await message.answer("Карта с таким номером не найдена. Попробуйте еще раз.")

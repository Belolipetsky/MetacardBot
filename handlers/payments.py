# handlers/payments.py
from aiogram import Router, types
from aiogram.filters import Text
from utils.storage import add_attempts
from utils.spreadsheet import log_payment
from config.config import PAYMENT_OPTIONS, PAYMENT_PROVIDER_TOKEN

router = Router()

@router.message(Text(text=["Купить 1 карту", "Купить 5 карт", "Купить 10 карт"]))
async def purchase_attempts(message: types.Message):
    option = message.text
    if option not in PAYMENT_OPTIONS:
        return
    price_info = PAYMENT_OPTIONS[option]
    price = price_info["price"]
    title = option
    description = f"Покупка {price_info['attempts']} попыток для вытягивания карт."
    currency = "RUB"
    prices = [
        types.LabeledPrice(label=option, amount=price)
    ]
    await message.answer_invoice(
        title=title,
        description=description,
        provider_token=PAYMENT_PROVIDER_TOKEN,
        currency=currency,
        prices=prices,
        start_parameter="purchase_attempts",
        payload=str(price_info["attempts"])
    )

@router.pre_checkout_query()
async def pre_checkout(pre_checkout_q: types.PreCheckoutQuery):
    await pre_checkout_q.answer(ok=True)

@router.message(lambda message: getattr(message, "successful_payment", None) is not None)
async def successful_payment(message: types.Message):
    attempts_purchased = int(message.successful_payment.invoice_payload)
    user_id = message.from_user.id
    add_attempts(user_id, attempts_purchased)
    log_payment(user_id, attempts_purchased, message.successful_payment.total_amount)
    await message.answer(f"✅ Оплата прошла успешно! Вам добавлено {attempts_purchased} попыток.")

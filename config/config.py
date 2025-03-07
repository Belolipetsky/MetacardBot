import os
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")
PAYMENT_PROVIDER_TOKEN = os.getenv("PAYMENT_PROVIDER_TOKEN", "TEST_TOKEN")
BONUS_CHANNEL = os.getenv("BONUS_CHANNEL", "@your_channel_username")

# Опции для покупки попыток (цены в копейках)
PAYMENT_OPTIONS = {
    "Купить 1 карту": {"price": 89, "attempts": 1},
    "Купить 5 карт": {"price": 356, "attempts": 5},
    "Купить 10 карт": {"price": 699, "attempts": 10},
}

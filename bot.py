import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
import os
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")
if not API_TOKEN:
    raise Exception("API_TOKEN is not set in .env file")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

# Импорт роутеров (обработчиков)
from handlers import auth, card, payments, session, admin, start

dp.include_router(auth.router)
dp.include_router(start.router)  # Дополнительный обработчик для команды /home, если нужен
dp.include_router(card.router)
dp.include_router(payments.router)
dp.include_router(session.router)
dp.include_router(admin.router)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

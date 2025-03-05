import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers import start, course, card

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(start.router)
    dp.include_router(course.router)
    dp.include_router(card.router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

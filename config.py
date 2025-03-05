import os
from dotenv import load_dotenv

load_dotenv()  # Загружаем переменные окружения из файла .env

BOT_TOKEN = os.getenv("BOT_TOKEN")

# Список администраторов по юзернейму (без символа "@")
ADMINS = ["kvazarus"]

# Для отладки можно раскомментировать:
# print("BOT_TOKEN:", BOT_TOKEN)

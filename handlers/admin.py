from aiogram import Router, types
from aiogram.filters import Command
from config import ADMINS

router = Router()

# Глобальные переменные для хранения настроек
admin_data = {
    "greeting_text": "Привет, я Мария и помогаю людям решать проблемы через нейрографику.",
    "course_text": (
        "Курс по нейрографике:\n"
        "В этом курсе вы узнаете, как использовать нейрографику для решения жизненных проблем."
    ),
    "greeting_images": [],
    "course_images": []
}

def is_admin(username: str) -> bool:
    # Если username отсутствует, считаем, что пользователь не админ
    if not username:
        return False
    return username.lower() in [admin.lower() for admin in ADMINS]

@router.message(Command("admin"))
async def admin_panel(message: types.Message):
    username = message.from_user.username
    # Для отладки можно раскомментировать следующую строку:
    # print(f"Username: {username}")
    if not is_admin(username):
        return
    text = (
        "🔹 Админ-панель 🔹\n\n"
        "/setgreeting <текст> - изменить приветственное сообщение\n"
        "/setcourse <текст> - изменить описание курса\n"
        "/addgreetingpic - добавить картинку для приветствия (ответьте на фото)\n"
        "/addcoursepic - добавить картинку для курса (ответьте на фото)\n"
        "/viewadmin - показать текущие настройки\n"
    )
    await message.answer(text)

@router.message(Command("setgreeting"))
async def set_greeting(message: types.Message):
    username = message.from_user.username
    if not is_admin(username):
        return
    new_text = message.get_args()
    if not new_text:
        await message.answer("❌ Укажите новый текст приветствия.")
        return
    admin_data["greeting_text"] = new_text
    await message.answer("✅ Приветствие обновлено.")

@router.message(Command("setcourse"))
async def set_course(message: types.Message):
    username = message.from_user.username
    if not is_admin(username):
        return
    new_text = message.get_args()
    if not new_text:
        await message.answer("❌ Укажите новый текст курса.")
        return
    admin_data["course_text"] = new_text
    await message.answer("✅ Описание курса обновлено.")

@router.message(Command("addgreetingpic"))
async def add_greeting_pic(message: types.Message):
    username = message.from_user.username
    if not is_admin(username):
        return
    if message.reply_to_message and message.reply_to_message.photo:
        photo = message.reply_to_message.photo[-1]
        file_id = photo.file_id
        admin_data["greeting_images"].append(file_id)
        await message.answer("✅ Картинка для приветствия добавлена.")
    else:
        await message.answer("❌ Ответьте на сообщение с фото, чтобы добавить картинку.")

@router.message(Command("addcoursepic"))
async def add_course_pic(message: types.Message):
    username = message.from_user.username
    if not is_admin(username):
        return
    if message.reply_to_message and message.reply_to_message.photo:
        photo = message.reply_to_message.photo[-1]
        file_id = photo.file_id
        admin_data["course_images"].append(file_id)
        await message.answer("✅ Картинка для курса добавлена.")
    else:
        await message.answer("❌ Ответьте на сообщение с фото, чтобы добавить картинку.")

@router.message(Command("viewadmin"))
async def view_admin_data(message: types.Message):
    username = message.from_user.username
    if not is_admin(username):
        return
    text = (
        f"📌 **Текущие настройки:**\n\n"
        f"📜 **Приветствие:**\n{admin_data['greeting_text']}\n\n"
        f"🎓 **Описание курса:**\n{admin_data['course_text']}\n\n"
        f"🖼 **Картинки приветствия:** {len(admin_data['greeting_images'])} шт.\n"
        f"🖼 **Картинки курса:** {len(admin_data['course_images'])} шт."
    )
    await message.answer(text, parse_mode="Markdown")

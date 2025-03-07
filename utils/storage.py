# utils/storage.py

# Хранилище пользователей: ключ – user_id, значение – данные пользователя
users = {}

def register_user(user_id: int, username: str, name: str, phone: str):
    if user_id not in users:
        # При регистрации выдаём 1 бесплатную попытку
        users[user_id] = {"username": username, "name": name, "phone": phone, "attempts": 1}
    else:
        users[user_id].update({"username": username, "name": name, "phone": phone})

def get_attempts(user_id: int) -> int:
    return users.get(user_id, {}).get("attempts", 0)

def add_attempts(user_id: int, count: int):
    if user_id in users:
        users[user_id]["attempts"] += count
    else:
        users[user_id] = {"username": "", "name": "", "phone": "", "attempts": count}

def use_attempt(user_id: int) -> bool:
    if get_attempts(user_id) > 0:
        users[user_id]["attempts"] -= 1
        return True
    return False


# utils/spreadsheet.py

def log_registration(user_data: dict):
    # Заглушка для логирования регистрации в Google Таблицы
    print("LOG (registration):", user_data)

def log_payment(user_id: int, attempts_purchased: int, amount: int):
    # Заглушка для логирования платежей в Google Таблицы
    print(f"LOG (payment): user_id={user_id}, attempts={attempts_purchased}, amount={amount}")

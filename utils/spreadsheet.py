def log_registration(user_data: dict):
    # Здесь должна быть интеграция с Google Sheets
    print("LOG (registration):", user_data)

def log_payment(user_id: int, attempts: int, amount: int):
    # Заглушка для логирования оплаты в Google Таблицы
    print(f"LOG (payment): user_id={user_id}, attempts={attempts}, amount={amount}")

from datetime import datetime, timedelta

def add_days_to_current_date(days_to_add):
    # Отримуємо поточну дату (без часу)
    current_date = datetime.now().date()
    # Додаємо задану кількість днів
    new_date = current_date + timedelta(days=days_to_add)
    return new_date

# Приклад використання:
# Додамо 10 днів до сьогоднішньої дати
result = add_days_to_current_date(10)
print(f"Нова дата: {result}")


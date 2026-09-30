# 1 Завдання date
from datetime import datetime


def days_between_dates(date_str1: str, date_str2: str) -> int:
    # Перетворюємо рядки у формати дат
    date1 = datetime.strptime(date_str1, "%Y-%m-%d").date()
    date2 = datetime.strptime(date_str2, "%Y-%m-%d").date()

    # Знаходимо різницю та повертаємо кількість днів (абсолютне значення)
    return abs((date2 - date1).days)


# Приклад використання:
date_start = "2026-01-01"
date_end = "2026-09-30"

result = days_between_dates(date_start, date_end)
print(f"Кількість днів між датами: {result}")  # Виведе: 272


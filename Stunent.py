# 3 Завдання date
from datetime import datetime, timedelta


def get_next_monday():
    # Отримуємо дату від користувача через консоль
    date_str = input("Введіть дату у форматі РРРР-ММ-ДД (наприклад, 2026-09-30): ")

    try:
        # Перетворюємо рядок у об'єкт datetime
        given_date = datetime.strptime(date_str, "%Y-%m-%d").date()

        # weekday() повертає: 0 для понеділка, 1 для вівторка, ..., 6 для неділі
        current_weekday = given_date.weekday()

        # Обчислюємо, скільки днів залишилося до наступного понеділка
        # Якщо сьогодні понеділок, додасться 7 днів (наступний тиждень)
        days_ahead = 7 - current_weekday

        next_monday = given_date + timedelta(days=days_ahead)

        print(f"Задана дата: {given_date} ({given_date.strftime('%A')})")
        print(f"Дата наступного понеділка: {next_monday}")
        return next_monday

    except ValueError:
        print("Помилка! Будь ласка, введіть дату у правильному форматі РРРР-ММ-ДД.")


# Запуск функції
get_next_monday()


from datetime import datetime, timedelta


def calculate_arrival_time(start_date_str, duration_hours):
    """
    Обчислює дату й час прибуття.

    :param start_date_str: рядок з датою і часом початку (формат: "РРРР-ММ-ДД ГГ:ХХ")
    :param duration_hours: тривалість поїздки у годинах (може бути дробовим числом)
    :return: об'єкт datetime з часом прибуття
    """
    # Рядок формату, який відповідає "2026-10-07 19:30"
    date_format = "%Y-%m-%d %H:%M"

    # Перетворюємо рядок у об'єкт datetime
    start_datetime = datetime.strptime(start_date_str, date_format)

    # Додаємо тривалість поїздки
    arrival_datetime = start_datetime + timedelta(hours=duration_hours)

    return arrival_datetime


# --- Приклад використання ---
# Початок поїздки: 7 жовтня 2026 року о 14:30
start_time = "2026-10-07 14:30"
duration = 11.5  # 11 годин і 30 хвилин

arrival = calculate_arrival_time(start_time, duration)

# Виводимо результат у зручному для читання форматі
print(f"Час відправлення: {start_time}")
print(f"Тривалість: {duration} год.")
print(f"Час прибуття:    {arrival.strftime('%Y-%m-%d %H:%M')}")

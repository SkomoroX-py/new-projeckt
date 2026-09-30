from datetime import datetime

def seconds_between(time1: datetime, time2: datetime) -> float:
    # Віднімаємо менший час від більшого (або використовуємо abs, щоб уникнути від'ємних значень)
    delta = abs(time2 - time1)
    return delta.total_seconds()

# Приклад використання:
# Формат: Рік, Місяць, День, Година, Хвилина, Секунда
t1 = datetime(2026, 9, 30, 12, 0, 0)
t2 = datetime(2026, 9, 30, 14, 30, 15)

seconds = seconds_between(t1, t2)
print(f"Пройшло секунд: {seconds}")


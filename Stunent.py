# 5 Завдання date
from datetime import datetime
import time

def calculate_datetime_duration(start_time, end_time):
    """
    Calculates the difference between two datetime objects.
    Returns a timedelta object.
    """
    return end_time - start_time

# Приклад використання:
start = datetime.now()

# Код, виконання якого ми вимірюємо
time.sleep(1.5)

end = datetime.now()

duration = calculate_datetime_duration(start, end)
print(f"Програма виконувалася: {duration}")
print(f"Тривалість у секундах: {duration.total_seconds()} сек")


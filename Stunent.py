# 2 Завдання date
from datetime import datetime


def convert_date_format():
    # Отримуємо дані з консолі
    user_input = input("Введіть дату у форматі YYYY-MM-DD: ")

    try:
        # Перетворюємо рядок у об'єкт datetime (парсинг)
        date_obj = datetime.strptime(user_input, "%Y-%m-%d")

        # Форматуємо об'єкт datetime у потрібний рядок
        formatted_date = date_obj.strftime("%d/%m/%Y")

        # Виводимо результат
        print(f"Результат: {formatted_date}")

    except ValueError:
        # Обробка помилки, якщо формат неправильний або дата не існує
        print("Помилка! Будь ласка, перевірте правильність введення дати та формату (YYYY-MM-DD).")


# Запуск функції
if __name__ == "__main__":
    convert_date_format()

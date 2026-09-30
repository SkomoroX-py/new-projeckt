# 4 Завдання date
import calendar


def check_leap_year():
    try:
        # Зчитуємо рік з консолі та перетворюємо у ціле число
        year = int(input("Введіть рік: "))

        # Перевіряємо за допомогою вбудованого модуля calendar
        if calendar.isleap(year):
            print(f"Рік {year} є високосним.")
        else:
            print(f"Рік {year} не є високосним.")

    except ValueError:
        print("Будь ласка, введіть коректне ціле число для року.")


# Виклик функції
check_leap_year()


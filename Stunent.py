import math


def to_polar(x, y):
    """A function for converting Cartesian coordinates to polar coordinates."""
    # Обчислення радіуса (відстані від початку координат)
    r = math.sqrt(x ** 2 + y ** 2)

    # Обчислення кута в радіанах від -pi до pi
    theta = math.atan2(y, x)

    return r, theta


# Введення даних з консолі
try:
    x_coord = float(input("Введіть координату x: "))
    y_coord = float(input("Введіть координату y: "))

    # Виклик функції
    radius, angle = to_polar(x_coord, y_coord)

    # Виведення результату
    print(f"\nПолярні координати:")
    print(f"Радіус (r): {radius:.4f}")
    print(f"Кут (theta) в радіанах: {angle:.4f}")
    print(f"Кут в градусах: {math.degrees(angle):.2f}°")

except ValueError:
    print("Будь ласка, введіть коректні чисельні значення.")


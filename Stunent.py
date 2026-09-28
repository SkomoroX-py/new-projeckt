import math


# def calculate_factorial(n):
#     """Returns the factorial of the number n using math.factorial."""
#     return math.factorial(n)
#
#
# number = int(input("Enter a number to calculate the factorial. : "))
# result = calculate_factorial(number)
# print(f"Factorial of a number {number} equals {result}")
#
#
# def area_of_circle(radius):
#     """Calculates the area of a circle given the radius."""
#     if radius < 0:
#         raise ValueError("The radius cannot be negative.")
#     return math.pi * (radius ** 2)
#
#
# r = int(input("Enter the number : "))
# print(f"Area of a circle with a radius {r} equals {area_of_circle(r):.2f}")


def solve_quadratic(a, b, c):
    '''Checking whether the equation is quadratic'''
    if a == 0:
        if b != 0:
            return [-c / b]
        else:
            return []

    '''Calculation of the discriminant'''
    D = b**2 - 4 * a * c

    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        return [x1, x2]
    elif D == 0:
        x = -b / (2 * a)
        return [x]
    else:
        return []


try:
    print("Введіть коефіцієнти для рівняння ax^2 + bx + c = 0:")
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))

    '''Function call and result output'''
    roots = solve_quadratic(a, b, c)

    if len(roots) == 2:
        print(f"Рівняння має два корені: x1 = {roots[0]}, x2 = {roots[1]}")
    elif len(roots) == 1:
        print(f"Рівняння має один корінь: x = {roots[0]}")
    else:
        print("Рівняння не має дійсних коренів")

except ValueError:
    print("Будь ласка, вводьте лише числа!")


import math


def calculate_factorial(n):
    """Returns the factorial of the number n using math.factorial."""
    return math.factorial(n)


number = int(input("Enter a number to calculate the factorial. : "))
result = calculate_factorial(number)
print(f"Factorial of a number {number} equals {result}")


def area_of_circle(radius):
    """Calculates the area of a circle given the radius."""
    if radius < 0:
        raise ValueError("The radius cannot be negative.")
    return math.pi * (radius ** 2)


r = int(input("Enter the number : "))
print(f"Area of a circle with a radius {r} equals {area_of_circle(r):.2f}")

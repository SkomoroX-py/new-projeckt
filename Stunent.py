import math

def calculate_factorial(n):
    """Returns the factorial of the number n using math.factorial."""
    return math.factorial(n)


number = int(input("Enter a number to calculate the factorial. : "))
result = calculate_factorial(number)
print(f"Factorial of a number {number} equals {result}")
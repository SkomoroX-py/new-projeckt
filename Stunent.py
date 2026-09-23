import math

def area_of_circle(radius):
    """Calculates the area of a circle given the radius."""
    if radius < 0:
        raise ValueError("The radius cannot be negative.")
    return math.pi * (radius ** 2)


r = int(input("Enter the number : "))
print(f"Area of a circle with a radius {r} equals {area_of_circle(r):.2f}")


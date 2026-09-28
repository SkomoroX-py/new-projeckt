import math


def calculate_arc_length(radius: float, angle_radians: float) -> float:
    """A function for calculating the length of a circular arc."""
    return radius * angle_radians


if __name__ == "__main__":
    try:
        r = float(input("Enter the radius of the circle (r): "))
        alpha = float(input("Enter the angle in radians (alpha): "))

        if r < 0 or alpha < 0:
            print("Error: Radius and angle cannot be negative.")
        else:
            length = calculate_arc_length(r, alpha)
            print(f"Arc length of a circle: {length:.4f}")

    except ValueError:
        print("Error: Please enter numeric values.")

import math


def calculate_ellipse_area(a, b):
    """
    Calculates the area of an ellipse along the major and minor axes.
    :param a: Major semi-axis (float or int)
    :param b: Minor semi-axis (float or int)
    :return: Ellipse area (float)
    """
    if a <= 0 or b <= 0:
        raise ValueError("The lengths of the semi-axes must be greater than zero.")

    return math.pi * a * b


semi_major_axis = 5
semi_minor_axis = 3

area = calculate_ellipse_area(semi_major_axis, semi_minor_axis)
print(f"Area of an ellipse with semi-axes {semi_major_axis} and {semi_minor_axis} equals: {area:.4f}")


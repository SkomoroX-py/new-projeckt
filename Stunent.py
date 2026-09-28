import math


def count_log_iterations(n):
    """Calculates how many times the natural logarithm of a number needs to be taken."""
    if n < 1:
        return 0

    count = 0

    while n >= 1:
        n = math.log(n)
        count += 1

    return count


if __name__ == "__main__":
    try:
        user_input = float(input("Enter the number: "))


        if user_input <= 0:
            print("Error: Number must be greater than 0.")
        else:
            iterations = count_log_iterations(user_input)
            print(f"Number of logarithm iterations: {iterations}")

    except ValueError:
        print("Error: Please enter a valid number.")

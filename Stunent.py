class Fraction:
    # Static variable (class-level attribute) to store the count of objects
    _instance_count = 0

    def __init__(self, numerator: int, denominator: int):
        """
        Constructor to initialize the fraction object.
        """
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")

        self.numerator = numerator
        self.denominator = denominator

        # Increment the counter every time a new object is created
        Fraction._instance_count += 1

    @classmethod
    def get_instance_count(cls) -> int:
        """
        Static/Class method that returns the total number of created objects.
        """
        return cls._instance_count


# --- Example of usage ---
if __name__ == "__main__":
    # Check initial count (should be 0)
    print(f"Initial count: {Fraction.get_instance_count()}")

    # Create instances of the Fraction class
    f1 = Fraction(1, 2)
    f2 = Fraction(3, 4)
    f3 = Fraction(5, 6)
    #
    # Check count after creating 3 objects (should be 3)
    print(f"Count after creating objects: {Fraction.get_instance_count()}")


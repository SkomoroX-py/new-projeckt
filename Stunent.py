class TemperatureConverter:
    # Static variable to keep track of the total number of conversions
    _conversion_count = 0

    @classmethod
    def _increment_count(cls):
        """Internal class method to increment the conversion counter."""
        cls._conversion_count += 1

    @staticmethod
    def celsius_to_fahrenheit(celsius: float) -> float:
        """Converts temperature from Celsius to Fahrenheit."""
        TemperatureConverter._increment_count()
        return (celsius * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit: float) -> float:
        """Converts temperature from Fahrenheit to Celsius."""
        TemperatureConverter._increment_count()
        return (fahrenheit - 32) * 5/9

    @classmethod
    def get_conversion_count(cls) -> int:
        """Returns the total number of temperature conversions performed."""
        return cls._conversion_count


# --- Example of usage ---
if __name__ == "__main__":
    # Perform several conversions
    temp1 = TemperatureConverter.celsius_to_fahrenheit(25)
    print(f"25°C is equal to {temp1}°F")

    temp2 = TemperatureConverter.fahrenheit_to_celsius(98.6)
    print(f"98.6°F is equal to {temp2}°C")

    temp3 = TemperatureConverter.celsius_to_fahrenheit(0)
    print(f"0°C is equal to {temp3}°F")

    # Get the total count of conversions
    total_conversions = TemperatureConverter.get_conversion_count()
    print(f"Total conversions performed: {total_conversions}")


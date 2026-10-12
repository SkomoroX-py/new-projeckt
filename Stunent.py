class UnitConverter:
    """
    A utility class to convert measurements between Metric and Imperial systems
    using static methods. Includes length, weight, and volume conversions.
    """

    # --- Length Conversions ---

    @staticmethod
    def meters_to_feet(meters: float) -> float:
        """Convert meters to feet."""
        return meters * 3.28084

    @staticmethod
    def feet_to_meters(feet: float) -> float:
        """Convert feet to meters."""
        return feet / 3.28084

    @staticmethod
    def centimeters_to_inches(cm: float) -> float:
        """Convert centimeters to inches."""
        return cm * 0.393701

    @staticmethod
    def inches_to_centimeters(inches: float) -> float:
        """Convert inches to centimeters."""
        return inches / 0.393701

    @staticmethod
    def kilometers_to_miles(km: float) -> float:
        """Convert kilometers to miles."""
        return km * 0.621371

    @staticmethod
    def miles_to_kilometers(miles: float) -> float:
        """Convert miles to kilometers."""
        return miles / 0.621371

    # --- Weight Conversions ---

    @staticmethod
    def kilograms_to_pounds(kg: float) -> float:
        """Convert kilograms to pounds."""
        return kg * 2.20462

    @staticmethod
    def pounds_to_kilograms(lbs: float) -> float:
        """Convert pounds to kilograms."""
        return lbs / 2.20462

    # --- Volume Conversions ---

    @staticmethod
    def liters_to_gallons(liters: float) -> float:
        """Convert liters to US gallons."""
        return liters * 0.264172

    @staticmethod
    def gallons_to_liters(gallons: float) -> float:
        """Convert US gallons to liters."""
        return gallons / 0.264172


# --- Example Usage ---
if __name__ == "__main__":
    # Testing length conversions
    meters = 10
    feet = UnitConverter.meters_to_feet(meters)
    print(f"{meters} meters = {feet:.2f} feet")

    inches = 12
    cm = UnitConverter.inches_to_centimeters(inches)
    print(f"{inches} inches = {cm:.2f} cm")

    # Testing weight conversions
    kg = 75
    lbs = UnitConverter.kilograms_to_pounds(kg)
    print(f"{kg} kg = {lbs:.2f} lbs")


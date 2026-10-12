class Car:
    def __init__(self, model_name: str, year: int, manufacturer: str, engine_capacity: float, color: str, price: float):
        """Initialize the Car object with its attributes."""
        self.model_name = model_name
        self.year = year
        self.manufacturer = manufacturer
        self.engine_capacity = engine_capacity
        self.color = color
        self.price = price

    def input_data(self):
        """Allow user to manually input or update the car details."""
        print("\n--- Enter Car Details ---")
        self.model_name = input("Enter model name: ")
        self.year = int(input("Enter production year: "))
        self.manufacturer = input("Enter manufacturer: ")
        self.engine_capacity = float(input("Enter engine capacity (in liters): "))
        self.color = input("Enter car color: ")
        self.price = float(input("Enter car price ($): "))

    def display_data(self):
        """Display the car details in a readable format."""
        print("\n--- Car Specification ---")
        print(f"Manufacturer:    {self.manufacturer}")
        print(f"Model Name:      {self.model_name}")
        print(f"Production Year: {self.year}")
        print(f"Engine Capacity: {self.engine_capacity}L")
        print(f"Color:           {self.color}")
        print(f"Price:           ${self.price:,.2f}")

    def apply_discount(self, percentage: float):
        """Reduce the price of the car by a given percentage."""
        if 0 < percentage < 100:
            discount_amount = self.price * (percentage / 100)
            self.price -= discount_amount
            print(f"\n[Success] Applied a {percentage}% discount. New price: ${self.price:,.2f}")
        else:
            print("\n[Error] Invalid discount percentage. Must be between 0 and 100.")

    def change_color(self, new_color: str):
        """Repaint the car to a new color."""
        print(f"\n[Repaint] Changing color from {self.color} to {new_color}.")
        self.color = new_color


# --- Example Usage ---
if __name__ == "__main__":
    # Creating an initial car object
    my_car = Car("Model S", 2023, "Tesla", 0.0, "White", 75000.0)

    # Displaying initial data
    my_car.display_data()

    # Changing the car color
    my_car.change_color("Midnight Blue")

    # Applying a 10% discount
    my_car.apply_discount(10)

    # Displaying updated data
    my_car.display_data()

    # Let the user input new values manually
    my_car.input_data()
    my_car.display_data()


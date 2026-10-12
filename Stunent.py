from datetime import datetime


class Stadium:
    def __init__(self, name: str = "", opening_date: str = "01.01.2000", country: str = "", city: str = "",
                 capacity: int = 0):
        # Initialize the attributes of the stadium
        self.name = name
        self.opening_date = opening_date
        self.country = country
        self.city = city
        self.capacity = capacity

    def input_data(self):
        # Method to input stadium details from the console
        print("\n--- Enter Stadium Data ---")
        self.name = input("Enter stadium name: ")
        self.opening_date = input("Enter opening date (e.g., DD.MM.YYYY): ")
        self.country = input("Enter country: ")
        self.city = input("Enter city: ")

        while True:
            try:
                self.capacity = int(input("Enter capacity (number of seats): "))
                if self.capacity >= 0:
                    break
                print("Capacity cannot be negative. Try again.")
            except ValueError:
                print("Invalid input. Please enter a valid integer for capacity.")

    def display_data(self):
        # Method to display stadium details to the console
        print("\n--- Stadium Information ---")
        print(f"Stadium Name: {self.name}")
        print(f"Opening Date: {self.opening_date}")
        print(f"Location:     {self.city}, {self.country}")
        print(f"Capacity:     {self.capacity:,} seats")

    # Getters and Setters for operational flexibility
    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str):
        self.name = name

    def get_capacity(self) -> int:
        return self.capacity

    def set_capacity(self, capacity: int):
        if capacity >= 0:
            self.capacity = capacity
        else:
            print("Error: Capacity cannot be negative.")


# Example usage of the Stadium class
if __name__ == "__main__":
    # Creating an instance with default/initial values
    stadium1 = Stadium("Olimpiyskiy", "12.08.1923", "Ukraine", "Kyiv", 70050)
    stadium1.display_data()

    # Creating an empty instance and filling it via user input
    stadium2 = Stadium()
    stadium2.input_data()
    stadium2.display_data()

    # Updating capacity using the setter method
    print("\nUpdating the capacity of the second stadium...")
    stadium2.set_capacity(45000)
    print(f"New capacity of {stadium2.get_name()}: {stadium2.get_capacity():,} seats")


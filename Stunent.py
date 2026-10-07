class City:
    def __init__(self, name=None, region=None, country=None, population=0, postal_code=None, phone_code=None):
        self.name = name
        self.region = region
        self.country = country
        self.population = population
        self.postal_code = postal_code
        self.phone_code = phone_code

    def input_data(self):
        """Entering city data from the keyboard"""
        print("--- Введення даних про місто ---")
        self.name = input("Введіть назву міста: ")
        self.region = input("Введіть назву регіону/області: ")
        self.country = input("Введіть назву країни: ")
        while True:
            try:
                self.population = int(input("Введіть кількість жителів: "))
                break
            except ValueError:
                print("Помилка! Кількість жителів має бути цілим числом.")
        self.postal_code = input("Введіть поштовий індекс: ")
        self.phone_code = input("Введіть телефонний код: ")

    def display_data(self):
        """Displaying city data on the screen"""
        print(f"\n--- Інформація про місто: {self.name} ---")
        print(f"Регіон:           {self.region}")
        print(f"Країна:           {self.country}")
        print(f"Кількість населення: {self.population:,} чол.")
        print(f"Поштовий індекс:  {self.postal_code}")
        print(f"Телефонний код:   {self.phone_code}")

    # Getters and setters for individual field access (other operations)
    def update_population(self, new_population):
        """Population count update"""
        if new_population >= 0:
            self.population = new_population
        else:
            print("Кількість населення не може бути від'ємною!")

    def get_city_location(self):
        """A method that returns the full name of the location."""
        return f"{self.name}, {self.region}, {self.country}"


# --- Demonstration of the program's operation using Prague as an example. ---

# Creating an object via the constructor with initial data for Prague.
prague = City(
    name="Прага",
    region="Головне місто Прага",
    country="Чехія",
    population=1384732,
    postal_code="100 00 - 199 00",
    phone_code="+420"
)

# Data output
prague.display_data()

# Demonstration of additional methods
print(f"\nПовна локація: {prague.get_city_location()}")

# Population count update
prague.update_population(1400000)
print(f"Оновлене населення: {prague.population:,} чол.")


'''Creating new city data via keyboard input.'''
custom_city = City()
custom_city.input_data()
custom_city.display_data()


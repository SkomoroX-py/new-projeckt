from datetime import datetime


class Person:
    def __init__(self, full_name: str = "", birth_date: str = "01.01.2000",
                 phone: str = "", city: str = "", country: str = "", address: str = ""):
        """Initialization of a Person class object"""
        self.full_name = full_name
        self.birth_date = birth_date
        self.phone = phone
        self.city = city
        self.country = country
        self.address = address

    def input_data(self):
        """Method for the user to enter all data via the keyboard"""
        print("\n--- Введення даних людини ---")
        self.full_name = input("Введіть ПІБ: ")
        self.birth_date = input("Введіть дату народження (ДД.ММ.РРРР): ")
        self.phone = input("Введіть контактний телефон: ")
        self.city = input("Введіть місто: ")
        self.country = input("Введіть країну: ")
        self.address = input("Введіть домашню адресу: ")

    def display_data(self):
        """Method for outputting data to the console"""
        print("\n=== Інформація про людину ===")
        print(f"ПІБ:               {self.full_name}")
        print(f"Дата народження:   {self.birth_date}")
        print(f"Вік:               {self.get_age()} років")
        print(f"Телефон:           {self.phone}")
        print(f"Країна:            {self.country}")
        print(f"Місто:             {self.city}")
        print(f"Домашня адреса:    {self.address}")
        print("=============================")

    def get_age(self) -> int:
        """An additional useful method: calculating current age based on date of birth."""
        try:
            birth = datetime.strptime(self.birth_date, "%d.%m.%Y")
            today = datetime.today()
            age = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))
            return age
        except ValueError:
            return 0  # Якщо формат дати неправильний

    # Getters and setters (methods for retrieving and modifying individual fields)
    def set_phone(self, new_phone: str):
        self.phone = new_phone

    def get_phone(self) -> str:
        return self.phone

    def set_address(self, new_city: str, new_country: str, new_address: str):
        self.city = new_city
        self.country = new_country
        self.address = new_address


#
if __name__ == "__main__":
    # 1. Creating an object with initial data
    person1 = Person(
        full_name="Шевченко Тарас Григорович",
        birth_date="09.03.1814",
        phone="+380501234567",
        city="Моринці",
        country="Україна",
        address="вул. Центральна, 1"
    )

    # Output of initial data
    person1.display_data()

    # 2. Modifying specific data via methods
    person1.set_phone("+380679876543")
    print(f"\n[Оновлено] Новий телефон: {person1.get_phone()}")

    # 3. Creating a new object and user data entry
    person2 = Person()
    person2.input_data()
    person2.display_data()

class Book:
    def __init__(self, title: str = "", year: int = 0, publisher: str = "", genre: str = "", author: str = "",
                 price: float = 0.0):
        # Initialize the Book object with default values
        self.title = title
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def input_data(self):
        # Get book details from user input
        print("\n--- Enter Book Details ---")
        self.title = input("Enter title: ")

        while True:
            try:
                self.year = int(input("Enter publication year: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid year (integer).")

        self.publisher = input("Enter publisher: ")
        self.genre = input("Enter genre: ")
        self.author = input("Enter author: ")

        while True:
            try:
                self.price = float(input("Enter price: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid price (number).")

    def display_data(self):
        # Print the book details to the console
        print("\n--- Book Information ---")
        print(f"Title:         {self.title}")
        print(f"Author:        {self.author}")
        print(f"Genre:         {self.genre}")
        print(f"Publisher:     {self.publisher}")
        print(f"Year:          {self.year}")
        print(f"Price:         {self.price:.2f} UAH")

    def apply_discount(self, percentage: float):
        # Reduce the price of the book by a given percentage
        if 0 < percentage <= 100:
            self.price -= self.price * (percentage / 100)
            print(f"\nSuccess: Applied a {percentage}% discount. New price: {self.price:.2f} UAH")
        else:
            print("\nError: Invalid discount percentage. Must be between 0 and 100.")

    def get_book_age(self, current_year: int = 2026) -> int:
        # Calculate and return how many years have passed since publication
        return current_year - self.year


# --- Example of usage ---
if __name__ == "__main__":
    # Option 1: Create a book object and fill it using user input
    my_book = Book()
    my_book.input_data()
    my_book.display_data()

    # Option 2: Apply a discount
    my_book.apply_discount(15)  # 15% off
    my_book.display_data()

    # Option 3: Calculate the age of the book
    age = my_book.get_book_age()
    print(f"\nThe book was published {age} years ago.")


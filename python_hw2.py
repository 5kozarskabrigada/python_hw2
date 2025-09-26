# Assignment 1
class Car:

    def __init__(self, model_name, year, manufacturer, engine_volume, color, price):

        self.model_name = model_name
        self.year = year
        self.manufacturer = manufacturer
        self.engine_volume = engine_volume
        self.color = color
        self.price = price

    def display_info(self):

        print("ABout Car")
        print(f"Model: {self.model_name}")
        print(f"Year: {self.year}")
        print(f"Manufacturer: {self.manufacturer}")
        print(f"Engine Volume: {self.engine_volume} L")
        print(f"Color: {self.color}")
        print(f"Price: ${self.price}")
        print("_________________________")

    def set_price(self, new_price):

        if new_price > 0:
            self.price = new_price
            print(f"Price for {self.model_name} updated to ${new_price}")

        else:
            print("Price must be above 0")

    def set_color(self, new_color):
        self.color = new_color
        print(f"Color for {self.model_name} updated to {new_color}")

    def get_age(self, current_year):
        return current_year - self.year



car1 = Car("Toyota Camry", 2020, "Toyota", 2.5, "White", 25000)
car1.display_info()
car1.set_price(26500)
car1.set_color("Black")
car1.display_info()

print(f"Age of the car (in 2025): {car1.get_age(2025)} years\n")



class Book:

    def __init__(self, title, publication_year, publisher, genre, author, price):

        self.title = title
        self.publication_year = publication_year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def display_info(self):

        print("About Book")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Publication Year: {self.publication_year}")
        print(f"Publisher: {self.publisher}")
        print(f"Genre: {self.genre}")
        print(f"Price: ${self.price}")
        print("_________________________")


    def set_price(self, new_price):

        if new_price > 0:
            self.price = new_price
            print(f"Price for book '{self.title}' updated to ${new_price}")

        else:
            print("Price must be positive.")

    def set_genre(self, new_genre):
        self.genre = new_genre

        print(f"Genre for book '{self.title}' updated to '{new_genre}'")

    def get_full_description(self):

        return f"'{self.title}' by {self.author} ({self.publication_year}, {self.publisher}), Genre: {self.genre}, Price: ${self.price}"



book1 = Book("1984", 1949, "Secker & Warburg", "Dystopian", "George Orwell", 12.99)
book1.display_info()

book1.set_price(14.50)
book1.set_genre("Classic")
print(f"Full book description: {book1.get_full_description()}\n")


class Stadium:

    def __init__(self, name, opening_date, country, city, capacity):

        self.name = name
        self.opening_date = opening_date
        self.country = country
        self.city = city
        self.capacity = capacity

    def display_info(self):

        print("About Stadium")
        print(f"Name: {self.name}")
        print(f"Opening Date: {self.opening_date}")
        print(f"Country: {self.country}")
        print(f"City: {self.city}")
        print(f"Capacity: {self.capacity} people")
        print("__________________________")


    def set_capacity(self, new_capacity):

        if new_capacity > 0:
            self.capacity = new_capacity
            print(f"Capacity of stadium '{self.name}' updated to {new_capacity} people")
        else:
            print("Capacity must be above 0.")

    def set_location(self, new_city, new_country):
        self.city = new_city
        self.country = new_country
        print(f"Location of stadium '{self.name}' updated to {new_city}, {new_country}")

    def get_location(self):

        return f"{self.city}, {self.country}"


stadium1 = Stadium("Stadium 1", "1956-07-31", "Russia", "Moscow", 81000)
stadium1.display_info()

stadium1.set_capacity(78000)
stadium1.set_location("Saint Petersburg", "Russia")
print(f"Current stadium location: {stadium1.get_location()}")

stadium1.display_info()
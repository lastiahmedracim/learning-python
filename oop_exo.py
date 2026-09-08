# class Dog:
#     def __init__(self, name):
#         self.name = name

#     def bark(self):
#         print("Woof!")

# dog = Dog("Rex")

# print(dog.name)
# dog.bark()

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def introduce(self):
#         print(f'Hi, my name is {self.name} and I am {self.age} years old.')

# person = Person("Alex", 20)
# person.introduce()

# class BankAccount:
#     def __init__(self, owner):
#         self.owner = owner
#         self.balance = 0

#     def deposit(self, amount):
#         self.balance += amount

#     def get_balance(self):
#         return self.balance

# account = BankAccount("Alex")
# account.deposit(100)

# print(account.get_balance())

# class BankAccount:
#     def __init__(self, owner):
#         self.owner = owner
#         self.balance = 0

#     def deposit(self, amount):
#         self.balance += amount

#     def withdraw(self, amount):
#         if self.balance >= amount:
#             self.balance -= amount
#             return True
#         return False

#     def get_balance(self):
#         return self.balance

# account = BankAccount("Alex")

# account.deposit(100)

# print(account.withdraw(40))
# print(account.get_balance())

# print(account.withdraw(100))
# print(account.get_balance())

# class ShoppingCart:
#     def __init__(self):
#         self.items = []

#     def add_item(self, item):
#         self.items.append(item)

#     def remove_item(self, item):
#         self.items.remove(item)

#     def show_items(self):
#         print(self.items)

# cart = ShoppingCart()

# cart.add_item("Apple")
# cart.add_item("Banana")

# cart.show_items()

# cart.remove_item("Apple")

# cart.show_items()

# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.grade = []

#     def add_grade(self, grade):
#         self.grade.append(grade)

#     def get_average(self):
#         return sum(self.grade) / len(self.grade)

# student = Student("Alex")

# student.add_grade(10)
# student.add_grade(15)
# student.add_grade(20)

# print(student.get_average())

# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#         self.available = True

#     def borrow(self):
#         if self.available:
#             self.available = False
#             return True
#         return False

#     def return_book(self):
#         self.available = True


# book = Book("1984", "George Orwell")

# print(book.borrow())
# print(book.available)

# print(book.borrow())

# book.return_book()

# print(book.available)

# class Bank:
#     def __init__(self):
#         self.accounts = []

#     def add_account(self, account):
#         self.accounts.append(account)

#     def total_money(self):
#         total = 0

#         for account in self.accounts:
#             total += account.get_balance()

#         return total


# bank = Bank()

# account1 = BankAccount("Alex")
# account1.deposit(100)

# account2 = BankAccount("Sam")
# account2.deposit(200)

# bank.add_account(account1)
# bank.add_account(account2)

# print(bank.total_money())

# class Playlist:
#     def __init__(self, name):
#         self.name = name
#         self.songs = []

#     def add_song(self, song):
#         self.songs.append(song)

#     def remove_song(self, song):
#         self.songs.remove(song)

#     def song_count(self):
#         print(len(self.songs))

# playlist = Playlist("My Music")

# playlist.add_song("Song A")
# playlist.add_song("Song B")
# playlist.add_song("Song C")

# print(playlist.song_count())

# playlist.remove_song("Song B")

# print(playlist.song_count())

# class Category:
#     def __init__(self, name):
#         self.name = name
#         self.ledger = []

#     def deposit(self, amount, description=""):
#         self.ledger.append({"amount": amount, "description": description})

#     def withdraw(self, amount, description=""):
#         if self.get_balance() >= amount:
#             self.ledger.append({"amount": -amount, "description": description})
#             return True
#         return False

#     def get_balance(self):
#         return sum(item["amount"] for item in self.ledger)

#     def transfer(self, amount, category):
#         if self.withdraw(amount, f"Transfer to {category.name}"):
#             category.deposit(amount, f"Transfer from {self.name}")
#             return True
#         return False


# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height

#     def perimeter(self):
#         return 2 * (self.width + self.height)

#     def is_square(self):
#         return self.width == self.height

#     def change_width(self, width):
#         self.width = width

#     def change_height(self, height):
#         self.height = height

        

# rectangle = Rectangle(5, 10)

# print(rectangle.area())
# print(rectangle.perimeter())
# print(rectangle.is_square())

# rectangle.change_width(7)
# rectangle.change_height(7)

# print(rectangle.area())
# print(rectangle.perimeter())
# print(rectangle.is_square())

# class BankAccount:
#     def __init__(self, name):
#         self.name = name
#         self.balance = 0

#     def deposit(self, amount):
#         self.balance += amount
#         return True

#     def withdraw(self, amount):
#         if self.balance >= amount:
#             self.balance -= amount
#             return True
#         return False

#     def get_balance(self):
#         return self.balance

#     def display_info(self):
#         print(f"Account holder: {self.name}")
#         print(f"Balance: {self.balance}")
    

# account = BankAccount("Ali")

# print(account.get_balance())

# print(account.deposit(500))
# print(account.get_balance())

# print(account.withdraw(150))
# print(account.get_balance())

# print(account.withdraw(500))

# account.display_info()

# class ShoppingCart:
#     def __init__(self):
#         self.items = []

#     def add_item(self, name, price):
#         self.items.append({
#             "name": name,
#             "price": price
#         })

#     def remove_item(self, name):
#         for item in self.items:
#             if item["name"] == name:
#                 self.items.remove(item)
#                 return True
#         return False

#     def total_price(self):
#         return sum(item["price"] for item in self.items)

#     def item_count(self):
#         return len(self.items)

#     def clear(self):
#         self.items.clear()

# cart = ShoppingCart()

# cart.add_item("Laptop", 1000)
# cart.add_item("Mouse", 50)
# cart.add_item("Keyboard", 100)

# print(cart.item_count())
# print(cart.total_price())

# cart.remove_item("Mouse")

# print(cart.item_count())
# print(cart.total_price())

# cart.clear()

# print(cart.item_count())
# print(cart.total_price())


# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.grade = []

#     def add_grade(self, grade):
#         self.grade.append(
#             {
#                 'grade' : grade
#             }
#         )

#     def average_grade(self):
#         return sum(ng['grade'] for ng in self.grade) / len(self.grade)

#     def highest_grade(self):
#         return max(ng['grade'] for ng in self.grade)

#     def lowest_grade(self):
#         return min(ng['grade'] for ng in self.grade)
    
#     def has_passed(self):
#         return self.average_grade() >= 50

# student = Student("Yacine", 20)

# student.add_grade(70)
# student.add_grade(80)
# student.add_grade(60)
# student.add_grade(40)

# print(student.average_grade())
# print(student.highest_grade())
# print(student.lowest_grade())
# print(student.has_passed())

# class Library:
#     def __init__(self):
#         self.books = []

#     def add_book(self, title, author):
#         self.books.append({
#             "title": title,
#             "author": author
#         })

#     def remove_book(self, title):
#         for book in self.books:
#             if book["title"] == title:
#                 self.books.remove(book)
#                 return True
#         return False

#     def has_book(self, title):
#         for book in self.books:
#             if book["title"] == title:
#                 return True
#         return False

#     def book_count(self):
#         return len(self.books)

#     def get_titles(self):
#         return [book["title"] for book in self.books]


# library = Library()

# library.add_book("1984", "George Orwell")
# library.add_book("The Hobbit", "J.R.R. Tolkien")
# library.add_book("Dune", "Frank Herbert")

# print(library.book_count())

# print(library.has_book("1984"))
# print(library.has_book("Harry Potter"))

# library.remove_book("The Hobbit")

# print(library.book_count())
# print(library.get_titles())

# class Employee:
#     def __init__(self, name, salary, department):
#         self.name = name
#         self.salary = salary
#         self.department = department

#     def give_raise(self, percentage):
#         self.salary += self.salary * (percentage / 100)

#     def yearly_salary(self):
#         return self.salary * 12

#     def is_high_earner(self):
#         return self.salary >= 5000

#     def display_info(self):
#         print(f"Name: {self.name}")
#         print(f"Salary: {self.salary}")
#         print(f"Department: {self.department}")

# employee = Employee("Sara", 4500, "IT")

# print(employee.yearly_salary())
# print(employee.is_high_earner())

# employee.give_raise(10)

# print(employee.salary)
# print(employee.yearly_salary())
# print(employee.is_high_earner())

# employee.display_info()


# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#         self.fuel = 0

#     def add_fuel(self, amount):
#         self.fuel += amount

#     def get_fuel(self):
#         return self.fuel

#     def drive(self, driven):
#         consum = driven / 10
#         if self.fuel > consum:
#             self.fuel -= consum
#             return True
#         return False

#     def display_info(self):
#         print(self.brand)
#         print(self.model)
#         print(self.fuel)

# car = Car("Toyota", "Corolla")

# print(car.get_fuel())

# car.add_fuel(20)

# print(car.get_fuel())

# print(car.drive(100))
# print(car.get_fuel())

# print(car.drive(150))
# print(car.get_fuel())

# car.display_info()

# from datetime import datetime
# now = datetime.now()
# year = now.strftime("%Y")
# year = int(year)

# class Movie:
#     def __init__(self, title, director, relase_year, rating):
#         self.title = title
#         self.director = director
#         self.relase_year = relase_year
#         self.rating = rating

#     def change_rating(self, rate):
#         self.rating = rate

#     def is_good(self):
#         if self.rating >= 8.5:
#             return True
#         return False

#     def age(self):
#         return year - self.relase_year

#     def display_info(self):
#         print(self.title)
#         print(self.director)
#         print(self.relase_year)
#         print(self.rating)

# movie = Movie("Inception", "Christopher Nolan", 2010, 8.8)

# print(movie.is_good())
# print(movie.age())

# movie.change_rating(6.5)

# print(movie.is_good())

# movie.display_info()


# class Phone:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#         self.battery = 100

#     def call(self):
#         if self.battery >= 10:
#             self.battery -= 10
#             return True
#         return False

#     def charge(self, amount):
#         self.battery += amount

#         if self.battery > 100:
#             self.battery = 100

#     def get_battery(self):
#         return self.battery

#     def display_info(self):
#         print(f"Brand: {self.brand}")
#         print(f"Model: {self.model}")
#         print(f"Battery: {self.battery}")


# phone = Phone("Samsung", "Galaxy S25")

# print(phone.get_battery())

# print(phone.call())
# print(phone.get_battery())

# phone.charge(5)

# print(phone.get_battery())

# phone.charge(50)

# print(phone.get_battery())

# phone.display_info()

# class Restaurant:
#     def __init__(self, name, cuisine):
#         self.name = name
#         self.cuisine = cuisine
#         self.dishes = []

#     def add_dish(self, name, price):
#         self.dishes.append({
#             "name": name,
#             "price": price
#         })

#     def remove_dish(self, name):
#         for dish in self.dishes:
#             if dish["name"] == name:
#                 self.dishes.remove(dish)
#                 return True
#         return False

#     def dish_count(self):
#         return len(self.dishes)

#     def total_price(self):
#         return sum(dish["price"] for dish in self.dishes)

#     def most_expensive(self):
#         if not self.dishes:
#             return None

#         return max(self.dishes, key=lambda dish: dish["price"])["name"]

#     def display_info(self):
#         print(f"Restaurant: {self.name}")
#         print(f"Cuisine: {self.cuisine}")
#         print(f"Dishes: {self.dish_count()}")


# restaurant = Restaurant("Le Gourmet", "French")

# restaurant.add_dish("Steak", 25)
# restaurant.add_dish("Pasta", 15)
# restaurant.add_dish("Salmon", 30)

# print(restaurant.dish_count())
# print(restaurant.total_price())
# print(restaurant.most_expensive())

# restaurant.remove_dish("Pasta")

# print(restaurant.dish_count())
# print(restaurant.total_price())

# restaurant.display_info()

# class Team:
#     def __init__(self, name):
#         self.name = name
#         self.players = []

#     def add_player(self, name, score):
#         self.players.append((name, score))

#     def remove_player(self, name):
#         for player in self.players:
#             if player[0] == name:
#                 self.players.remove(player)
#                 break

#     def player_count(self):
#         return len(self.players)

#     def has_player(self, name):
#         for player in self.players:
#             if player[0] == name:
#                 return True
#         return False

#     def total_score(self):
#         total = 0

#         for player in self.players:
#             total += player[1]

#         return total

#     def top_player(self):
#         top = self.players[0]

#         for player in self.players:
#             if player[1] > top[1]:
#                 top = player

#         return top[0]


# team = Team("Tigers")

# team.add_player("Ali", 10)
# team.add_player("Yacine", 25)
# team.add_player("Karim", 15)

# print(team.player_count())
# print(team.has_player("Yacine"))
# print(team.has_player("Omar"))

# print(team.total_score())
# print(team.top_player())

# team.remove_player("Karim")

# print(team.player_count())
# print(team.total_score())

# class Store:
#     def __init__(self, name):
#         self.name = name
#         self.products = []

#     def add_product(self, name, price, quantity):
#         self.products.append({
#             "name": name,
#             "price": price,
#             "quantity": quantity
#         })

#     def remove_product(self, name):
#         for product in self.products:
#             if product["name"] == name:
#                 self.products.remove(product)
#                 return True
#         return False

#     def product_count(self):
#         return len(self.products)

#     def total_value(self):
#         return sum(
#             product["price"] * product["quantity"]
#             for product in self.products
#         )

#     def find_product(self, name):
#         for product in self.products:
#             if product["name"] == name:
#                 return True
#         return False

#     def most_expensive(self):
#         if not self.products:
#             return None

#         return max(
#             self.products,
#             key=lambda product: product["price"]
#         )["name"]

#     def sell_product(self, name, quantity):
#         for product in self.products:
#             if product["name"] == name:
#                 if product["quantity"] >= quantity:
#                     product["quantity"] -= quantity
#                     return True
#                 return False
#         return False


# store = Store("Tech Store")

# store.add_product("Laptop", 1000, 3)
# store.add_product("Mouse", 50, 10)
# store.add_product("Keyboard", 100, 5)

# print(store.product_count())
# print(store.find_product("Mouse"))
# print(store.find_product("Phone"))

# print(store.total_value())
# print(store.most_expensive())

# print(store.sell_product("Mouse", 3))
# print(store.total_value())

# print(store.sell_product("Laptop", 5))
# print(store.total_value())

# store.remove_product("Keyboard")

# print(store.product_count())
# print(store.total_value())


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, name, price, quantity):
        self.products.append({
            "name": name,
            "price": price,
            "quantity": quantity
        })

    def remove_product(self, name):
        for product in self.products:
            if product["name"] == name:
                self.products.remove(product)
                return True
        return False

    def find_product(self, name):
        for product in self.products:
            if product["name"] == name:
                return product
        return None

    def total_value(self):
        total = 0

        for product in self.products:
            total += product["price"] * product["quantity"]

        return total

    def sell_product(self, name, quantity):
        product = self.find_product(name)

        if product and product["quantity"] >= quantity:
            product["quantity"] -= quantity
            return True

        return False

    def restock(self, name, quantity):
        product = self.find_product(name)

        if product:
            product["quantity"] += quantity
            return True

        return False

    def low_stock(self):
        return [
            product["name"]
            for product in self.products
            if product["quantity"] < 5
        ]

    def most_valuable(self):
        if not self.products:
            return None

        most = self.products[0]

        for product in self.products:
            if product["price"] * product["quantity"] > most["price"] * most["quantity"]:
                most = product

        return most["name"]


inventory = Inventory()

inventory.add_product("Laptop", 1000, 3)
inventory.add_product("Mouse", 50, 10)
inventory.add_product("Keyboard", 100, 4)
inventory.add_product("Monitor", 300, 6)

print(inventory.total_value())

print(inventory.find_product("Mouse"))
print(inventory.find_product("Phone"))

print(inventory.sell_product("Mouse", 4))
print(inventory.sell_product("Laptop", 5))

inventory.restock("Laptop", 4)

print(inventory.low_stock())
print(inventory.most_valuable())

print(inventory.total_value())

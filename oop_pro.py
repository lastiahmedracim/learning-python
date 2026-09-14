# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def show_info(self):
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age}")


# class Employee(Person):
#     def __init__(self, name, age, job):
#         super().__init__(name, age)
#         self.job = job

#     def work(self):
#         print(f"{self.name} is working as a {self.job}.")


# class Manager(Person):
#     def __init__(self, name, age, department):
#         super().__init__(name, age)
#         self.department = department

#     def manage(self):
#         print(f"{self.name} manages the {self.department} department.")


# # Create objects
# employee = Employee("Ahmed", 25, "Python Developer")
# manager = Manager("Ali", 35, "IT")


# # Employee
# employee.show_info()
# employee.work()

# print()

# # Manager
# manager.show_info()
# manager.manage()

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         print("Animal makes a sound.")


# class Dog(Animal):
#     def speak(self):
#         print(f"{self.name} says: Woof!")


# class Cat(Animal):
#     def speak(self):
#         print(f"{self.name} says: Meow!")


# class Cow(Animal):
#     def speak(self):
#         print(f"{self.name} says: Moo!")


# # Create objects
# animal = Animal("Something")
# dog = Dog("Rex")
# cat = Cat("Luna")
# cow = Cow("Bessie")


# # Call speak()
# animal.speak()
# dog.speak()
# cat.speak()
# cow.speak()


# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         print("Animal makes a sound.")


# class Dog(Animal):
#     def speak(self):
#         print(f"{self.name} says: Woof!")


# class Cat(Animal):
#     def speak(self):
#         print(f"{self.name} says: Meow!")


# class Cow(Animal):
#     def speak(self):
#         print(f"{self.name} says: Moo!")


# def make_animals_speak(animals):
#     for animal in animals:
#         animal.speak()


# animals = [
#     Dog("Rex"),
#     Cat("Luna"),
#     Cow("Bessie")
# ]

# make_animals_speak(animals)



# class CPU:
#     def __init__(self, brand, cores):
#         self.brand = brand
#         self.cores = cores

#     def process(self):
#         print(f"{self.brand} CPU with {self.cores} cores is processing.")


# class RAM:
#     def __init__(self, capacity):
#         self.capacity = capacity

#     def show_info(self):
#         print(f"RAM: {self.capacity} GB")


# class Storage:
#     def __init__(self, capacity, storage_type):
#         self.capacity = capacity
#         self.storage_type = storage_type

#     def show_info(self):
#         print(f"Storage: {self.capacity} GB {self.storage_type}")


# class Computer:
#     def __init__(self, brand, cpu, ram, storage):
#         self.brand = brand
#         self.cpu = cpu
#         self.ram = ram
#         self.storage = storage

#     def start(self):
#         print(f"Computer {self.brand} is starting...")
#         self.cpu.process()
#         self.ram.show_info()
#         self.storage.show_info()

#     def show_info(self):
#         print(f"Computer: {self.brand}")
#         print(f"CPU: {self.cpu.brand}, {self.cpu.cores} cores")
#         print(f"RAM: {self.ram.capacity} GB")
#         print(
#             f"Storage: {self.storage.capacity} GB "
#             f"{self.storage.storage_type}"
#         )


# # Create components
# cpu = CPU("Intel", 8)
# ram = RAM(16)
# storage = Storage(512, "SSD")

# # Create computer
# computer = Computer("HP", cpu, ram, storage)

# # Use computer
# computer.start()

# print()

# computer.show_info()



# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#     def show_info(self):
#         print(f"{self.name} - ${self.price}")


# class Cart:
#     def __init__(self):
#         self.products = []

#     def add_product(self, product):
#         self.products.append(product)

#     def remove_product(self, product):
#         if product in self.products:
#             self.products.remove(product)

#     def show_cart(self):
#         print("Cart:")

#         for product in self.products:
#             product.show_info()

#     def get_total(self):
#         total = 0

#         for product in self.products:
#             total += product.price

#         return total


# class Store:
#     def __init__(self):
#         self.products = []
#         self.cart = Cart()

#     def add_product(self, product):
#         self.products.append(product)

#     def show_products(self):
#         print("Products:")

#         for product in self.products:
#             product.show_info()

#     def add_to_cart(self, product_name):
#         for product in self.products:
#             if product.name == product_name:
#                 self.cart.add_product(product)
#                 print(f"{product.name} added to cart.")
#                 return

#         print("Product not found.")

#     def show_cart(self):
#         self.cart.show_cart()
#         print(f"Total: ${self.cart.get_total()}")


# # Products
# laptop = Product("Laptop", 800)
# mouse = Product("Mouse", 30)
# keyboard = Product("Keyboard", 50)

# # Store
# store = Store()

# store.add_product(laptop)
# store.add_product(mouse)
# store.add_product(keyboard)

# store.show_products()

# print()

# store.add_to_cart("Laptop")
# store.add_to_cart("Mouse")

# print()

# store.show_cart()


# class Doctor:
#     def __init__(self, name, specialty):
#         self.name = name
#         self.specialty = specialty

#     def show_info(self):
#         print(f"Dr. {self.name} - {self.specialty}")


# class Patient:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def show_info(self):
#         print(f"{self.name} - {self.age} years old")


# class Appointment:
#     def __init__(self, doctor, patient, date):
#         self.doctor = doctor
#         self.patient = patient
#         self.date = date

#     def show_info(self):
#         print("Appointment:")
#         print(f"Doctor: Dr. {self.doctor.name}")
#         print(f"Patient: {self.patient.name}")
#         print(f"Date: {self.date}")


# class Hospital:
#     def __init__(self):
#         self.doctors = []
#         self.patients = []
#         self.appointments = []

#     def add_doctor(self, doctor):
#         self.doctors.append(doctor)

#     def add_patient(self, patient):
#         self.patients.append(patient)

#     def make_appointment(self, doctor, patient, date):
#         appointment = Appointment(doctor, patient, date)
#         self.appointments.append(appointment)

#     def show_doctors(self):
#         print("Doctors:")

#         for doctor in self.doctors:
#             doctor.show_info()

#     def show_patients(self):
#         print("Patients:")

#         for patient in self.patients:
#             patient.show_info()

#     def show_appointments(self):
#         print("Appointments:")

#         for appointment in self.appointments:
#             appointment.show_info()
#             print()


# # Create doctors
# doctor1 = Doctor("Ahmed", "Cardiology")
# doctor2 = Doctor("Sara", "Dermatology")

# # Create patients
# patient1 = Patient("Ali", 22)
# patient2 = Patient("Omar", 30)

# # Create hospital
# hospital = Hospital()

# # Add doctors
# hospital.add_doctor(doctor1)
# hospital.add_doctor(doctor2)

# # Add patients
# hospital.add_patient(patient1)
# hospital.add_patient(patient2)

# # Create appointments
# hospital.make_appointment(
#     doctor1,
#     patient1,
#     "2026-09-10"
# )

# hospital.make_appointment(
#     doctor2,
#     patient2,
#     "2026-09-11"
# )

# # Display everything
# hospital.show_doctors()

# print()

# hospital.show_patients()

# print()

# hospital.show_appointments()



# class Player:
#     def __init__(self, name, level):
#         self.name = name
#         self.level = level

#     def show_info(self):
#         print(f"{self.name} - Level {self.level}")


# class Team:
#     def __init__(self, name):
#         self.name = name
#         self.players = []

#     def add_player(self, player):
#         self.players.append(player)

#     def remove_player(self, player):
#         if player in self.players:
#             self.players.remove(player)

#     def show_players(self):
#         print(f"Team: {self.name}")
#         print("Players:")

#         for player in self.players:
#             player.show_info()

#     def get_average_level(self):
#         if not self.players:
#             return 0

#         total = 0

#         for player in self.players:
#             total += player.level

#         return total / len(self.players)


# class Game:
#     def __init__(self):
#         self.players = []
#         self.teams = []

#     def add_player(self, player):
#         self.players.append(player)

#     def create_team(self, name):
#         team = Team(name)
#         self.teams.append(team)
#         return team

#     def add_player_to_team(self, player, team):
#         if player in self.players and team in self.teams:
#             team.add_player(player)

#     def show_players(self):
#         print("All players:")

#         for player in self.players:
#             player.show_info()

#     def show_teams(self):
#         for team in self.teams:
#             team.show_players()
#             print(f"Average level: {team.get_average_level()}")
#             print()


# # Create players
# player1 = Player("Hunter", 25)
# player2 = Player("Alex", 30)
# player3 = Player("John", 20)
# player4 = Player("Mike", 35)

# # Create game
# game = Game()

# # Add players to game
# game.add_player(player1)
# game.add_player(player2)
# game.add_player(player3)
# game.add_player(player4)

# # Create teams
# team1 = game.create_team("Warriors")
# team2 = game.create_team("Legends")

# # Add players to teams
# game.add_player_to_team(player1, team1)
# game.add_player_to_team(player2, team1)

# game.add_player_to_team(player3, team2)
# game.add_player_to_team(player4, team2)

# # Show teams
# game.show_teams()



# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author

#     def show_info(self):
#         print(f"{self.title} - {self.author}")


# class Member:
#     def __init__(self, name):
#         self.name = name
#         self.borrowed_books = []

#     def borrow_book(self, book):
#         self.borrowed_books.append(book)

#     def return_book(self, book):
#         if book in self.borrowed_books:
#             self.borrowed_books.remove(book)

#     def show_borrowed_books(self):
#         print(f"{self.name}'s borrowed books:")

#         for book in self.borrowed_books:
#             book.show_info()


# class Library:
#     def __init__(self):
#         self.books = []
#         self.members = []

#     def add_book(self, book):
#         self.books.append(book)

#     def add_member(self, member):
#         self.members.append(member)

#     def show_books(self):
#         print("Library books:")

#         for book in self.books:
#             book.show_info()

#     def show_members(self):
#         print("Library members:")

#         for member in self.members:
#             print(member.name)


# # Create Book objects
# book1 = Book("Harry Potter", "J.K. Rowling")
# book2 = Book("The Hobbit", "J.R.R. Tolkien")
# book3 = Book("1984", "George Orwell")

# # Create Member objects
# member1 = Member("Hunter")
# member2 = Member("Alex")

# # Create Library object
# library = Library()

# # Add books to library
# library.add_book(book1)
# library.add_book(book2)
# library.add_book(book3)

# # Add members to library
# library.add_member(member1)
# library.add_member(member2)

# # Members borrow books
# member1.borrow_book(book1)
# member1.borrow_book(book2)

# member2.borrow_book(book3)

# # Show borrowed books
# member1.show_borrowed_books()

# print()

# member2.show_borrowed_books()

# from abc import ABC, abstractmethod


# class Payment(ABC):

#     @abstractmethod
#     def process_payment(self, amount):
#         pass

#     @abstractmethod
#     def refund(self, amount):
#         pass


# class CreditCard(Payment):
#     def __init__(self, card_number, owner):
#         self.card_number = card_number
#         self.owner = owner

#     def process_payment(self, amount):
#         last_four = self.card_number[-4:]
#         print(
#             f"Payment of ${amount} processed "
#             f"with credit card ending in {last_four}."
#         )

#     def refund(self, amount):
#         print(
#             f"Refund of ${amount} made "
#             f"to {self.owner}'s credit card."
#         )


# class PayPal(Payment):
#     def __init__(self, email):
#         self.email = email

#     def process_payment(self, amount):
#         print(
#             f"Payment of ${amount} processed "
#             f"through PayPal: {self.email}"
#         )

#     def refund(self, amount):
#         print(
#             f"Refund of ${amount} sent to {self.email}"
#         )


# class Cash(Payment):

#     def process_payment(self, amount):
#         print(f"Payment of ${amount} received in cash.")

#     def refund(self, amount):
#         print(f"Refund of ${amount} given in cash.")


# # Create objects
# credit_card = CreditCard("1234567890121234", "Hunter")
# paypal = PayPal("hunter@example.com")
# cash = Cash()

# # Test
# credit_card.process_payment(100)
# credit_card.refund(50)

# paypal.process_payment(200)
# paypal.refund(100)

# cash.process_payment(50)
# cash.refund(20)

# print()

# # Polymorphism
# payments = [credit_card, paypal, cash]

# for payment in payments:
#     payment.process_payment(100)


# class BankAccount:
#     def __init__(self, owner, balance, account_type):
#         self.owner = owner
#         self.balance = balance
#         self.account_type = account_type

#     def show_info(self):
#         print(f"Owner: {self.owner}")
#         print(f"Balance: ${self.balance}")
#         print(f"Type: {self.account_type}")

#     @classmethod
#     def create_savings(cls, owner, initial_balance):
#         return cls(owner, initial_balance, "Savings")

#     @classmethod
#     def from_string(cls, data):
#         owner, balance, account_type = data.split(",")

#         return cls(owner, float(balance), account_type)


# # Normal creation
# account1 = BankAccount("Hunter", 1000, "Checking")

# # Using class method
# account2 = BankAccount.create_savings("Hunter", 500)

# # Using class method with a string
# account3 = BankAccount.from_string(
#     "Alex,2500,Checking"
# )

# account1.show_info()

# print()

# account2.show_info()

# print()

# account3.show_info()


# class Temperature:

#     @staticmethod
#     def celsius_to_fahrenheit(celsius):
#         return celsius * 9 / 5 + 32

#     @staticmethod
#     def fahrenheit_to_celsius(fahrenheit):
#         return (fahrenheit - 32) * 5 / 9

#     @staticmethod
#     def is_freezing(celsius):
#         return celsius <= 0

#     @staticmethod
#     def is_boiling(celsius):
#         return celsius >= 100


# print(Temperature.celsius_to_fahrenheit(0))
# print(Temperature.fahrenheit_to_celsius(212))

# print(Temperature.is_freezing(-5))
# print(Temperature.is_freezing(20))

# print(Temperature.is_boiling(100))
# print(Temperature.is_boiling(50))

# class Product:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity

#     def __repr__(self):
#         return f"Product(name='{self.name}', price={self.price}, quantity={self.quantity})"

#     def __str__(self):
#         return f"{self.name} - ${self.price} ({self.quantity} available)"


# laptop = Product("Laptop", 800, 2)

# print(repr(laptop))
# print(laptop)

# class Product:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity

#     def __eq__(self, other):
#         return (
#             self.name == other.name
#             and self.price == other.price
#             and self.quantity == other.quantity
#         )


# p1 = Product("Laptop", 800, 2)
# p2 = Product("Laptop", 800, 2)
# p3 = Product("Mouse", 30, 5)

# print(p1 == p2)
# print(p1 == p3)

# class Playlist:
#     def __init__(self, name, songs):
#         self.name = name
#         self.songs = songs

#     def __len__(self):
#         return len(self.songs)

#     def add_song(self, song):
#         self.songs.append(song)


# playlist = Playlist(
#     "My Favorites",
#     ["Song A", "Song B", "Song C"]
# )

# print(len(playlist))

# playlist.add_song("Song D")

# print(len(playlist))
# print(f"Playlist contains {len(playlist)} songs.")

# class ShoppingCart:
#     def __init__(self, items, total):
#         self.items = items
#         self.total = total

#     def __add__(self, other):
#         new_items = self.items + other.items
#         new_total = self.total + other.total

#         return ShoppingCart(new_items, new_total)


# cart1 = ShoppingCart(["Laptop", "Mouse"], 830)
# cart2 = ShoppingCart(["Keyboard"], 50)

# cart3 = cart1 + cart2

# print(cart3.items)
# print(cart3.total)

# print(cart1.total)
# print(cart2.total)
# print(cart3.total)

# class Playlist:
#     def __init__(self, name, songs):
#         self.name = name
#         self.songs = songs

#     def __getitem__(self, index):
#         return self.songs[index]


# playlist = Playlist(
#     "Favorites",
#     ["Song A", "Song B", "Song C"]
# )

# print(playlist[0])
# print(playlist[1])
# print(playlist[2])

# print(playlist[-1])
# print(playlist[0:2])

# class Playlist:
#     def __init__(self, name, songs):
#         self.name = name
#         self.songs = songs

#     def __contains__(self, song):
#         return song.lower() in [s.lower() for s in self.songs]


# playlist = Playlist(
#     "Favorites",
#     ["Song A", "Song B", "Song C"]
# )

# print("Song A" in playlist)
# print("Song X" in playlist)

# if "Song B" in playlist:
#     print("Song B is in the playlist!")

# print("song a" in playlist)



# class Playlist:
#     def __init__(self, name, songs):
#         self.name = name
#         self.songs = songs

#     def __iter__(self):
#         return iter(self.songs)


# playlist = Playlist(
#     "Favorites",
#     ["Song A", "Song B", "Song C"]
# )

# for song in playlist:
#     print(song)

# songs = list(playlist)
# print(songs)


# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#     def __lt__(self, other):
#         return self.price < other.price

#     def __str__(self):
#         return f"{self.name} - ${self.price}"


# p1 = Product("Laptop", 800)
# p2 = Product("Mouse", 30)

# print(p2 < p1)
# print(p1 < p2)

# products = [
#     Product("Laptop", 800),
#     Product("Mouse", 30),
#     Product("Keyboard", 50)
# ]

# products.sort()

# for product in products:
#     print(product)



# class MyResource:
#     def __init__(self):
#         self.name = "Database Connection"

#     def __enter__(self):
#         print(f"{self.name} opened")
#         return self

#     def __exit__(self, exc_type, exc_value, traceback):
#         print(f"{self.name} closed")


# with MyResource() as resource:
#     print(f"Using {resource.name}")




# class Calculator:
#     def __init__(self, operation):
#         self.operation = operation

#     def __call__(self, a, b):
#         if self.operation == "add":
#             return a + b

#         elif self.operation == "multiply":
#             return a * b

#         elif self.operation == "subtract":
#             return a - b

#         else:
#             raise ValueError("Unknown operation")


# calculator = Calculator("add")

# print(calculator(10, 5))

# calculator = Calculator("multiply")

# print(calculator(10, 5))

# calculator = Calculator("subtract")

# print(calculator(10, 5))






# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance

#     def __bool__(self):
#         return self.balance > 0

#     def deposit(self, amount):
#         self.balance += amount

#     def withdraw(self, amount):
#         self.balance -= amount


# account1 = BankAccount("Hunter", 500)
# account2 = BankAccount("Alex", 0)

# print(bool(account1))
# print(bool(account2))

# if account1:
#     print("Account has money")

# if not account2:
#     print("Account is empty")




# class User:
#     def __init__(self, username, email):
#         self.username = username
#         self.email = email

#     def __eq__(self, other):
#         if not isinstance(other, User):
#             return NotImplemented

#         return self.email == other.email

#     def __hash__(self):
#         return hash(self.email)


# user1 = User("Hunter", "hunter@example.com")
# user2 = User("Hunter123", "hunter@example.com")
# user3 = User("Alex", "alex@example.com")

# print(user1 == user2)
# print(user1 == user3)

# users = {user1, user2, user3}

# print(len(users))



# class Playlist:
#     def __init__(self, name, songs):
#         self.name = name
#         self.songs = songs

#     def __getitem__(self, index):
#         return self.songs[index]

#     def __setitem__(self, index, value):
#         self.songs[index] = value

#     def __iter__(self):
#         return iter(self.songs)


# playlist = Playlist(
#     "Favorites",
#     ["Song A", "Song B", "Song C"]
# )

# print(playlist[0])

# playlist[0] = "New Song"

# print(playlist[0])

# playlist[1] = "Another Song"

# for song in playlist:
#     print(song)






# class Playlist:
#     def __init__(self, name, songs):
#         self.name = name
#         self.songs = songs

#     def __getitem__(self, index):
#         return self.songs[index]

#     def __setitem__(self, index, value):
#         self.songs[index] = value

#     def __delitem__(self, index):
#         del self.songs[index]

#     def __iter__(self):
#         return iter(self.songs)


# playlist = Playlist(
#     "Favorites",
#     ["Song A", "Song B", "Song C"]
# )

# del playlist[1]

# for song in playlist:
#     print(song)






# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#     def __eq__(self, other):
#         if not isinstance(other, Product):
#             return NotImplemented

#         return self.price == other.price

#     def __ne__(self, other):
#         if not isinstance(other, Product):
#             return NotImplemented

#         return self.price != other.price

#     def __lt__(self, other):
#         if not isinstance(other, Product):
#             return NotImplemented

#         return self.price < other.price

#     def __le__(self, other):
#         if not isinstance(other, Product):
#             return NotImplemented

#         return self.price <= other.price

#     def __gt__(self, other):
#         if not isinstance(other, Product):
#             return NotImplemented

#         return self.price > other.price

#     def __ge__(self, other):
#         if not isinstance(other, Product):
#             return NotImplemented

#         return self.price >= other.price


# p1 = Product("Laptop", 800)
# p2 = Product("Mouse", 30)
# p3 = Product("Keyboard", 800)

# print(p1 == p3)
# print(p1 != p2)

# print(p2 < p1)
# print(p1 <= p3)

# print(p1 > p2)
# print(p1 >= p3)





# class ScoreBoard(dict):
#     def __missing__(self, key):
#         return 0

#     def add_score(self, player, points):
#         self[player] = self.get(player, 0) + points


# scores = ScoreBoard()

# scores["Hunter"] = 100
# scores["Alex"] = 80

# print(scores["Hunter"])  # 100
# print(scores["John"])    # 0

# scores.add_score("Hunter", 50)
# scores.add_score("John", 30)

# print(scores)





# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#     def __str__(self):
#         return f"{self.name} - ${self.price:.2f}"

#     def __format__(self, format_spec):
#         if format_spec == "short":
#             return self.name

#         elif format_spec == "full":
#             return f"{self.name} - ${self.price:.2f}"

#         elif format_spec == "":
#             return str(self)

#         else:
#             raise ValueError(f"Unknown format: {format_spec}")


# product = Product("Keyboard", 49.99)

# print(f"{product}")
# print(f"{product:short}")
# print(f"{product:full}")




# class User:
#     def __init__(self, username, age, email):
#         self.username = username
#         self.age = age
#         self.email = email

#     def __str__(self):
#         return f"{self.username} ({self.age})"

#     def __repr__(self):
#         return (
#             f"User(username='{self.username}', "
#             f"age={self.age}, email='{self.email}')"
#         )

#     def __format__(self, format_spec):
#         if format_spec == "short":
#             return self.username

#         elif format_spec == "full":
#             return f"{self.username} ({self.age}) - {self.email}"

#         elif format_spec == "":
#             return str(self)

#         else:
#             raise ValueError("Unknown format")


# user = User("Hunter", 20, "hunter@example.com")

# print(user)
# print(repr(user))
# print(f"{user}")
# print(f"{user:short}")
# print(f"{user:full}")



# class Number:
#     def __new__(cls, value):
#         return super().__new__(cls)

#     def __init__(self, value):
#         value = int(value)
#         self.value = value

# n = Number("100")
# print(n.value)
# print(type(n.value))


# class PositiveNumber(int):
#     def __new__(cls, nb):
#         if nb <= 0:
#             raise ValueError("number must be positive")
#         return super().__new__(cls, nb)

#     def __init__(self, nb):
#         self.nb = nb

# a = PositiveNumber(50)
# b = PositiveNumber(25)

# print(a)
# print(b)
# print(a + b)
    

# class User:
#     def __init__(self, username):
#         self.username = username

#     def __getattr__(self, name):
#         print(f"Unknown attribute: {name}")
#         return None

# user = User("Hunter")

# print(user.username)
# print(user.age)
# print(user.country)

# class Config:
#     def __init__(self):
#         self.host = "localhost"
#         self.port = 8080

#     def __getattr__(self, name):
#         if name == "debug":
#             return False

#         elif name == "timeout":
#             return 30

#         else:
#             return None


# config = Config()

# print(config.host)
# print(config.port)
# print(config.debug)
# print(config.timeout)
# print(config.database)

# class User:
#     def __init__(self, username, age):
#         self.username = username
#         self.age = age

#     def __getattribute__(self, name):
#         print(f"Accessing: {name}")
#         return object.__getattribute__(self, name)


# user = User("Hunter", 20)

# print(user.username)
# print(user.age)


# class Player:
#     def __init__(self, username):
#         self.username = username


# player = Player("Hunter")

# print("Player has username:", hasattr(player, "username"))
# print("Player has score:", hasattr(player, "score"))
# print("Player has level:", hasattr(player, "level"))

# player.score = 100

# print("Player has score:", hasattr(player, "score"))



# class User:
#     def __setattr__(self, name, value):
#         if "username" == name and hasattr("self", name):
#             raise AttributeError("username cannot be changed")
#         print(f"setting {name} = {value}")
#         object.__setattr__(self, name, value)

# user = User()

# user.username = "Hunter"
# print(user.username)

# user.age = 20
# print(user.age)

# user.age = 21
# print(user.age)

# user.username = "Alex"


# class Player:
#     def __setattr__(self, name, value):
#         if "usernamme" == name and hasattr(self, name):
#             AttributeError("username cannot be change")
#         print(f"setting {name} = {value}")
#         object.__setattr__(self, name, value)


# player = Player()

# player.username = "Hunter"
# player.score = 100
# player.level = 5

# print()
# print(player.username)
# print(player.score)
# print(player.level)

# print()

# player.score = 150

# print()
# print(player.username)
# print(player.score)
# print(player.level)

# player.username = "Alex"


# class User:
#     def __init__(self, username, age, email):
#         self.username = username
#         self.age = age
#         self.email = email

#     def __getattribute__(self, name):
#         print(f"reading attribute: {name}")
#         return object.__getattribute__(self, name)

# user = User("Hunter", 20, "hunter@email.com")

# print(user.username)
# print(user.age)
# print(user.email)


# class User:
#     def __init__(self, username, age, password):
#         self.username = username
#         self.age = age
#         self._password = password

#     def __getattribute__(self, name):
#         if "_password" == name:
#             raise AttributeError(" Password is private")
#         print(f"reading: {name}")
#         return object.__getattribute__(self, name)

# user = User("Hunter", 20, "12345")

# print(user.username)
# print(user.age)
# print(user._password)

# class BankAccount:
#     def __init__(self, owner, balance, pin):
#         self.owner = owner
#         self.balance = balance
#         self._pin = pin

#     def __getattribute__(self, name):
#         if "_pin" == name:
#             raise AttributeError("pin not acccessible for you")
#         print(f"accessing {name}")
#         return object.__getattribute__(self, name)

# account = BankAccount("Hunter", 5000, "1234")

# print(account.owner)
# print(account.balance)
# print(account._pin)


# class User:
#     def __init__(self, username, age):
#         self.username = username
#         self.age = age
#         self._access_count = 0

#     def __getattribute__(self, name):
#         if name == "_access_count":
#             return object.__getattribute__(self, name)

#         if name == "username" or name == "age":
#             count = object.__getattribute__(self, "_access_count")
#             object.__setattr__(self, "_access_count", count + 1)

#         return object.__getattribute__(self, name)


# user = User("Hunter", 20)

# print(user.username)
# print(user.age)
# print(user.username)
# print(user._access_count)

# class Product:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity

#     def __setattr__(self, name, value):
#         print(f"set {name} = {value}")
#         object.__setattr__(self, name, value)

#     def __getattribute__(self, name):
#         print(f"get {name}")
#         return object.__getattribute__(self, name)


# product = Product("Keyboard", 50, 10)

# print(product.name)

# product.price = 60

# print(product.price)


# class BankAccount:
#     def __init__(self, owner, balance, _account_number):
#         self.owner = owner
#         self.balance = balance
#         self._account_number = _account_number

#     def __setattr__(self, name, value):
#         if "balance" == name and value < 0:
#             raise ValueError("balance cannot be negative")
#         print(f"SET {name} = {value}")
#         object.__setattr__(self, name, value)

#     def __getattribute__(self, name):
#         if "_account_number" == name:
#             raise AttributeError("account number is private")
        
#         if name == "owner" or name == "balance":
#             print(f"GET {name}")

#         return object.__getattribute__(self, name)

# account = BankAccount("Hunter", 1000, "123456")

# print(account.owner)
# print(account.balance)

# account.balance = 1500

# print(account.balance)

# # account.balance = -500

# # print(account._account_number)


# class Player:
#     def __init__(self, username, score, level, is_admin):
#         self.username = username
#         self.score = score
#         self.level = level
#         self.is_admin = is_admin

#     def __setattr__(self, name, value):
#         if "score" == name and value < 0:
#             raise ValueError("score cannot be negative")
#         if "is_admin" == name and hasattr(self, name):
#             raise AttributeError("is_admin cannot be change")
#         print(f"SET {name} = {value}")
#         object.__setattr__(self, name, value)

#     def __getattribute__(self, name):
#         if "is_admin" == name:
#             raise AttributeError("is_admin is private")
#         print(f"GET {name}")
#         return object.__getattribute__(self, name)

# player = Player("Hunter", 100, 5, False)

# print(player.username)
# print(player.score)
# print(player.level)

# player.score = 200
# print(player.score)

# player.score = -50

# player._is_admin = True
# player._is_admin = False



# class Player:
#     def __init__(self, username, score):
#         self.username = username
#         self.score = score
#         self.level = 1

#     def __setattr__(self, name, value):
#         print(f"SET {name} = {value}")

#         if name == "score":
#             if value < 100:
#                 level = 1
#             elif value < 200:
#                 level = 2
#             elif value < 300:
#                 level = 3
#             else:
#                 level = 4

#             object.__setattr__(self, "score", value)
#             object.__setattr__(self, "level", level)

#         else:
#             object.__setattr__(self, name, value)

#     def __getattribute__(self, name):
#         if name == "username" or name == "score" or name == "level":
#             print(f"GET {name}")

#         return object.__getattribute__(self, name)


# player = Player("Hunter", 50)

# print(player.level)

# player.score = 150
# print(player.level)

# player.score = 250
# print(player.level)

# player.score = 500
# print(player.level)

# class Player:
#     def __init__(self, username, score, level, rank):
#         self.username = username
#         self.score = score
#         self.level = level
#         self._rank = rank

#     def __setattr__(self, name, value):
#         if name == "score" and value < 0:
#             raise ValueError("Score cannot be negative")

#         if name == "_rank" and hasattr(self, "_rank"):
#             raise AttributeError("rank cannot be changed")

#         print(f"SET {name} = {value}")
#         object.__setattr__(self, name, value)

#     def __getattribute__(self, name):
#         if name == "_rank":
#             print("GET private rank")
#         elif name == "username" or name == "score" or name == "level":
#             print(f"GET {name}")

#         return object.__getattribute__(self, name)


# player = Player("Hunter", 100, 5, "Gold")

# print(player.username)
# print(player.score)
# print(player.level)
# print(player._rank)

# player.score = 200
# print(player.score)

# player._rank = "Silver"


# class User:
#     def __init__(self, username, email, password):
#         self.username = username
#         self.email = email
#         self.password = password

#     def __delattr__(self, name):
#         if "username" == name:
#             raise AttributeError("username cannot be deleted")
#         print(f"deleting {name}")
#         object.__delattr__(self, name)

# user = User("Hunter", "hunter@email.com", "12345")

# del user.email

# print(user.username)
# print(user.password)

# del user.username

# def my_decorator(fun):

#     def wrapper():
#         print("before fun")

#         fun()

#         print("after fun")

#     return wrapper

# def say_hello():
#     print("hello")

# say_hello = my_decorator(say_hello)
# say_hello()

# def my_decorator(fun):

#     def wrapper(name):
#         print("before fun")

#         fun(name)

#         print("after fun")

#     return wrapper

# def greet(name):
#     print(f"Hello {name}")

# greet = my_decorator(greet)

# greet("Hunter")

# def my_decorator(fun):

#     def wrapper(a, b):
#         print("before fun")

#         result = fun(a, b)

#         print("after fun")

#         return result

#     return wrapper

# def add(a, b):
#     return a + b

# add = my_decorator(add)
# result = add(5, 10)
# print(result)


# def my_decorator(fun):

#     def wrapper(a, b):
#         print("before fun")

#         result = fun(a, b)

#         print("after fun")

#         return result

#     return wrapper

# @my_decorator
# def add(a, b):
#     return a + b

# print(add(10, 5))


# def my_decorator(fun):

#     def wrapper(*args):

#         print("before fun")

#         result = fun(*args)

#         print("after fun")

#         return result
    
#     return wrapper

# @my_decorator
# def add(a, b):
#     return a + b

# @my_decorator
# def greet(name):
#     return f"hello {name}"

# print(add(10, 5))
# print(greet("Hunter"))

# def my_decorator(fun):

#     def wrapper(*args, **kwargs):

#         print("before fun")

#         result = fun(*args, **kwargs)

#         print("after fun")

#         return result
    
#     return wrapper

# @my_decorator
# def greet(name, age):
#     return f"{name} is {age}"


# print(greet("Hunter", 20))
# print(greet(name=20, age="Hunter"))


# def logger(fun):

#     def wrapper(*args, **kwargs):
#         print("before fun")

#         result = fun(*args, **kwargs)

#         print("after fun")

#         return result

#     return wrapper

# @logger
# def greet(name, age, city):
#     return f"{name} is {age} and lives in {city}"


# print(greet("Hunter", 20, "Algiers"))

# print(greet(name=20, age="Algiers", city="Hunter"))


# from functools import wraps


# def logger(func):

#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         return func(*args, **kwargs)

#     return wrapper


# @logger
# def add(a, b):
#     """Add two numbers."""
#     return a + b


# print(add(10, 5))
# print(add.__name__)
# print(add.__doc__)

# import time
# from functools import wraps

# def timer(fun):
    
#     @wraps(fun)
#     def wrapper(*args, **kwargs):
        
#         start = time.perf_counter()
        
#         result = fun(*args, **kwargs)

#         end = time.perf_counter()

#         duration = end - start

#         print(f"executing time: {duration:.6f} seconds")

#         return result
    
#     return wrapper

# @timer
# def calculate():
#     total = 0

#     for i in range(1, 1_000_001):
#         total += i

#     return total


# print(calculate())

# from functools import wraps

# def positive_only(fun):

#     @wraps(fun)
#     def wrapper(*args, **kwargs):

#         for value in args:
#             if value < 0:
#                 print("Error: number must be positive")
#                 return
            
#         for value in kwargs.values():
#             if value < 0:
#                 print("Error: number cannot be negative")
#                 return
            
#         return fun(*args, **kwargs)
    
#     return wrapper

# @positive_only
# def calculate(a, b):
#     return a * b

# print(calculate(5, 3))
# print(calculate(5, -3))
# print(calculate(a=4, b=2))

# from functools import wraps


# def repeat(times):

#     def decorator(func):

#         @wraps(func)
#         def wrapper(*args, **kwargs):

#             result = None

#             for _ in range(times):
#                 result = func(*args, **kwargs)

#             return result

#         return wrapper

#     return decorator


# @repeat(3)
# def hello():
#     print("Hello")


# @repeat(5)
# def greet(name):
#     print(f"Hello {name}")


# hello()
# greet("Hunter")

# from functools import wraps

# def double_resault(func):

#     @wraps(func)
#     def wrapper(*args, **kwargs):

#         result = func(*args, *kwargs)

#         return result * 2
    
#     return wrapper

# @double_resault
# def add(a, b):
#     return a + b

# print(add(2, 3))

# from functools import wraps

# user_logged_in = True

# def login_required(func):

#     @wraps(func)
#     def wrapper(*args, **kwargs):

#         if user_logged_in:
#             return func(*args, **kwargs)
        
#         print("access denied you need to login")

#     return wrapper

# @login_required
# def view_profile():
#     print("welcome to your profile")

# view_profile()



# from functools import wraps


# def log_call(func):

#     @wraps(func)
#     def wrapper(*args, **kwargs):

#         print(f"Calling: {func.__name__}")
#         print(f"Arguments: {args}")

#         result = func(*args, **kwargs)

#         print(f"Result: {result}")

#         return result

#     return wrapper


# @log_call
# def add(a, b):
#     return a + b


# print(add(10, 5))


# from functools import wraps


# def log_call(func):

#     @wraps(func)
#     def wrapper(*args, **kwargs):

#         print(f"Calling: {func.__name__}")
#         print(f"Positional arguments: {args}")
#         print(f"Keyword arguments: {kwargs}")

#         result = func(*args, **kwargs)

#         print(f"Result: {result}")

#         return result

#     return wrapper


# @log_call
# def add(a, b):
#     return a + b


# print(add(10, 5))
# print()
# print(add(a=10, b=5))
# print()
# print(add(10, b=5))


from functools import wraps


def retry(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        for attempt in range(1, 4):

            try:
                result = func(*args, **kwargs)
                return result

            except Exception:
                print(f"Attempt {attempt} failed")

        print("All attempts failed")

    return wrapper


@retry
def test():
    print("Trying...")
    raise ValueError("Something went wrong")


test()
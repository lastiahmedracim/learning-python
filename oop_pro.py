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


# from functools import wraps


# def retry(func):

#     @wraps(func)
#     def wrapper(*args, **kwargs):

#         for attempt in range(1, 4):

#             try:
#                 result = func(*args, **kwargs)
#                 return result

#             except Exception:
#                 print(f"Attempt {attempt} failed")

#         print("All attempts failed")

#     return wrapper


# @retry
# def test():
#     print("Trying...")
#     raise ValueError("Something went wrong")


# test()


# from functools import wraps


# def retry(func):

#     @wraps(func)
#     def wrapper(*args, **kwargs):

#         for attempt in range(1, 4):

#             try:
#                 result = func(*args, **kwargs)
#                 return result

#             except Exception:
#                 print(f"Attempt {attempt} failed")

#         print("All attempts failed")
#         return None

#     return wrapper


# @retry
# def divide(a, b):
#     return a / b


# print(divide(10, 2))

# print()

# result = divide(10, 0)
# print(result)





# from functools import wraps


# def retry(times):

#     def decorator(func):

#         @wraps(func)
#         def wrapper(*args, **kwargs):

#             for attempt in range(1, times + 1):

#                 try:
#                     result = func(*args, **kwargs)
#                     return result

#                 except Exception:
#                     print(f"Attempt {attempt} failed")

#             print("All attempts failed")
#             return None

#         return wrapper

#     return decorator


# @retry(5)
# def divide(a, b):
#     return a / b


# print(divide(10, 2))

# print()

# print(divide(10, 0))



# from functools import wraps

# def uppercase(func):

#     @wraps(func)
#     def wrapper(*args, **kwargs):

#         resault = func(*args, **kwargs)
#         return resault.upper()
    
#     return wrapper

# @uppercase
# def greet(name):
#     return f"hello {name}"

# print(greet("Hunter"))



# from functools import wraps


# def cache(func):

#     cache_data = {}

#     @wraps(func)
#     def wrapper(n):

#         if n in cache_data:
#             return cache_data[n]

#         result = func(n)

#         cache_data[n] = result

#         return result

#     return wrapper


# @cache
# def square(n):
#     print("Calculating...")
#     return n * n


# print(square(5))
# print(square(5))
# print(square(10))
# print(square(5))




# from functools import wraps


# def cache(func):

#     cache_data = {}

#     @wraps(func)
#     def wrapper(*args):

#         if args in cache_data:
#             return cache_data[args]

#         result = func(*args)

#         cache_data[args] = result

#         print(cache_data)
#         return result

#     return wrapper


# @cache
# def add(a, b):
#     print("Calculating...")
#     return a + b

# print(add(2, 3))
# print(add(2, 3))
# print(add(5, 10))
# print(add(2, 3))




# from functools import wraps


# def cache(func):

#     cache_data = {}

#     @wraps(func)
#     def wrapper(*args, **kwargs):

#         key = (args, tuple(kwargs.items()))
#         if key in cache_data:
#             return cache_data[key]
            
#         resault = func(*args, **kwargs)
#         cache_data[key] = resault
#         return resault


#     return wrapper


# @cache
# def add(a, b):
#     print("Calculating...")
#     return a + b

# print(add(2, 3))
# print(add(2, 3))
# print(add(5, 10))
# print(add(2, 3))





# class CountDown:

#     def __init__(self, start):
#         self.current = start

#     def __iter__(self):
#         return self

#     def __next__(self):

#         if self.current <= 0:
#             raise StopIteration

#         number = self.current
#         self.current -= 1

#         return number


# counter = CountDown(5)

# for number in counter:
#     print(number)


# class NumberRange:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end

#     def __iter__(self):
#         return self

#     def __next__(self):

#         if self.start > self.end:
#             raise StopIteration

#         number = self.start
#         self.start += 1

#         return number

# numbers = NumberRange(2, 6)

# for n in numbers:
#     print(n)


# def count_up(start, end):

#     current = start

#     while current <= end:
#         yield current
#         current += 1


# for number in count_up(1, 5):
#     print(number)


# def even_numbers(start, end):

#     current = start

#     while current <= end:
#         if current % 2 == 0:
#             yield current
#         current += 1
    
# for n in even_numbers(1, 10):
#     print(n)


# def squares(a, b):

#     current = a

#     while current <= b:
#         s = current * current
#         yield s
#         current += 1
        

# for nb in squares(1, 5):
#     print(nb)


# def fibonacci(n):

#     a = 0
#     b = 1

#     for _ in range(n):
#         yield a

#         a, b = b, a + b


# for number in fibonacci(8):
#     print(number)


# generator = (number ** 2 for number in range(1, 11))

# for number in generator:
#     print(number)



# generator = (number ** 2 for number in range(2, 21) if number % 2 == 0)

# for number in generator:
#     print(number)

# generator = (number ** 2 for number in range (1, 51) if number % 3 == 0)

# for n in generator:
#     print(n)

# def positive_numbers(numbers):

#     for n in numbers:
#         if n > 0:
#             yield n

# numbers = [-5, 10, -2, 7, 0, 3, -8]

# for number in positive_numbers(numbers):
#     print(number)


# def process_numbers(numbers):

#     for number in numbers:
#         if number % 3 == 0:
#             yield number ** 2


# numbers = [1, 4, 7, 10, 12, 15, 18, 21, 25]

# for number in process_numbers(numbers):
#     print(number)

# def positive_even_numbers(numbers):

#     for n in numbers:
#         if n > 0 and n % 2 == 0:
#             yield n

# numbers = [-10, -4, -2, 0, 2, 4, 7, 8, 11, 12]

# for n in positive_even_numbers(numbers):
#     print(n)

# def calculator():
#     total = 0

#     while True:
#         value = yield total
#         total += value


# calc = calculator()

# next(calc)

# print(calc.send(10))
# print(calc.send(5))
# print(calc.send(20))


# def average():
#     total = 0
#     count = 0

#     while True:
#         number = yield total / count if count > 0 else 0
#         total += number
#         count += 1


# avg = average()

# next(avg)

# print(avg.send(10))
# print(avg.send(20))
# print(avg.send(30))
# print(avg.send(40))

# def numbers1():
#     yield 1
#     yield 2
#     yield 3


# def numbers2():
#     yield 4
#     yield 5
#     yield 6


# def all_numbers():
#     yield from numbers1()
#     yield from numbers2()


# for number in all_numbers():
#     print(number)

# def numbers():
#     number = 1

#     while True:
#         yield number
#         number += 1


# gen = numbers()

# print(next(gen))
# print(next(gen))
# print(next(gen))

# gen.close()

# try:
#     print(next(gen))
# except StopIteration:
#     print("Generator is closed")


# def numbers():
#     n = 1
#     while True:

#         try:
#             yield n
#             n += 1
#         except ValueError as error:
#             print(f"error received {error}")

# gen = numbers()

# print(next(gen))
# print(next(gen))

# print(gen.throw(ValueError("Something went wrong!")))

# def counter():
#     n = 0
#     while True:
#         try:
#             yield n
#             n += 1
#         except ValueError as error:
#             print(f"counter {error}")

# counter = counter()

# print(next(counter))
# print(next(counter))
# print(next(counter))

# counter.throw(ValueError("reset"))

# print(next(counter))
# print(next(counter))

# def bank_account():
#     balance = 0

#     while True:
#         try:
#             n = yield balance
#             balance += n
            
#         except ValueError as error:
#             print(f"{error}")
#             balance = 0

# account = bank_account()

# next(account)

# print(account.send(100))
# print(account.send(50))
# print(account.send(-30))

# account.throw(ValueError("Account error"))

# print(account.send(200))

# def numbers():
#     for number in range(1, 21):
#         yield number


# def even_numbers(numbers):
#     for number in numbers:
#         if number % 2 == 0:
#             yield number


# def squares(numbers):
#     for number in numbers:
#         yield number ** 2


# numbers_generator = numbers()
# even_generator = even_numbers(numbers_generator)
# square_generator = squares(even_generator)

# for number in square_generator:
#     print(number)



# def numbers():
#     for number in range(1, 51):
#         yield number


# def divisible_by_3(numbers):
#     for number in numbers:
#         if number % 3 == 0:
#             yield number


# def greater_than_20(numbers):
#     for number in numbers:
#         if number > 20:
#             yield number


# def squares(numbers):
#     for number in numbers:
#         yield number ** 2


# numbers_generator = numbers()

# divisible_generator = divisible_by_3(numbers_generator)

# greater_generator = greater_than_20(divisible_generator)

# square_generator = squares(greater_generator)


# for number in square_generator:
#     print(number)



# class Product:
#     def __init__(self, name, price, category):
#         self.name = name
#         self.price = price
#         self.category = category


# def products():
#     yield Product("Laptop", 1200, "Electronics")
#     yield Product("Mouse", 50, "Electronics")
#     yield Product("Keyboard", 150, "Electronics")
#     yield Product("Chair", 200, "Furniture")
#     yield Product("Pen", 10, "Office")
#     yield Product("Monitor", 300, "Electronics")


# def expensive_products(products):
#     for product in products:
#         if product.price > 100:
#             yield product


# def product_names(products):
#     for product in products:
#         yield product.name


# product_generator = products()

# expensive_generator = expensive_products(product_generator)

# name_generator = product_names(expensive_generator)


# for name in name_generator:
#     print(name)


# def safe_numbers(data):
#     for item in data:
#         try:
#             if isinstance(item, (int, float)):
#                 yield item
#         except TypeError:
#             pass


# data = [10, 20, "hello", 30, "Python", 40, 50]

# for number in safe_numbers(data):
#     print(number)


# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price


# def products():
#     yield Product("Laptop", 1200)
#     yield Product("Mouse", -50)
#     yield Product("Keyboard", 150)
#     yield Product("Monitor", -100)
#     yield Product("Phone", 800)


# def valid_products(products):
#     for product in products:
#         if isinstance(product.price, (int, float)) and product.price >= 0:
#             yield product


# def product_prices(products):
#     for product in products:
#         yield product.price


# product_generator = products()

# valid_generator = valid_products(product_generator)

# price_generator = product_prices(valid_generator)


# for price in price_generator:
#     print(price)




# class Product:
#     def __init__(self, name, price, category):
#         self.name = name
#         self.price = price
#         self.category = category


# def products():
#     yield Product("Laptop", 1200, "Electronics")
#     yield Product("Mouse", 50, "Electronics")
#     yield Product("Keyboard", 150, "Electronics")
#     yield Product("Chair", 200, "Furniture")
#     yield Product("Phone", 800, "Electronics")
#     yield Product("Table", 300, "Furniture")


# def electronics(products):
#     for product in products:
#         if product.category == "Electronics":
#             yield product


# def expensive(products):
#     for product in products:
#         if product.price > 100:
#             yield product


# def discounted_prices(products):
#     for product in products:
#         yield product.price * 0.90


# product_generator = products()

# electronics_generator = electronics(product_generator)

# expensive_generator = expensive(electronics_generator)

# discounted_generator = discounted_prices(expensive_generator)


# for price in discounted_generator:
#     print(price)



# def price_filter():
#     minimum_price = 100

#     while True:
#         price = yield

#         if price >= minimum_price:
#             yield price
#         else:
#             yield None


# filter_gen = price_filter()

# next(filter_gen)

# print(filter_gen.send(50))
# print(filter_gen.send(100))
# print(filter_gen.send(250))
# print(filter_gen.send(80))


# def counter():
#     count = 0

#     command = yield count

#     while True:
#         if command == "add":
#             count += 1

#         elif command == "remove":
#             count -= 1

#         elif command == "reset":
#             count = 0

#         command = yield count


# counter_gen = counter()

# next(counter_gen)

# print(counter_gen.send("add"))
# print(counter_gen.send("add"))
# print(counter_gen.send("remove"))
# print(counter_gen.send("add"))
# print(counter_gen.send("reset"))
# print(counter_gen.send("hello"))


# def bank_account():

#     balance = 0
#     comande = yield balance

#     while True:
#         action, amount = comande
#         if action == "deposit":
#             balance += amount
#         elif action == "withdraw":
#             balance -= amount
#         elif action == "reset":
#             balance = 0
#         else:
#             balance = 0
#         comande = yield balance

# account = bank_account()

# next(account)

# print(account.send(("deposit", 100)))
# print(account.send(("deposit", 50)))
# print(account.send(("withdraw", 30)))
# print(account.send(("deposit", 200)))
# print(account.send(("reset", 0)))
# print(account.send(("hello", 0)))



# def numbers():
#     yield 1
#     yield 2
#     yield 3
#     return "Finished"

# gen = numbers()

# print(next(gen))
# print(next(gen))
# print(next(gen))

# try:
#     next(gen)
# except StopIteration as error:
#     print(error.value)


# def numbers():
#     yield 1
#     yield 2
#     yield 3
#     return "numbers finsished"


# def main():
#     resault = yield from numbers()
#     print(resault)
#     yield "main finished"

# for value in main():
#     print(value)

# def fruits():
#     yield "appel"
#     yield "banana"
#     yield "orange"

# def vegetables():
#     yield "carrot"
#     yield "tomato"
#     yield "potato"

# def food():
#     yield from fruits()
#     yield from vegetables()


# for item in food():
#     print(item)


# def numbers():
#     c = 1
#     try:
#         while True:
#             yield c
#             c += 1
#     finally:
#         print("Generator cleanup")

# n = numbers()
# print(next(n))
# print(next(n))
# print(next(n))
# print(next(n))

# n.close()


# def worker():
#     number = 1

#     try:
#         while True:
#             try:
#                 yield number
#                 number += 1

#             except ValueError:
#                 print("Error handled")

#     finally:
#         print("Cleanup done")


# gen = worker()

# print(next(gen))
# print(next(gen))

# gen.throw(ValueError("Something went wrong"))

# gen.close()


# def resource_manager():
#     active = False
#     try:
#         value = yield active

#         while True:
#             if value == "start":
#                 active = True

#             elif value == "stop":
#                 active = False

#             elif value == "status":
#                 pass

#             value = yield active

#     finally:
#         print("Resource cleaned up")
    
# manager = resource_manager()

# next(manager)

# print(manager.send("start"))
# print(manager.send("status"))
# print(manager.send("stop"))
# print(manager.send("status"))

# manager.close()

# def numbers():
#     for n in range(1, 21):
#         yield n

# def processor(numbers):
#     for n in numbers:
#         if n % 2 == 0:
#             yield n * 10

# number_generator = numbers()
# processed_generator = processor(number_generator)


# for resault in processed_generator:
#     print(resault)


# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

# def products():
#     yield Product("laptop", 1200)
#     yield Product("mouse", 50)
#     yield Product("keyboard", 150)
#     yield Product("monitor", 300)
#     yield Product("phone", 800)

# def expensive_products(products):
#     for product in products:
#         if product.price > 100:
#             yield product

# def product_names(products):
#     for product in products:
#         yield product.name


# product_generator = products()
# expensive_generator = expensive_products(product_generator)
# name_generator = product_names(expensive_generator)

# for name in name_generator:
#     print(name)



# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

# def products():
#     yield Product("laptop", 1200)
#     yield Product("mouse", 50)
#     yield Product("keyboard", 150)
#     yield Product("monitor", 300)
#     yield Product("phone", 800)

# def expensive_products(products):
#     for product in products:
#         if product.price > 100:
#             yield product

# def discounted_products(products):
#     for product in products:
#         product.price = product.price * 0.80
#         yield product

# def product_info(products):
#     for product in products:
#         yield f"{product.name}: ${product.price}"

# p = products()
# expensive_products_generator = expensive_products(p)
# discounted_products_generator = discounted_products(expensive_products_generator)
# products_info_generator = product_info(discounted_products_generator)

# for p in products_info_generator:
#     print(p)





# class Product:
#     def __init__(self, name, price, category):
#         self.name = name
#         self.price = price
#         self.category = category

# def products():
#     yield Product("Laptop", 1200, "Electronics")
#     yield Product("Mouse", 50, "Electronics")
#     yield Product("Keyboard", 150, "Electronics")
#     yield Product("Chair", 200, "Furniture")
#     yield Product("Phone", 800, "Electronics")
#     yield Product("Table", 300, "Furniture")
#     yield Product("Pen", 10, "Office")

# def electronics(products):
#     for product in products:
#         if product.category == "Electronics":
#             yield product

# def expensive(products):
#     for product in products:
#         if product.price > 100:
#             yield product

# def product_info(products):
#     for product in products:
#         yield f"{product.name} {product.price} {product.category}"

# def total_price(products):
#     yield sum(product.price for product in products)

# p = products()
# e = electronics(p)
# ex = expensive(e)
# pi = product_info(ex)
# t = total_price(pi)

# for p in t:
#     print(p)

# def numbers():
#     yield 10
#     yield 20
#     yield 30
#     yield 40

# def running_average(numbers):
#     s = 0
#     t = 0
#     for n in numbers:
#         s += n
#         t += 1
#         yield s / t

# nbs = numbers()
# avg = running_average(nbs)

# for nb in avg:
#     print(nb)


# def calculator():
#     total = 0
#     command = yield total

#     while True:
#         action, amount = command

#         if action == "add":
#             total += amount

#         elif action == "subtract":
#             total -= amount

#         elif action == "reset":
#             total = 0

#         command = yield total


# calc = calculator()

# next(calc)

# print(calc.send(("add", 10)))
# print(calc.send(("add", 20)))
# print(calc.send(("subtract", 5)))
# print(calc.send(("add", 100)))
# print(calc.send(("reset", 0)))


# def inventory():
#     item = 0
#     command = yield item

#     while True:
#         action, amount = command

#         if action == "add":
#             item += amount

#         elif action == "remove":
#             item -= amount

#         elif action == "reset":
#             item = 0

#         command = yield item

# stock = inventory()

# next(stock)

# print(stock.send(("add", 10)))
# print(stock.send(("add", 5)))
# print(stock.send(("remove", 3)))
# print(stock.send(("add", 20)))
# print(stock.send(("remove", 7)))



# class DatabaseConnection:
#     def __enter__(self):
#         print("Database connected")
#         return self

#     def execute(self, query):
#         print(f"Executing: {query}")

#     def __exit__(self, exc_type, exc_value, traceback):
#         print("Database disconnected")

#         if exc_value is not None:
#             print(f"Error: {exc_value}")

#         return True


# with DatabaseConnection() as db:
#     db.execute("SELECT users")
#     raise ValueError("Database error")



# class FileManager:
#     def __init__(self, filename, mode):
#         self.filename = filename
#         self.mode = mode
#         self.file = None

#     def __enter__(self):
#         self.file = open(self.filename, self.mode)
#         return self.file

#     def __exit__(self, exc_type, exc_value, traceback):
#         self.file.close()


# with FileManager("test.txt", "w") as file:
#     file.write("Hello Python!")

# print(file.closed)



# import time


# class Timer:
#     def __enter__(self):
#         self.start = time.perf_counter()
#         return self

#     def __exit__(self, exc_type, exc_value, traceback):
#         end = time.perf_counter()
#         duration = end - self.start

#         print(f"Execution time: {duration:.6f} seconds")


# with Timer():
#     total = 0

#     for number in range(1_000_000):
#         total += number

# print(total)


# from contextlib import contextmanager

# @contextmanager
# def connection():
#     print("connected")
#     yield
#     print("disconnected")

# with connection():
#     print("somthing inside")



# from contextlib import contextmanager

# @contextmanager
# def database():
#     print("database connected")

#     var = "MyDatabase"
#     yield var

#     print("database disconnected")

# with database() as db:
#     print(db)



# from contextlib import contextmanager


# @contextmanager
# def database():
#     print("Database connected")

#     try:
#         db = "MyDatabase"
#         yield db

#     except ValueError as error:
#         print(f"Error: {error}")

#     finally:
#         print("Database disconnected")


# with database() as db:
#     print(db)
#     raise ValueError("Connection failed")



# from contextlib import contextmanager

# @contextmanager
# def database():
#     print("database connected")

#     var = "MyDatabase"
#     yield var

#     print("database disconnected")

# @contextmanager
# def file_manager():
#     print("file opened")

#     var = "MyFile"
#     yield var

#     print("file closed")


# with database() as db:
#     with file_manager() as file:
#         print(db)
#         print(file)


# from contextlib import contextmanager


# @contextmanager
# def transaction():
#     print("Transaction started")

#     try:
#         yield "Transaction"

#     except ValueError as error:
#         print(f"Transaction rolled back: {error}")

#     else:
#         print("Transaction committed")

#     finally:
#         print("Transaction closed")


# print("Successful transaction:")

# with transaction() as tx:
#     print(tx)


# print("\nFailed transaction:")

# with transaction() as tx:
#     print(tx)
#     raise ValueError("Something went wrong")


# from dataclasses import dataclass


# @dataclass
# class Product:
#     name: str
#     price: float
#     category: str


# product = Product("Laptop", 1200, "Electronics")

# print(product)

# product2 = Product("Laptop", 1200, "Electronics")

# print(product == product2)



# from dataclasses import dataclass

# @dataclass
# class User:
#     name: str
#     age: int
#     active: bool = True

# user1 = User("Hunter", 25)
# user2 = User("John", 30, False)

# print(user1)
# print(user2)


# from dataclasses import dataclass, field

# @dataclass
# class Product:
#     name: str
#     price: float
#     tags: list = field(default_factory=list)

# product1 = Product("Laptop", 1200)
# product2 = Product("Mouse", 50)

# product1.tags.append("electronics")

# print(product1)
# print(product2)


# from dataclasses import dataclass


# @dataclass
# class Product:
#     name: str
#     price: float
#     price_with_tax: float = 0

#     def __post_init__(self):
#         self.price_with_tax = self.price * 1.20


# product = Product("Laptop", 1000)

# print(product)

# from dataclasses import dataclass

# @dataclass
# class BankAccount:
#     owner: str
#     balance: float

#     def __post_init__(self):
#         if self.balance < 0:
#             raise ValueError("Balance cannot be negative")

# account1 = BankAccount("Hunter", 1000)
# print(account1)
# account2 = BankAccount("John", -500)


# from dataclasses import dataclass


# @dataclass(frozen=True)
# class User:
#     name: str
#     age: int


# user = User("Hunter", 25)

# print(user)
# print(user.name)
# print(user.age)

# user.age = 26


# from dataclasses import dataclass


# @dataclass(frozen=True)
# class Product:
#     name: str
#     price: float


# product = Product("Laptop", 1200)

# products = {product}

# print(products)

# product2 = Product("Laptop", 1200)

# print(product == product2)
# print(product2 in products)



# from dataclasses import dataclass


# @dataclass(frozen=True)
# class Product:
#     name: str
#     price: float


# product = Product("Laptop", 1200)

# products = {product}

# print(products)

# product2 = Product("Laptop", 1200)

# print(product == product2)
# print(product2 in products)



# from dataclasses import dataclass


# @dataclass(order=True)
# class Product:
#     name: str
#     price: float


# product1 = Product("Laptop", 1200)
# product2 = Product("Mouse", 50)

# print(product1 < product2)
# print(product2 < product1)

# products = [product1, product2]

# products.sort()

# print(products)



# from dataclasses import dataclass, field


# @dataclass(order=True)
# class Product:
#     price: float
#     name: str = field(compare=False)
#     stock: int = field(compare=False)


# product1 = Product(1200, "Laptop", 10)
# product2 = Product(50, "Mouse", 100)

# print(product1 > product2)

# products = [product1, product2]
# products.sort()

# print(products)







# def calculate_total(prices: list[int | float]) -> int | float:
#     return sum(prices)

# print(calculate_total([10, 20, 30]))



# def get_user_ages(users: dict[str, int]) -> list[int]:
#     return list(users.values())


# users = {
#     "Alice": 25,
#     "Bob": 30,
#     "John": 22
# }

# print(get_user_ages(users))


# def find_user(users: dict[str, int], name: str) -> int | None:
#     if name in users:
#         return users[name]

#     return None


# users = {
#     "Alice": 25,
#     "Bob": 30
# }

# print(find_user(users, "Alice"))
# print(find_user(users, "John"))


# def find_user(users: dict[str, int], age: int) -> str | None:
#     for name, user_age in users.items():
#         if user_age == age:
#             return name

#     return None


# users = {
#     "Alice": 25,
#     "Bob": 30
# }

# print(find_user(users, 25))  # Alice
# print(find_user(users, 30))  # Bob


# def find_product(products: dict[int, str], product_id: int) -> str | None:
#     if product_id in products:
#         return products[product_id]

# products = {
#     101: "Laptop",
#     102: "Mouse",
#     103: "Keyboard"
# }

# print(find_product(products, 102))
# print(find_product(products, 999))


# def get_user_info(user: tuple[str, int, bool]) -> tuple[str, int, bool]:
#     return user


# user = ("Hunter", 25, True)

# print(get_user_info(user))


# def calculate_average(numbers: tuple[int | float, ...]) -> float:
#     return sum(numbers) / len(numbers)

# numbers = (10, 20, 30, 40)

# print(calculate_average(numbers))


# from typing import Any


# def create_user(**info: Any) -> dict[str, Any]:
#     return info


# user = create_user(
#     name="Hunter",
#     age=25,
#     active=True
# )

# print(user)

# def calculate_sum(*numbers: int | float) -> float:
#     return sum(numbers)


# print(calculate_sum(10, 20, 5.5))



# from collections.abc import Callable


# def apply_operation(
#     operation: Callable[[int, int], int],
#     a: int,
#     b: int
# ) -> int:
#     return operation(a, b)


# def multiply(a, b):
#     return a * b


# result = apply_operation(multiply, 5, 4)

# print(result)



# from collections.abc import Callable

# def execute(operation: callable[[str], str], a: str) -> str:
#     return operation(a)

# def f(a):
#     return a.upper()


# print(execute(f, "python"))




# from collections.abc import Callable

# def apply_to_numbers(operation: Callable[[int], int], *numbers: int) -> list[int]:
#     return [operation(number) for number in numbers]


# def double(number):
#     return number * 2


# print(apply_to_numbers(double, 1, 2, 3, 4))


# from typing import TypeVar

# T = TypeVar("T")


# def get_first(items: list[T]) -> T:
#     return items[0]


# print(get_first([10, 20, 30]))
# print(get_first(["Python", "Java", "C++"]))


# from typing import TypeVar

# T = TypeVar("T")

# def first_or_second(first: T, second: T, use_first: bool) -> T:
#     if use_first == True:
#         return first
#     return second

# print(first_or_second(10, 20, True))
# print(first_or_second("Hello", "World", False))



# from typing import Generic, TypeVar

# T = TypeVar("T")


# class Box(Generic[T]):
#     def __init__(self, value: T):
#         self.value = value

#     def get_value(self) -> T:
#         return self.value


# box1 = Box(100)
# box2 = Box("Python")

# print(box1.get_value())
# print(box2.get_value())


# from typing import Generic, TypeVar

# T = TypeVar("T")
# U = TypeVar("U")

# class Pair(Generic[T, U]):
#     def __init__(self, a: T, b: U):
#         self.a = a
#         self.b = b

#     def get_first(self) -> T:
#         return self.a
    
#     def get_second(self) -> U:
#         return self.b


# pair1 = Pair("Hunter", 25)
# pair2 = Pair(100, True)

# print(pair1.get_first())
# print(pair1.get_second())

# print(pair2.get_first())
# print(pair2.get_second())


# from typing import Generic, TypeVar

# T = TypeVar("T")

# class Storage(Generic[T]):
#     def __init__(self):
#         self.items: list[T] = []

#     def add(self, item: T) -> None:
#         self.items.append(item)

#     def get_all(self) -> list[T]:
#         return self.items

# numbers = Storage()

# numbers.add(10)
# numbers.add(20)
# numbers.add(30)

# words = Storage()

# words.add("Python")
# words.add("Java")

# print(numbers.get_all())
# print(words.get_all())

# from typing import Generic, TypeVar

# T = TypeVar("T")

# class Storage(Generic[T]):
#     def __init__(self):
#         self.items: list[T]= []

#     def add(self, value: T) -> None:
#         self.items.append(value)

#     def get(self, index: int) -> T:
#         return self.items[index]

#     def get_all(self) -> list[T]:
#         return self.items

# numbers = Storage[int]()

# numbers.add(10)
# numbers.add(20)
# numbers.add(30)

# print(numbers.get(1))
# print(numbers.get_all())


# from typing import TypeVar

# T = TypeVar("T")
# U = TypeVar("U")

# def make_pair(first: T, second: U) -> tuple[T, U]:
#     return (first, second)

# print(make_pair("Hunter", 25))
# print(make_pair(100, True))


# from typing import TypeVar

# T = TypeVar("T", int, float)

# def double_value(value: T) -> T:
#     return value * 2

# print(double_value(10))
# print(double_value(2.5))



# from typing import Protocol


# class HasLength(Protocol):
#     def __len__(self) -> int:
#         ...


# def get_length(value: HasLength) -> int:
#     return len(value)


# print(get_length("Python"))
# print(get_length([1, 2, 3]))
# print(get_length((10, 20)))



# from typing import Protocol


# class Printable(Protocol):
#     def display(self) -> str:
#         ...


# class User:
#     def __init__(self, name: str):
#         self.name = name

#     def display(self) -> str:
#         return f"User: {self.name}"


# class Product:
#     def __init__(self, name: str):
#         self.name = name

#     def display(self) -> str:
#         return f"Product: {self.name}"


# def show(item: Printable) -> None:
#     print(item.display())


# user = User("Hunter")
# product = Product("Laptop")

# show(user)
# show(product)


# from typing import Protocol


# class HasName(Protocol):
#     name: str


# class User:
#     def __init__(self, name: str):
#         self.name = name


# class Product:
#     def __init__(self, name: str):
#         self.name = name


# def print_name(item: HasName) -> None:
#     print(f"Name: {item.name}")


# user = User("Hunter")
# product = Product("Laptop")

# print_name(user)
# print_name(product)


# from typing import Protocol


# class UserLike(Protocol):
#     name: str

#     def get_email(self) -> str:
#         ...


# class Admin:
#     def __init__(self, name: str, email: str):
#         self.name = name
#         self.email = email

#     def get_email(self) -> str:
#         return self.email


# class Customer:
#     def __init__(self, name: str, email: str):
#         self.name = name
#         self.email = email

#     def get_email(self) -> str:
#         return self.email


# def show_user(user: UserLike) -> None:
#     print(f"Name: {user.name}")
#     print(f"Email: {user.get_email()}")


# admin = Admin("Hunter", "hunter@example.com")
# customer = Customer("Alice", "alice@example.com")

# show_user(admin)
# show_user(customer)




# from typing import Protocol, runtime_checkable


# @runtime_checkable
# class Playable(Protocol):
#     name: str

#     def play(self) -> None:
#         ...


# class VideoGame:
#     def __init__(self, name: str):
#         self.name = name

#     def play(self) -> None:
#         print(f"Playing {self.name}")


# class Music:
#     def __init__(self, name: str):
#         self.name = name

#     def play(self) -> None:
#         print(f"Playing {self.name}")


# class Book:
#     def __init__(self, name: str):
#         self.name = name


# def check_playable(item: object) -> None:
#     if isinstance(item, Playable):
#         print(f"{item.name} is playable")
#     else:
#         print(f"{item.name} is not playable")


# game = VideoGame("Minecraft")
# music = Music("Music")
# book = Book("Python Book")

# check_playable(game)
# check_playable(music)
# check_playable(book)


# from typing import Protocol, runtime_checkable


# @runtime_checkable
# class Worker(Protocol):
#     name: str

#     def work(self) -> str:
#         ...

#     def get_salary(self) -> float:
#         ...


# class Developer:
#     def __init__(self, name: str, salary: float):
#         self.name = name
#         self.salary = salary

#     def work(self) -> str:
#         return "Writing code"

#     def get_salary(self) -> float:
#         return self.salary


# class Designer:
#     def __init__(self, name: str, salary: float):
#         self.name = name
#         self.salary = salary

#     def work(self) -> str:
#         return "Designing UI"

#     def get_salary(self) -> float:
#         return self.salary


# class Student:
#     def __init__(self, name: str):
#         self.name = name

#     def work(self) -> str:
#         return "Studying"


# def check_worker(person: object) -> None:
#     if isinstance(person, Worker):
#         print(f"{person.name} is a worker")
#         print(f"Work: {person.work()}")
#         print(f"Salary: {person.get_salary()}")
#     else:
#         print(f"{person.name} is not a worker")


# developer = Developer("Hunter", 2000.0)
# designer = Designer("Sarah", 1800.0)
# student = Student("Alex")

# check_worker(developer)
# print()

# check_worker(designer)
# print()

# check_worker(student)


# from typing import Protocol, runtime_checkable

# @runtime_checkable
# class Payable(Protocol):
#     name: str

#     def pay() -> float:
#         ...


# class Employee:
#     def __init__ (self, name: str,
#     salary: float):
#          self.name = name
#          self.salary = salary

#     def pay(self) -> float:
#         return self.salary


# class Freelancer:
#     def __init__ (self, name: str,
#     amount: float):
#             self.name = name
#             self.amount = amount

#     def pay(self) -> float:
#         return self.amount

# class Student:
#     def __init__(self, name: str):
#         self.name = name


# def process_payment(person: object) -> None:
#     if isinstance(person, Protocol):
#         print(f"{person.name} will recive {person.pay()}")
#     else:
#         print(f"{person.name} cannot recive payment")



# employee = Employee("Hunter", 2500.0)
# freelancer = Freelancer("Sarah", 1800.0)
# student = Student("Alex")

# process_payment(employee)
# process_payment(freelancer)
# process_payment(student)


# from typing import TypedDict

# class ProductData(TypedDict):
#     name: str
#     price: float
#     stock: int


# def show_product(product: ProductData) -> None:
#     print(f"Product: {product["name"]}")
#     print(f"Price: {product["price"]}")
#     print(f"Stock: {product["stock"]}")


# product1: ProductData = {
#     "name": "Laptop",
#     "price": 1200.0,
#     "stock": 5
# }

# product2: ProductData = {
#     "name": "Keyboard",
#     "price": 80.0,
#     "stock": 20
# }


# show_product(product1)
# print()
# show_product(product2)


# from typing import TypedDict, NotRequired

# class UserData(TypedDict):
#     name: str
#     email: str
#     age: int
#     phone: NotRequired[str]


# def show_user(user: UserData) -> None:
#     print(f"name: {user["name"]}")
#     print(f"email: {user["email"]}")
#     print(f"age: {user["age"]}")

#     if "phone" in user:
#         print(f"Phone: {user['phone']}")


# user1: UserData = {
#     "name": "Hunter",
#     "email": "hunter@example.com",
#     "age": 25,
#     "phone": "0550123456"
# }

# user2: UserData = {
#     "name": "Alice",
#     "email": "alice@example.com",
#     "age": 30
# }


# show_user(user1)

# print()

# show_user(user2)


# from typing import TypedDict, Required, NotRequired

# class ProductData(TypedDict):
#     id: Required[int]
#     name: Required[str]
#     price: Required[float]
#     description: NotRequired[str]
#     discount: NotRequired[float]

# def show_product(product: ProductData) -> None:
#     print(f"{product["id"]}")
#     print(f"{product["name"]}")
#     print(f"{product["price"]}")

#     if "description" in product:
#         print(f"{product["description"]}")

#     if "discount" in product:
#         print(f"{product["discount"]}")


# product1: ProductData = {
#     "id": 1,
#     "name": "Laptop",
#     "price": 1200.0,
#     "description": "Gaming laptop",
#     "discount": 10.0
# }

# product2: ProductData = {
#     "id": 2,
#     "name": "Keyboard",
#     "price": 80.0
# }


# show_product(product1)

# print()

# show_product(product2)


# from typing import TypedDict, NotRequired


# class Address(TypedDict):
#     city: str
#     country: str
#     zip_code: NotRequired[str]


# class UserData(TypedDict):
#     name: str
#     email: str
#     address: Address


# def show_user(user: UserData) -> None:
#     print(f"Name: {user['name']}")
#     print(f"Email: {user['email']}")
#     print(f"City: {user['address']['city']}")
#     print(f"Country: {user['address']['country']}")

#     if "zip_code" in user["address"]:
#         print(f"Zip code: {user['address']['zip_code']}")


# user1: UserData = {
#     "name": "Hunter",
#     "email": "hunter@example.com",
#     "address": {
#         "city": "Algiers",
#         "country": "Algeria",
#         "zip_code": "16000"
#     }
# }


# user2: UserData = {
#     "name": "Alice",
#     "email": "alice@example.com",
#     "address": {
#         "city": "Oran",
#         "country": "Algeria"
#     }
# }


# show_user(user1)

# print()

# show_user(user2)

# from typing import TypedDict, Required, NotRequired

# class Product(TypedDict):
#     name: Required[str]
#     price: Required[float]
#     discount: NotRequired[float]


# class OrderItem(TypedDict):
#     product: Required[Product]
#     quantity: Required[int]


# class Order(TypedDict):
#     order_id: Required[int]
#     customer: Required[str]
#     items: Required[list[OrderItem]]


# def show_order(order: Order) -> None:


# from typing import TypedDict, NotRequired


# class Product(TypedDict):
#     name: str
#     price: float
#     discount: NotRequired[float]


# class OrderItem(TypedDict):
#     product: Product
#     quantity: int


# class Order(TypedDict):
#     order_id: int
#     customer: str
#     items: list[OrderItem]


# def show_order(order: Order) -> None:
#     print(f"Order ID: {order['order_id']}")
#     print(f"Customer: {order['customer']}")

#     print("Items:")

#     for item in order["items"]:
#         product = item["product"]

#         print(f"  Product: {product['name']}")
#         print(f"  Price: {product['price']}")
#         print(f"  Quantity: {item['quantity']}")

#         if "discount" in product:
#             print(f"  Discount: {product['discount']}")

#         print()


# order: Order = {
#     "order_id": 1001,
#     "customer": "Hunter",
#     "items": [
#         {
#             "product": {
#                 "name": "Laptop",
#                 "price": 1200.0,
#                 "discount": 10.0
#             },
#             "quantity": 1
#         },
#         {
#             "product": {
#                 "name": "Keyboard",
#                 "price": 80.0
#             },
#             "quantity": 2
#         }
#     ]
# }


# show_order(order)



# from typing import Literal


# def set_status(status: Literal["online", "offline", "away"]) -> None:
#     if status == "online":
#         print("User is online")
#     elif status == "offline":
#         print("User is offline")
#     elif status == "away":
#         print("User is away")


# set_status("online")
# set_status("offline")
# set_status("away")


# status: Literal["online", "offline", "away"] = "online"

# set_status(status)




# from typing import TypedDict, Literal


# class Task(TypedDict):
#     title: str
#     status: Literal["pending", "completed", "cancelled"]
#     priority: Literal["low", "medium", "high"]


# def show_task(task: Task) -> None:
#     print(f"Title: {task['title']}")
#     print(f"Status: {task['status']}")
#     print(f"Priority: {task['priority']}")

#     if task["status"] == "pending":
#         print("Task is waiting")
#     elif task["status"] == "completed":
#         print("Task is finished")
#     elif task["status"] == "cancelled":
#         print("Task was cancelled")


# task1: Task = {
#     "title": "Learn Python",
#     "status": "pending",
#     "priority": "high"
# }

# task2: Task = {
#     "title": "Finish project",
#     "status": "completed",
#     "priority": "medium"
# }


# show_task(task1)

# print()

# show_task(task2)


# from typing import TypedDict, Literal


# class Order(TypedDict):
#     id: int
#     customer: str
#     status: Literal["pending", "shipped", "delivered", "cancelled"]


# def process_order(order: Order) -> None:
#     print(f"Order #{order['id']}")
#     print(f"Customer: {order['customer']}")

#     if order["status"] == "pending":
#         print("Order is being processed")

#     elif order["status"] == "shipped":
#         print("Order has been shipped")

#     elif order["status"] == "delivered":
#         print("Order has been delivered")

#     elif order["status"] == "cancelled":
#         print("Order was cancelled")


# order1: Order = {
#     "id": 1001,
#     "customer": "Hunter",
#     "status": "pending"
# }

# order2: Order = {
#     "id": 1002,
#     "customer": "Alice",
#     "status": "shipped"
# }

# order3: Order = {
#     "id": 1003,
#     "customer": "Bob",
#     "status": "delivered"
# }


# process_order(order1)

# print()

# process_order(order2)

# print()

# process_order(order3)

# from typing import Literal


# def get_message(
#     status: Literal["success", "error", "warning"]
# ) -> str:

#     if status == "success":
#         return "Operation completed successfully"

#     elif status == "error":
#         return "Something went wrong"

#     elif status == "warning":
#         return "Be careful"


# print(get_message("success"))
# print(get_message("error"))
# print(get_message("warning"))


# from typing import Final


# MAX_USERS: Final[int] = 100
# APP_NAME: Final[str] = "MyApp"


# def show_limit() -> None:
#     print(f"Maximum users: {MAX_USERS}")
#     print(f"App name: {APP_NAME}")


# show_limit()



# from typing import Final


# class GameConfig:
#     MAX_PLAYERS: Final[int] = 4
#     GAME_NAME: Final[str] = "DMZ"

#     def show_config(self) -> None:
#         print(f"Maximum players: {self.MAX_PLAYERS}")
#         print(f"Game name: {self.GAME_NAME}")


# game = GameConfig()

# game.show_config()

# print(game.MAX_PLAYERS)
# print(game.GAME_NAME)


# from typing import Self


# class User:
#     def __init__(self, name: str):
#         self.name = name

#     def rename(self, new_name: str) -> Self:
#         self.name = new_name
#         return self


# class Admin(User):
#     def promote(self) -> Self:
#         print("User promoted to admin")
#         return self


# admin = Admin("Hunter")

# admin.rename("Alex").promote()

# print(admin.name)


# from typing import Self

# class Character:
#     def __init__(self, name: str):
#         self.name = name
#         self.level = 1
#         self.health = 100

#     def set_level(self, level: int) -> Self:
#         self.level = level
#         return self

#     def set_health(self, health: int) -> Self:
#         self.health = health
#         return self

#     def show(self) ->None:
#         print(f"name: {self.name}, level: {self.level}, health: {self.health}")

# char1 = Character("Hunter")

# char1.set_level(10).set_health(250).show()



# from typing import TypeAlias


# ProductID: TypeAlias = int


# def get_product(product_id: ProductID) -> str:
#     return f"Product #{product_id}"


# product_id: ProductID = 25

# print(get_product(product_id))


# from typing import TypeAlias

# UserData: TypeAlias = dict[str, str | int | bool]

# def show_user(user: UserData) -> None:
#     print(f"name: {user["name"]}")
#     print(f"age: {user["age"]}")
#     print(f"status: {user["active"]}")


# user: UserData = {
#     "name": "Hunter",
#     "age": 25,
#     "active": True
# }

# show_user(user)




# from typing import TypeAlias


# Position: TypeAlias = tuple[float, float]


# def move(position: Position, x: float, y: float) -> Position:
#     new_x = position[0] + x
#     new_y = position[1] + y

#     return (new_x, new_y)


# position: Position = (100.0, 50.0)

# new_position = move(position, 20.0, 10.0)

# print(new_position)



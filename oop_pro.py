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


class BankAccount:
    def __init__(self, owner, balance, account_type):
        self.owner = owner
        self.balance = balance
        self.account_type = account_type

    def show_info(self):
        print(f"Owner: {self.owner}")
        print(f"Balance: ${self.balance}")
        print(f"Type: {self.account_type}")

    @classmethod
    def create_savings(cls, owner, initial_balance):
        return cls(owner, initial_balance, "Savings")

    @classmethod
    def from_string(cls, data):
        owner, balance, account_type = data.split(",")

        return cls(owner, float(balance), account_type)


# Normal creation
account1 = BankAccount("Hunter", 1000, "Checking")

# Using class method
account2 = BankAccount.create_savings("Hunter", 500)

# Using class method with a string
account3 = BankAccount.from_string(
    "Alex,2500,Checking"
)

account1.show_info()

print()

account2.show_info()

print()

account3.show_info()
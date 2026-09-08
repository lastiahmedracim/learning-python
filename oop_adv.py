# def main():
#     while True:
#         print("1. print hello")
#         print("2. exit")

#         choice = input("chose option: ")

#         if choice == "1":
#             print("hello world")
#         elif choice == "2":
#             print("goodbye")
#             break
#         else:
#             print("invalid choice")

# if __name__=="__main__":
#     main()


# def main():
#     numbers = []

#     while True:

#         print("\n---numbermanager--")
#         print("1. add number")
#         print("2. show number")
#         print("3. total number")
#         print("4. exit")

#         choice = input("chose option: \n")

#         if choice == "1":
#             try:
#                 n = int(input("add number"))
#                 numbers.append(n)
#                 print("number added succesfully")
#             except ValueError:
#                 print("invalid number")

#         elif choice == "2":
#             print("numbers: ")
#             for n in numbers:
#                 print(n)
#         elif choice == "3":
#             s = sum(numbers)
#             print(f'total number: {s}')

#         elif choice == "4":
#             print("goodbye")
#             break

#         else:
#             print("invalid option")

# if __name__ == "__main__":
#     main()


# def main():
#     expenses = []

#     while True:
#         print("\n--- Expense Tracker ---")
#         print("1. Add expense")
#         print("2. Show expenses")
#         print("3. Show total")
#         print("4. Show most expensive")
#         print("5. Exit")

#         choice = input("Choose an option: ")

#         if choice == "1":
#             name = input("Expense name: ")

#             try:
#                 amount = float(input("Expense amount: "))

#                 expense = [name, amount]
#                 expenses.append(expense)

#                 print("Expense added.")

#             except ValueError:
#                 print("Invalid amount.")

#         elif choice == "2":
#             if not expenses:
#                 print("No expenses yet.")
#             else:
#                 print("\nExpenses:")

#                 for expense in expenses:
#                     name = expense[0]
#                     amount = expense[1]

#                     print(f"{name} - {amount}")

#         elif choice == "3":
#             if not expenses:
#                 print("No expenses yet.")
#             else:
#                 total = 0

#                 for expense in expenses:
#                     total += expense[1]

#                 print(f"Total: {total}")

#         elif choice == "4":
#             if not expenses:
#                 print("No expenses yet.")
#             else:
#                 most_expensive = expenses[0]

#                 for expense in expenses:
#                     if expense[1] > most_expensive[1]:
#                         most_expensive = expense

#                 print(
#                     f"Most expensive: "
#                     f"{most_expensive[0]} - {most_expensive[1]}"
#                 )

#         elif choice == "5":
#             print("Goodbye!")
#             break

#         else:
#             print("Invalid option.")


# if __name__ == "__main__":
#     main()


# class User:
#     def __init__(self, username, age):
#         self.username = username
#         self.age = age

#     @property
#     def age(self):
#         return self._age

#     @age.setter
#     def age(self, value):
#         if value < 0 or value > 120:
#             print("Invalid age")
#             return

#         self._age = value


# user = User("Alex", 25)

# print(user.age)

# user.age = 30
# print(user.age)

# user.age = 200


# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     @property
#     def age(self):
#         return self._age

#     @age.setter
#     def age(self, new_age):
#         if new_age < 0 or new_age > 100:
#             print("Invalid age")
#         else:
#             self._age = new_age

#     def add_info(self, name, age):
#         self.name = name
#         self.age = age
#         print("Student information added.")

#     def remove_info(self):
#         self.name = ""
#         self._age = None
#         print("Student information removed.")

#     def show_info(self):
#         if self.name == "" or self._age is None:
#             print("No student information.")
#         else:
#             print(f"Name: {self.name}")
#             print(f"Age: {self.age}")


# def main():
#     student = Student("", 0)

#     while True:
#         print("\n1. Add info")
#         print("2. Remove info")
#         print("3. Show info")
#         print("4. Quit")

#         choice = input("Choose an option: ")

#         if choice == "1":
#             name = input("Enter student name: ")

#             try:
#                 age = int(input("Enter student age: "))
#                 student.add_info(name, age)
#             except ValueError:
#                 print("Please enter a valid number for the age.")

#         elif choice == "2":
#             student.remove_info()

#         elif choice == "3":
#             student.show_info()

#         elif choice == "4":
#             print("Goodbye!")
#             break

#         else:
#             print("Invalid option.")


# if __name__ == "__main__":
#     main()


# class Book:
#     def __init__(self, title, author, price, available):
#         self.title = title
#         self.author = author
#         self.price = price
#         self.available = available

#     @property
#     def price(self):
#         return self._price

#     @price.setter
#     def price(self, value):
#         if value < 0:
#             print("Invalid price")
#         else:
#             self._price = value

#     def borrow_book(self):
#         if self.available:
#             self.available = False
#             print("Book borrowed successfully.")
#         else:
#             print("Book is not available.")

#     def return_book(self):
#         if not self.available:
#             self.available = True
#             print("Book returned successfully.")
#         else:
#             print("Book is already available.")

#     def show_info(self):
#         print(f"Title: {self.title}")
#         print(f"Author: {self.author}")
#         print(f"Price: {self.price}")
#         print(f"Available: {'Yes' if self.available else 'No'}")


# def main():

#     book = Book("Harry Potter", "J.K. Rowling", 20, True)

#     while True:
#         print("\n1. Borrow book")
#         print("2. Return book")
#         print("3. Show book information")
#         print("4. Change price")
#         print("5. Quit")

#         choice = input("Choose an option: ")

#         if choice == "1":
#             book.borrow_book()

#         elif choice == "2":
#             book.return_book()

#         elif choice == "3":
#             book.show_info()

#         elif choice == "4":
#             try:
#                 new_price = float(input("Enter new price: "))
#                 book.price = new_price
#             except ValueError:
#                 print("Please enter a valid number.")

#         elif choice == "5":
#             print("Goodbye!")
#             break

#         else:
#             print("Invalid option.")


# if __name__ == "__main__":
#     main()



# class Employee:
#     def __init__(self, name, job, salary, active):
#         self.name = name
#         self.job = job
#         self.salary = salary
#         self.active = active

#     @property
#     def salary(self):
#         return self._salary

#     @salary.setter
#     def salary(self, salary):
#         if salary < 0:
#             return print("invalid salary")
#         self._salary = salary
#         return print(f"salary = {self._salary}")

#     def give_raise(self, amount):
#         if amount <= 0:
#             return print("invalid raise")
#         self.salary += amount
#         return print(f"raise = {amount}\nnew salary {self.salary}")

#     def deactivate(self, name):
#         if self.name == name:
#             if self.active == True:
#                 self.active = False
#                 return print("Employee deactivated successfully")
#             return print("employee already deactivated")
#         return print("invalid employee name")

#     def activate(self, name):
#         if self.name == name:
#             if self.active == False:
#                 self.active = True
#                 return print("Employee activated successfully")
#             return print("employee already activated")
#         return print("invalid employee name")

#     def show_info(self):
#         print(f"name : {self.name}")
#         print(f"job : {self.job}")
#         print(f"salary : {self.salary}")
#         print(f"active : {self.active}")


# def main():

#     employee = Employee("Alice", "Developer", 3000, True)

#     while True:

#         print("1. give raise")
#         print("2. deactivate employee")
#         print("3. activate employee")
#         print("4. show employee info")
#         print("5. change salary")
#         print("6. quit")

#         choice = input("choose option: ")

#         if choice == "1":
#             try:
#                 amount = int(input("enter raise amount: "))
#                 employee.give_raise(amount)
#             except ValueError:
#                 print("invalid raise number")

#         elif choice == "2":
#             name = input("enter employee name: ")
#             employee.deactivate(name)

#         elif choice == "3":
#             name = input("enter employee name: ")
#             employee.activate(name)

#         elif choice == "4":
#             employee.show_info()

#         elif choice == "5":
#             try:
#                 new_salary = int(input("enter new salary: "))
#                 employee.salary = new_salary
#             except ValueError:
#                 print("invalid salary number")

#         elif choice == "6":
#             print("goodbye")
#             break

#         else:
#             print("invalid option")


# if __name__ == "__main__":
#     main()


# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"{self.name}, {self.age} years old"


# class Course:
#     def __init__(self, name):
#         self.name = name
#         self.students = []

#     def add_student(self, student):
#         self.students.append(student)

#     def remove_student(self, student):
#         self.students.remove(student)

#     def show_students(self):
#         print(f"Students in {self.name}:")
#         for student in self.students:
#             print(student)

#     def find_student(self, name):
#         for student in self.students:
#             if student.name == name:
#                 print(f"Student found: {student}")
#                 return

#         print("Student not found")

#     def __str__(self):
#         result = f"Course: {self.name}\nStudents:"

#         for student in self.students:
#             result += f"\n- {student}"

#         return result


# # Create students
# student1 = Student("Alice", 20)
# student2 = Student("John", 22)
# student3 = Student("Sarah", 19)

# # Create course
# course = Course("Python")

# # Add students
# course.add_student(student1)
# course.add_student(student2)
# course.add_student(student3)

# # Show course
# print(course)

# print()

# # Find student
# course.find_student("Sarah")

# print()

# # Remove Alice
# course.remove_student(student1)

# # Show course again
# print(course)


# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.grades = []

#     def __str__(self):
#         return f"{self.name}, {self.age} years old"

#     def add_grade(self, grade):
#         self.grades.append(grade)

#     def show_grades(self):
#         print(f"{self.name}'s grades:")
#         for grade in self.grades:
#             print(grade)

#     def average_grade(self):
#         return sum(self.grades) / len(self.grades)

#     def is_passing(self):
#         return self.average_grade() >= 10

#     def highest_grade(self):
#         return max(self.grades)


# # Create students
# student1 = Student("Alice", 20)
# student2 = Student("John", 22)
# student3 = Student("Sarah", 19)

# # Add grades
# student1.add_grade(15)
# student1.add_grade(18)
# student1.add_grade(12)

# student2.add_grade(8)
# student2.add_grade(11)
# student2.add_grade(9)

# student3.add_grade(17)
# student3.add_grade(16)
# student3.add_grade(19)


# # Show Alice
# student1.show_grades()
# print("Average:", student1.average_grade())
# print("Passing:", student1.is_passing())
# print("Highest:", student1.highest_grade())

# print()

# # Show John
# student2.show_grades()
# print("Average:", student2.average_grade())
# print("Passing:", student2.is_passing())
# print("Highest:", student2.highest_grade())

# print()

# # Show Sarah
# student3.show_grades()
# print("Average:", student3.average_grade())
# print("Passing:", student3.is_passing())
# print("Highest:", student3.highest_grade())


# class Wallet:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance

#     def __str__(self):
#         return f"wallet of {self.owner}: ${self.balance}"

#     def deposit(self, amount):
#         self.balance += amount

#     def withdrow(self, amount):
#         if self.balance < amount:
#             return f"not enough money"
#         else:
#             self.balance -= amount

# class Person:
#     def __init__(self, name, wallet):
#         self.name = name
#         self.wallet = wallet

#     def __str__(self):
#         return f"{self.name}\n{self.wallet}"

#     def add_money(self, amount):
#         self.wallet.deposit(amount)

#     def spend_money(self, amount):
#         self.wallet.withdrow(amount)

# wallet = Wallet("Ahmed", 100)

# # Put the Wallet object inside Person
# person = Person("Ahmed", wallet)

# print(person)

# print()

# person.add_money(50)
# print(person)

# print()

# person.spend_money(30)
# print(person)

# print()

# person.spend_money(200)


# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance

#     def __str__(self):
#         return f"{self.owner} - ${self.balance}"

#     def deposit(self, amount):
#         self.balance += amount

#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Not enough money")
#         else:
#             self.balance -= amount


# class Person:
#     def __init__(self, name, account):
#         self.name = name
#         self.account = account

#     def __str__(self):
#         return f"Name: {self.name}\nAccount: {self.account}"

#     def add_money(self, amount):
#         self.account.deposit(amount)

#     def spend_money(self, amount):
#         self.account.withdraw(amount)


# class Bank:
#     def __init__(self, name):
#         self.name = name
#         self.accounts = []

#     def add_account(self, account):
#         self.accounts.append(account)

#     def show_accounts(self):
#         for account in self.accounts:
#             print(account)


# # Create the bank
# bank = Bank("Algeria Bank")

# # Create Ahmed's account
# ahmed_account = BankAccount("Ahmed", 500)

# # Create Ahmed
# ahmed = Person("Ahmed", ahmed_account)

# # Add Ahmed's account to the bank
# bank.add_account(ahmed_account)

# # Create Ali's account
# ali_account = BankAccount("Ali", 1000)

# # Add Ali's account to the bank
# bank.add_account(ali_account)

# # Show accounts
# bank.show_accounts()

# print()

# # Ahmed deposits 200
# ahmed.add_money(200)

# # Show accounts again
# bank.show_accounts()


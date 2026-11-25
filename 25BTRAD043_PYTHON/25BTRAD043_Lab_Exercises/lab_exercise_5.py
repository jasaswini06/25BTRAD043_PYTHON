# LAB EXPERIMENT PART 5
# Name: Jasaswini Sahu
# USN: 25BTRAD043

import random

# Lab Exercise 14: Bank Account System Using OOP
class BankAccount:
    def __init__(self, holder):
        self.holder = holder
        self.__balance = 0

    def deposit(self, amount):
        if type(amount) is not int or amount <= 0:
            print("Invalid deposit. Enter a positive whole amount.")
            return

        self.__balance += amount
        print(f"Deposited: Rs. {amount}")

    def withdraw(self, amount):
        if type(amount) is not int or amount <= 0:
            print("Invalid withdrawal. Enter a positive whole amount.")
        elif amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            print(f"Withdrawn: Rs. {amount}")

    def check_balance(self):
        return self.__balance


account = BankAccount("Jasaswini")
print(f"Account holder: {account.holder}")
account.deposit(1000)
account.withdraw(300)
account.deposit(-100)
account.withdraw(0)
account.withdraw(800)
print(f"Current balance: Rs. {account.check_balance()}")

print()

# Lab Exercise 15: Library Management System
class LibraryItem:
    def __init__(self, title):
        self.title = title
        self.available = True

    def issue(self):
        if self.available:
            self.available = False
            print(f"Issued: {self.title}")
        else:
            print(f"Already issued: {self.title}")

    def return_item(self):
        if self.available:
            print(f"Already in the library: {self.title}")
        else:
            self.available = True
            print(f"Returned: {self.title}")


class Book(LibraryItem):
    def __init__(self, title, author):
        super().__init__(title)
        self.author = author

    def display(self):
        status = "Available" if self.available else "Issued"
        print(f"{self.title} by {self.author} | {status}")


book = Book("The Blue Umbrella", "Ruskin Bond")
book.issue()
book.issue()
book.display()
book.return_item()
book.return_item()
book.display()

print()

# Lab Exercise 16: Dice Simulator Using the Random Module
def roll_dice(number_of_dice, number_of_rounds):
    frequency = {face: 0 for face in range(1, 7)}

    for round_number in range(1, number_of_rounds + 1):
        outcomes = []

        for _ in range(number_of_dice):
            face = random.randint(1, 6)
            outcomes.append(face)
            frequency[face] += 1

        print(f"Round {round_number}: {outcomes}")

    print("\nFace frequencies")
    for face, count in frequency.items():
        print(f"{face}: {count}")


try:
    dice = int(input("Enter number of dice: "))
    rounds = int(input("Enter number of rounds: "))

    if dice <= 0 or rounds <= 0:
        print("Enter positive numbers for dice and rounds.")
    else:
        roll_dice(dice, rounds)
except ValueError:
    print("Enter whole numbers only.")

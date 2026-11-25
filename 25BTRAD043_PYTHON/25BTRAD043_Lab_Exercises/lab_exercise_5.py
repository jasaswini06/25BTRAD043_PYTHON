{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "3cb3bc2f",
   "metadata": {},
   "source": [
    "LAB EXPERIMENT PART 5\n",
    "\n",
    "NAME:JASASWINI SAHU\n",
    "\n",
    "USN:25BTRAD043"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ddbbe013",
   "metadata": {},
   "source": [
    "Lab Exercise 14 — Bank Account System Using OOP\n",
    "\n",
    "Question:\n",
    "\n",
    "Develop a Python program using classes and objects to manage bank accounts. Implement deposit, withdrawal, balance enquiry, and transaction validation.\n",
    "\n",
    "CODE:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "2ecd8f15",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Account holder: Jasaswini\n",
      "Deposited: Rs. 1000\n",
      "Withdrawn: Rs. 300\n",
      "Invalid deposit. Enter a positive whole amount.\n",
      "Invalid withdrawal. Enter a positive whole amount.\n",
      "Insufficient balance.\n",
      "Current balance: Rs. 700\n"
     ]
    }
   ],
   "source": [
    "class BankAccount:\n",
    "    def __init__(self, holder):\n",
    "        self.holder = holder\n",
    "        self.__balance = 0\n",
    "\n",
    "    def deposit(self, amount):\n",
    "        if type(amount) is not int or amount <= 0:\n",
    "            print(\"Invalid deposit. Enter a positive whole amount.\")\n",
    "            return\n",
    "\n",
    "        self.__balance += amount\n",
    "        print(f\"Deposited: Rs. {amount}\")\n",
    "\n",
    "    def withdraw(self, amount):\n",
    "        if type(amount) is not int or amount <= 0:\n",
    "            print(\"Invalid withdrawal. Enter a positive whole amount.\")\n",
    "        elif amount > self.__balance:\n",
    "            print(\"Insufficient balance.\")\n",
    "        else:\n",
    "            self.__balance -= amount\n",
    "            print(f\"Withdrawn: Rs. {amount}\")\n",
    "\n",
    "    def check_balance(self):\n",
    "        return self.__balance\n",
    "\n",
    "\n",
    "account = BankAccount(\"Jasaswini\")\n",
    "print(f\"Account holder: {account.holder}\")\n",
    "account.deposit(1000)\n",
    "account.withdraw(300)\n",
    "account.deposit(-100)\n",
    "account.withdraw(0)\n",
    "account.withdraw(800)\n",
    "print(f\"Current balance: Rs. {account.check_balance()}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2e28de22",
   "metadata": {},
   "source": [
    "Lab Exercise 15 — Library Management System\n",
    "\n",
    "Question:\n",
    "\n",
    "Develop a Python program using classes and objects to manage books, issue and return books, and maintain availability status.\n",
    "\n",
    "CODE:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "0030a94f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Issued: The Blue Umbrella\n",
      "Already issued: The Blue Umbrella\n",
      "The Blue Umbrella by Ruskin Bond | Issued\n",
      "Returned: The Blue Umbrella\n",
      "Already in the library: The Blue Umbrella\n",
      "The Blue Umbrella by Ruskin Bond | Available\n"
     ]
    }
   ],
   "source": [
    "class LibraryItem:\n",
    "    def __init__(self, title):\n",
    "        self.title = title\n",
    "        self.available = True\n",
    "\n",
    "    def issue(self):\n",
    "        if self.available:\n",
    "            self.available = False\n",
    "            print(f\"Issued: {self.title}\")\n",
    "        else:\n",
    "            print(f\"Already issued: {self.title}\")\n",
    "\n",
    "    def return_item(self):\n",
    "        if self.available:\n",
    "            print(f\"Already in the library: {self.title}\")\n",
    "        else:\n",
    "            self.available = True\n",
    "            print(f\"Returned: {self.title}\")\n",
    "\n",
    "\n",
    "class Book(LibraryItem):\n",
    "    def __init__(self, title, author):\n",
    "        super().__init__(title)\n",
    "        self.author = author\n",
    "\n",
    "    def display(self):\n",
    "        status = \"Available\" if self.available else \"Issued\"\n",
    "        print(f\"{self.title} by {self.author} | {status}\")\n",
    "\n",
    "\n",
    "book = Book(\"The Blue Umbrella\", \"Ruskin Bond\")\n",
    "book.issue()\n",
    "book.issue()\n",
    "book.display()\n",
    "book.return_item()\n",
    "book.return_item()\n",
    "book.display()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cac20b9d",
   "metadata": {},
   "source": [
    "Lab Exercise 16 — Dice Simulator Using the Random Module\n",
    "\n",
    "Question:\n",
    "\n",
    "Develop a Python program that simulates rolling one or more dice using Python's random module. Allow repeated rolls and display the outcomes.\n",
    "\n",
    "CODE:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "98d3aa20",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Round 1: [1, 2]\n",
      "Round 2: [4, 1]\n",
      "\n",
      "Face frequencies\n",
      "1: 2\n",
      "2: 1\n",
      "3: 0\n",
      "4: 1\n",
      "5: 0\n",
      "6: 0\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "\n",
    "\n",
    "def roll_dice(number_of_dice, number_of_rounds):\n",
    "    frequency = {face: 0 for face in range(1, 7)}\n",
    "\n",
    "    for round_number in range(1, number_of_rounds + 1):\n",
    "        outcomes = []\n",
    "\n",
    "        for _ in range(number_of_dice):\n",
    "            face = random.randint(1, 6)\n",
    "            outcomes.append(face)\n",
    "            frequency[face] += 1\n",
    "\n",
    "        print(f\"Round {round_number}: {outcomes}\")\n",
    "\n",
    "    print(\"\\nFace frequencies\")\n",
    "    for face, count in frequency.items():\n",
    "        print(f\"{face}: {count}\")\n",
    "\n",
    "\n",
    "try:\n",
    "    dice = int(input(\"Enter number of dice: \"))\n",
    "    rounds = int(input(\"Enter number of rounds: \"))\n",
    "\n",
    "    if dice <= 0 or rounds <= 0:\n",
    "        print(\"Enter positive numbers for dice and rounds.\")\n",
    "    else:\n",
    "        roll_dice(dice, rounds)\n",
    "except ValueError:\n",
    "    print(\"Enter whole numbers only.\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": ".venv (3.9.6)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

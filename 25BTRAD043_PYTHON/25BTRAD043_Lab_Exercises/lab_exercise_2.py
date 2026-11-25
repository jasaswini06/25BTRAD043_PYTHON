{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "4fd65f3f",
   "metadata": {},
   "source": [
    "Name : Jasaswini Sahu\n",
    "\n",
    "USN : 25BTRAD043\n",
    "\n",
    "LAB 2\n",
    "\n",
    "LAB EXPERIMENTS (Using Unit 2 Concepts)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2e7f9486",
   "metadata": {},
   "source": [
    "Lab Exercise 5\n",
    "\n",
    "Question:\n",
    "\n",
    "Number Guessing Game.\n",
    "\n",
    "CODE:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "a1919845",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "===== NUMBER GUESSING GAME =====\n",
      "Wrong guess!\n",
      "The correct number was: 4\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "\n",
    "number = random.randint(1, 10)\n",
    "print(\"===== NUMBER GUESSING GAME =====\")\n",
    "guess = int(input(\"Guess a number between 1 and 10: \"))\n",
    "\n",
    "if guess == number:\n",
    "    print(\"Correct! You guessed the number.\")\n",
    "else:\n",
    "    print(\"Wrong guess!\")\n",
    "    print(\"The correct number was:\", number)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4eb334b0",
   "metadata": {},
   "source": [
    "Lab Exercise 6\n",
    "\n",
    "Question:\n",
    "\n",
    "Prime Number and Factorial Programs.\n",
    "\n",
    "Program 1: Prime Number\n",
    "\n",
    "CODE:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "8cdf9735",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10 is not a Prime Number\n"
     ]
    }
   ],
   "source": [
    "number = int(input(\"Enter a number: \"))\n",
    "\n",
    "if number > 1:\n",
    "    for i in range(2, number):\n",
    "        if number % i == 0:\n",
    "            print(number, \"is not a Prime Number\")\n",
    "            break\n",
    "    else:\n",
    "        print(number, \"is a Prime Number\")\n",
    "else:\n",
    "    print(number, \"is not a Prime Number\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3373df33",
   "metadata": {},
   "source": [
    "Program 2: Factorial\n",
    "\n",
    "CODE:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "281ab213",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Factorial of 10 is 3628800\n"
     ]
    }
   ],
   "source": [
    "number = int(input(\"Enter a number: \"))\n",
    "factorial = 1\n",
    "\n",
    "for i in range(1, number + 1):\n",
    "    factorial = factorial * i\n",
    "\n",
    "print(\"Factorial of\", number, \"is\", factorial)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "599d1748",
   "metadata": {},
   "source": [
    "Lab Exercise 7\n",
    "\n",
    "Question:\n",
    "\n",
    "Fibonacci Series Using Recursion.\n",
    "\n",
    "CODE:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "ce37f12e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Fibonacci Series:\n",
      "0 1 1 2 "
     ]
    }
   ],
   "source": [
    "def fibonacci(n):\n",
    "    if n <= 1:\n",
    "        return n\n",
    "    else:\n",
    "        return fibonacci(n - 1) + fibonacci(n - 2)\n",
    "\n",
    "terms = int(input(\"Enter the number of terms: \"))\n",
    "print(\"Fibonacci Series:\")\n",
    "\n",
    "for i in range(terms):\n",
    "    print(fibonacci(i), end=\" \")"
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

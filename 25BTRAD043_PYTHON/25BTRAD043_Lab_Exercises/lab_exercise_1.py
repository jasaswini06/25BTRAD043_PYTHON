{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "eed9fa69",
   "metadata": {},
   "source": [
    "Name : Jasaswini Sahu\n",
    "\n",
    "USN : 25BTRAD043\n",
    "\n",
    "LAB EXPERIMENTS_Part 1\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cb51e8e8",
   "metadata": {},
   "source": [
    "Lab Exercise 1\n",
    "\n",
    "Question:\n",
    "Installing Python, Setting up VS Code / PyCharm, Jupyter Notebook\n",
    "STEPS:\n",
    "1. Download and install Python from the official Python website.\n",
    "2. Open the Python installer and complete the installation.\n",
    "3. Install VS Code or PyCharm as the code editor.\n",
    "4. Install the Python extension in VS Code if using VS Code.\n",
    "5. Install Jupyter Notebook using Python.\n",
    "6. Open VS Code / PyCharm / Jupyter Notebook.\n",
    "7. Create a new Python file with the .py extension.\n",
    "8. Write a simple Python program.\n",
    "9. Run the program and check the output."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e9b35d19",
   "metadata": {},
   "source": [
    "Lab Exercise 2\n",
    "\n",
    "Question:\n",
    "\n",
    "Write and execute a basic Python program.\n",
    "\n",
    "CODE:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "a8c3e5e8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello, World!\n",
      "Welcome to Python Programming\n"
     ]
    }
   ],
   "source": [
    "print(\"Hello, World!\")\n",
    "print(\"Welcome to Python Programming\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1e1e245c",
   "metadata": {},
   "source": [
    "Lab Exercise 3\n",
    "\n",
    "Question:\n",
    "\n",
    "Programs using variables, operators, and input/output.\n",
    "\n",
    "Program 1: Variables and Input/Output\n",
    "\n",
    "CODE:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "75b9bfe9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Name: jasaswini sahu\n",
      "Age: 19\n",
      "City: bengaluru\n"
     ]
    }
   ],
   "source": [
    "name = input(\"Enter your name: \")\n",
    "age = int(input(\"Enter your age: \"))\n",
    "city = input(\"Enter your city: \")\n",
    "print(\"Name:\", name)\n",
    "print(\"Age:\", age)\n",
    "print(\"City:\", city)\n",
    "\n",
    "a = 10\n",
    "b = 5"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "44574372",
   "metadata": {},
   "source": [
    "Program 2: Operators\n",
    "\n",
    "CODE:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "c14bf805",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Addition: 15\n",
      "Subtraction: 5\n",
      "Multiplication: 50\n",
      "Division: 2.0\n",
      "Modulus: 0\n"
     ]
    }
   ],
   "source": [
    "print(\"Addition:\", a + b)\n",
    "print(\"Subtraction:\", a - b)\n",
    "print(\"Multiplication:\", a * b)\n",
    "print(\"Division:\", a / b)\n",
    "print(\"Modulus:\", a % b)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e462d8b8",
   "metadata": {},
   "source": [
    "Lab Exercise 4\n",
    "\n",
    "Question:\n",
    "\n",
    "Simple calculator and area calculation programs.\n",
    "\n",
    "Program 1: Simple Calculator\n",
    "\n",
    "CODE:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "077477c7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Addition: 30.0\n",
      "Subtraction: -10.0\n",
      "Multiplication: 200.0\n",
      "Division: 0.5\n"
     ]
    }
   ],
   "source": [
    "a = float(input(\"Enter first number: \"))\n",
    "b = float(input(\"Enter second number: \"))\n",
    "print(\"Addition:\", a + b)\n",
    "print(\"Subtraction:\", a - b)\n",
    "print(\"Multiplication:\", a * b)\n",
    "print(\"Division:\", a / b)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f963d74d",
   "metadata": {},
   "source": [
    "Program 2: Area of a Rectangle\n",
    "\n",
    "CODE:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "8ab82744",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Area of Rectangle: 96.0\n"
     ]
    }
   ],
   "source": [
    "length = float(input(\"Enter the length: \"))\n",
    "breadth = float(input(\"Enter the breadth: \"))\n",
    "area = length * breadth\n",
    "print(\"Area of Rectangle:\", area)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "82de7c36",
   "metadata": {},
   "source": [
    "Program 3: Area of a Circle\n",
    "\n",
    "CODE:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "9aa6f2f1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Area of Circle: 78.5\n"
     ]
    }
   ],
   "source": [
    "radius = float(input(\"Enter the radius: \"))\n",
    "area = 3.14 * radius * radius\n",
    "print(\"Area of Circle:\", area)"
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

# Lab Exercise 2: Write and execute a basic Python program
print("Hello, World!") 
name = "Ansh" 
print("Welcome,", name) 



#Lab Exercise 3: Programs using variables, operators, and input/output

# # Variables
# a = 10
# b = 3
# # Arithmetic operators
# print("Addition:", a + b)
# print("Subtraction:", a - b)
# print("Multiplication:", a * b)
# print("Division:", a / b)
# print("Modulus:", a % b)
# print("Exponent:", a ** b)
# # Input/Output
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# print("Hello", name, "- you are", age, "years old.")

# # Comparison and logical operators
# x = 5
# y = 8
# print("x > y:", x > y)
# print("x < y and y > 0:", x < y and y > 0)


# Lab Exercise 4: Simple calculator and area calculation programs 25

# # Simple Calculator
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# op = input("Enter operator (+, -, *, /): ")

# if op == '+':
#     result = num1 + num2
# elif op == '-':
#     result = num1 - num2
# elif op == '*':
#     result = num1 * num2
# elif op == '/':
#     if num2 != 0:
#         result = num1 / num2
#     else:
#         result = "Error: Division by zero"
# else:
#     result = "Invalid operator"

# print("Result:", result)




# Area Calculation Program
# import math

# print("Choose shape: 1-Circle 2-Rectangle 3-Triangle")
# choice = int(input("Enter choice: "))

# if choice == 1:
#     r = float(input("Enter radius: "))
#     area = math.pi * r ** 2
#     print("Area of Circle:", round(area, 2))

# elif choice == 2:
#     length = float(input("Enter length: "))
#     width = float(input("Enter width: "))
#     area = length * width
#     print("Area of Rectangle:", area)

# elif choice == 3:
#     base = float(input("Enter base: "))
#     height = float(input("Enter height: "))
#     area = 0.5 * base * height
#     print("Area of Triangle:", area)

# else:
#     print("Invalid choice")
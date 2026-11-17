# Simple calculator using switch-case (match-case)

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

match operator:
    case '+':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    case '-':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    case '*':
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    case '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
    case _:
        print("Invalid operator. Please use +, -, *, or /.")
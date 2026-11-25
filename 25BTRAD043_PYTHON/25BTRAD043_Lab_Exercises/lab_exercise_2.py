import random

number = random.randint(1, 10)
print("===== NUMBER GUESSING GAME =====")
guess = int(input("Guess a number between 1 and 10: "))

if guess == number:
    print("Correct! You guessed the number.")
else:
    print("Wrong guess!")
    print("The correct number was:", number)

number = int(input("Enter a number: "))

if number > 1:
    for i in range(2, number):
        if number % i == 0:
            print(number, "is not a Prime Number")
            break
    else:
        print(number, "is a Prime Number")
else:
    print(number, "is not a Prime Number")

number = int(input("Enter a number: "))
factorial = 1

for i in range(1, number + 1):
    factorial = factorial * i

print("Factorial of", number, "is", factorial)

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

terms = int(input("Enter the number of terms: "))
print("Fibonacci Series:")

for i in range(terms):
    print(fibonacci(i), end=" ")

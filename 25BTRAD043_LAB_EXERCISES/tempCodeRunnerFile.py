def is_prime(number):
    if number < 2:
        return False
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True


number = int(input("Enter a number to check for prime: "))
if is_prime(number):
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")

factorial_number = int(input("Enter a non-negative number for factorial: "))
if factorial_number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    factorial = 1
    for value in range(1, factorial_number + 1):
        factorial *= value
    print(f"Factorial of {factorial_number} is {factorial}.")
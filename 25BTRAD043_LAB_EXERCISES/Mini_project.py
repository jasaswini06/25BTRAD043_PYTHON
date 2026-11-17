import random

# Generate a 6-digit OTP
otp = random.randint(100000, 999999)
print("Your OTP is:", otp)

# def generate_otp(length=6):
#     # Linear Congruential Generator (LCG) parameters
#     # Values commonly used in standard C/C++ runtimes
#     multiplier = 1103515245
#     increment = 12345
#     modulus = 2**31

#     # Use the memory address of a new object as a dynamic seed
#     seed = id(object())

#     otp = ""
#     for _ in range(length):
#         seed = (multiplier * seed + increment) % modulus
#         digit = seed % 10
#         otp += str(digit)

#     return otp


# # Example usage
# print("Generated OTP:", generate_otp())
# print("8-digit OTP:", generate_otp(8))
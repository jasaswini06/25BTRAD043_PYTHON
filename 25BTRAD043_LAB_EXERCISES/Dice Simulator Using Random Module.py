import random


def roll_dice(num_dice):
    rolls = [random.randint(1, 6) for _ in range(num_dice)]
    return rolls


while True:
    try:
        num = int(input("\nHow many dice do you want to roll? "))
        if num < 1:
            print("Enter at least 1 die.")
            continue

        outcomes = roll_dice(num)
        print(f"Rolled: {outcomes} | Total Sum: {sum(outcomes)}")

        again = input("Roll again? (y/n): ").strip().lower()
        if again != "y":
            print("Exiting simulator.")
            break
    except ValueError:
        print("Please enter a valid integer.")
import random


secret_number = random.randint(1, 10)

number = int(input("Guess the secret number between 1 and 10: "))

while number != secret_number:

    if number < secret_number:
        print("Too low")

    elif number > secret_number:
        print("Too high")

    number = int(input("Guess the secret number between 1 and 10: "))

print(f"Correct! The answer was {secret_number}")
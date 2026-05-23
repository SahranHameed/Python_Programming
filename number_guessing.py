# Number Gussing game
import random

print("Number Gussing Game")
print("-------------------")

number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Guuss the number (1-100): "))
    attempts += 1

    if guess < number:
        print("Too Low! Try again!")
    elif guess > number:
        print("Too High! Try again!")
    else:
        print(f"Correct! You Guessed it in {attempts} attempts!")
        break
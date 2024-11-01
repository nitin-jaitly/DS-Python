import random

# Simple Number Guessing Game

number = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))

if guess == number:
    print("You won!")
else:
    print("Sorry, try again!")


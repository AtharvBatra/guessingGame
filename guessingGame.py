import random

number = random.randrange(1,9)
guess = int(input("guess a number between 1 to 9\nEnter your guess:-"))
chances = 5

while guess != number:
    if guess < number:
        print("You need to guess higher")
        guess = int(input("guess a number between 1 to 9\nEnter your guess:-"))
    else:
        print("You need to guess lower")
        guess = int(input("guess a number between 1 to 9\nEnter your guess:-"))

print("You guessed the number correctly!")
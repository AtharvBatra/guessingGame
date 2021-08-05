import random

number = random.randrange(1, 9)
chances = 0

while chances < 5:
    guess = int(input("guess a number between 1 to 9\nEnter your guess:-"))
    if chances == 4:
        print("You lose")
        break
    elif guess == number:
        print("You win!")
        break
    elif guess < number:
        print("Your guess is too low,","the number is higher than",guess)
    elif guess > number:
        print("Your guess is too high,","the number is lower than",guess)
    chances+=1

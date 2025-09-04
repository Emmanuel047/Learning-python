#Number Guessing Game
#Build a small game where the computer picks a random number 
# and the user has to guess it. #
# Provide hints like "too high" or "too low" based on the guess.

import random
import time
num = random.randint(1, 100)
while True:
    guess = int(input("Enter your guess: "))
    if guess < num:
        print("Too low")
    elif guess > num:
        print("Too high")
    else:
        time.sleep(1)
        print("You've guessed right")
        break
# 09/16/2025
# Practice: Build your own Number Guessing Game

import random

random_number = random.randint(1, 20)
usr_attempts = 0
usr_limit = 7

while usr_attempts < usr_limit:
    usr_guess = int(input("\nEnter a number between 1 and 20. \nYou have 7 chances: "))
    usr_attempts += 1
    if usr_guess == random_number:
        print(f"You win. The number is {random_number}.\nYou won in {usr_attempts} attempts")
        break
    elif usr_guess >= random_number:
        print("Too high. Try again.")
    elif usr_guess <= random_number:
        print("Too low. Try again.")    
else:
    print(f"You lose. The number is {random_number}.")
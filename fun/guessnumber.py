# Made by Luuk Klingens
# GitHub: https://github.com/luukklingens
# Copyright Luuk Klingens 2025
import random

def guess_number():
    input("Welcome to the Guess the Number game! Press Enter to start...")
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed = False
    while not guessed:
        try:
            guess = int(input("Enter your guess (between 1 and 100): "))
            attempts += 1
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                guessed = True
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 100.")
if __name__ == "__main__":
    guess_number()

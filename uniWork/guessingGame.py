# Importing random library
import random

# Defining main game function
def guessing_game():
    print("Welcome to the Guessing Game!\n")
    print("I have selected a number between 1 and 20.\n")
    print("You have 6 atte4mpts to guess it.\n")

    # Generate a random number between 1 and 20
    secretNumber = random.randint(1, 20)
    attempts = 6

    # While loop to check attempts and check win state
    while attempts > 0:
        guess = int(input("Enter your guess: "))
        if guess < secretNumber:
            print("Too low, try again.")
        elif guess > secretNumber:
            print("Too high, try again.")
        else:
            print("Congratulations! Your guess is correct. YOU WIN!")
            return  # Exit the function if the guess is correct

        attempts -= 1
        print(f"You have {attempts} attempts left.\n")

    print("Sorryno attempts left. The secret number was:", secretNumber)


# Call the function to start the game
guessing_game()

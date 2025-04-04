import random

def guess_the_number():
    # Randomly generate a number between 1 and 100
    number_to_guess = random.randint(1, 100)
    
    print("Welcome to 'Guess the Number'!")
    print("I have randomly chosen a number between 1 and 100.")
    print("Try to guess it!")

    # Variable to track the number of attempts
    attempts = 0

    while True:
        try:
            # Prompt the user to make a guess
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            # Check if the guess is correct, too high, or too low
            if user_guess < number_to_guess:
                print("Your guess is too low. Try again!")
            elif user_guess > number_to_guess:
                print("Your guess is too high. Try again!")
            else:
                print(f"Congratulations! You've guessed the number {number_to_guess} correctly in {attempts} attempts.")
                break  # Exit the loop when the guess is correct
        except ValueError:
            print("Invalid input! Please enter a valid number.")

# Run the game
guess_the_number()

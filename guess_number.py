import random

def guess_number():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        guess = int(input("Take a guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts!")
            break

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        guess_number()
    else:
        print("Thank you for playing Guess the Number!")

guess_number()

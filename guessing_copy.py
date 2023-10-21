import random

def guessing_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    play_again = True

    while play_again:
        print("Welcome to the Number Guessing Game!")
        print("I'm thinking of a number between 1 and 100.")

        while True:
            try:
                user_guess = int(input("Guess the number: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        attempts += 1

        if user_guess < secret_number:
            print("Too low! Try again.")
        elif user_guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations, you guessed it in {attempts} attempts!")

            while True:
                play_again_input = input("Play again? (yes/no): ").lower()
                if play_again_input == "no":
                    play_again = False
                    break
                elif play_again_input == "yes":
                    break
                else:
                    print("Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    guessing_game()

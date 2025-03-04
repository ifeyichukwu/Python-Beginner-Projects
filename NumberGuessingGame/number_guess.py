import random

print("Number Guessing Game")

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I have picked a number between 1 and 100.")
    print("Try to guess it!")

    #generate a random number between 1 and 100

    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            #Ask the player for their guess
            guess = int(input("\nEnter your guess: "))
            attempts += 1

            #check if hte gues is correct
            if guess < secret_number:
                print("⛔ Too Low! Try again.")
            elif guess > secret_number:
                print("🔺 Too high! Try again.")
            else: 
                print(f"✅  Congratulations! you guessed the right number in {attempts} attempts!")
                break # End the game

        except ValueError:
            print("⚠️ Invalid input! Please enter a number.")

# Run the game
if __name__ == "__main__":
    number_guessing_game()

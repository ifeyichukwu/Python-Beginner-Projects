import number_guess
import random

def guess_number():
    print("I have picked a number between 1 and 50.")
    print("Could you guess it right?")

    picked_number = random.randint(1, 50)
    attempts = 0

    while True:
        try:
            guessed_number = int(input("\nWhat is your guess: "))
            attempts +=1

            if guessed_number == picked_number:
                print (f"Conratulations, your guess of {guessed_number} is correct. \n Total number of Attempts = {attempts} ✔")
                break
            
            elif guessed_number < picked_number:
                print (f"You are almost there, just a bit higher ➕")
            
            elif guessed_number > picked_number:
                print (f"You are almost there, just a bit lower. ➖")
            
        except ValueError:
            print("It seems you didn't enter a valid number. Please try again")


if __name__ == "__main__": 
    guess_number()
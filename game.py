import random

secret_number = random.randint(1, 100)
num_guesses = 0
max_guesses = 10

print("I'm thinking of a number between 1 and 100. Can you guess what it is?")

while num_guesses < max_guesses:
    guess = input("Enter your guess: ")
    try:
        guess = int(guess)
    except ValueError:
        print("That's not a valid number. Please try again.")
        continue
    
    if guess < secret_number:
        print("Too low! Guess higher.")
    elif guess > secret_number:
        print("Too high! Guess lower.")
    else:
        print("Congratulations, you guessed it!")
        break
        
    num_guesses += 1

if num_guesses == max_guesses:
    print(f"Sorry, you ran out of guesses. The number was {secret_number}.")

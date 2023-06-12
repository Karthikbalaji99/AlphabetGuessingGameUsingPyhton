import random

while True:
    random_alphabet = random.choice('abcdefghijklmnopqrstuvwxyz')  # Generate a random English alphabet
    print("Guess a random English alphabet.")

    chances = 0
    while chances < 8:  # Allow the user to guess up to 8 times
        chances += 1
        guess = input("Enter your guess: ").lower()  # Take user's guess and convert it to lowercase

        if guess == random_alphabet:  # Check if the guess matches the random alphabet
            print("Congratulations, you did it! The alphabet was", random_alphabet)
            break
        elif guess < random_alphabet:  # Check if the guess is smaller than the random alphabet
            print("Your guessed alphabet comes before the correct alphabet.")
        elif guess > random_alphabet:  # Check if the guess is larger than the random alphabet
            print("Your guessed alphabet comes after the correct alphabet.")

        if chances == 7:  # If the user has made 7 incorrect guesses
            print("\nYou've run out of chances.")
            print("The alphabet was", random_alphabet)
            print("Better luck next time.")
            break

    play_again = input("\nDo you want to play again? (yes/no): ").lower()  # Ask the user if they want to play again
    if play_again != "yes":  # If the user doesn't want to play again, exit the loop
        break

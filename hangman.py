#A simple hangman Game
import random

from words import word_list

word_to_guess = random.choice(word_list)

print(word_to_guess)

print("Welcome to Hangman!")

blank = ""

word_length = len(word_to_guess)
for position in range(word_length):
    blank = blank + "_"
print("Word to guess: " + blank)

"""Defining the number of lives of the player, initializing the game as not 
over & creating an empty list to store the letters guessed correctly"""

no_of_lives = 6
letters_guessed = []
game_over = False

while not game_over:
    print(f"\n, You have {no_of_lives} lives left\n")
    guess = input("Guess a letter: ").lower()

    if guess in letters_guessed:
        print(f"You have already guessed the letter {guess}")

    your_word = ""
    
    for letter in word_to_guess:
        if letter == guess:
            your_word  = your_word + letter
            letters_guessed.append(guess)
        elif letter in letters_guessed:
            your_word  = your_word + letter
        else:
            your_word = your_word + "_"
            
    print("\nWord to guess: ", your_word)
    
    if guess not in word_to_guess:
        number_of_lives -= 1
        print(f"\nYou guessed {guess}, that's not in the word. You lose a life.")

        if number_of_lives == 0:
            game_over = True
            print(f"\nIT WAS {word_to_guess}! YOU LOSE!")

    if "_" not in your_word:
        game_over = True
        print("\nYou have guessed the word! YOU WIN!")
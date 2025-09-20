'''
This is a simple Hangman game using Python programming language.

The Hangman program randomly selects a secret word from a list of secret words.
The Game: Here, a random word (a fruit name) is picked up from our collection and the player gets limited chances to win the game.
When a letter in that word is guessed correctly, that letter position in the word is made visible. In this way, all letters of the word are to be guessed before all the chances are over. 
For convenience, we have given length of word + 2 chances. 
'''
import random
from collections import Counter

words = '''apple banana mango strawberry orange grape pineapple lemon coconut watermelon cherry papaya berry peach lychee'''

words = words.split(" ")


def hangman_game():
    secret_word = random.choice(words)

    print("Guess the word! HINT: word is a name of a fruit.")

    for i in secret_word:
        print("_", end=" ")
    print()

    letter_correctly_guessed = ""
    letter_wrongly_guessed = ""
    chances = len(secret_word) + 2
    chances_used = 0
    correct = 0
    flag = 0

    print(f"You have {chances} chances to guess the word correctly.")

    try:
        # if the user guessed the letter correctly flag is updated
        while (chances != 0) and flag == 0:
            print()
            chances -= 1
            chances_used += 1
            try:
                print()
                guess = str(input("Enter a letter to guess: "))
            except:
                print("Enter only a Letter!")
                continue

            # guess validation
            if len(guess) > 1:
                print("Enter a single letter.")

            elif guess in letter_correctly_guessed:
                print(
                    f"You have already guessed this letter. Number of chances remaining is {chances}")

            # If the correct letter is guessed
            if guess in secret_word:
                print(
                    f"{guess} is in the word. Number of chances remaining is {chances}")
                # num is the number of times the letter used in the secret word
                num = secret_word.count(guess)

                # this for loop places the correct guessed letter in all the correct places
                for _ in range(num):
                    letter_correctly_guessed += guess

            if guess not in secret_word and guess in letter_wrongly_guessed:
                print(
                    f"You have already guessed the letter '{guess}'. Number of chances remaining is {chances}")

            # If the guessed letter is not correct
            if guess not in secret_word and guess not in letter_wrongly_guessed:
                print(
                    f"The letter '{guess}' is not in the word. Number of chances remaining is {chances}")
                letter_wrongly_guessed += guess

            # If the secred word is guessed correctly
            for char in secret_word:
                if char in letter_correctly_guessed and (Counter(letter_correctly_guessed) != Counter(secret_word)):
                    print(char, end=" ")
                    correct += 1

                elif (Counter(letter_correctly_guessed) == Counter(secret_word)):
                    print()
                    print(
                        f"The word is {secret_word}. You WON! You guessed the word in {chances_used} chances.")
                    flag = 1

                    break
                else:
                    print("_", end=" ")
        if chances == 0 and (Counter(letter_correctly_guessed) != Counter(secret_word)):
            print()
            print(
                f"\nSorry! You LOST! You have {chances} chances remaining. The word was '{secret_word}'.")

    except KeyboardInterrupt:
        print()
        print("Bye! Try again.")
        exit


def user_consent():
    while True:
        print("\nDo you want to play again?")
        print("1. Yes\n2. No")

        ans = input("> ")

        if ans == "1":
            hangman_game()

        else:
            print("\nThank You for playing!")
            break


while True:
    print("\nDo you want to play the Hangman game where you need to guess the word of a fruit?")
    print("1. Yes(Type 1 for Yes)\n2. No(Type 2 for no)")

    answer = input("> ")

    if answer == "1":
        hangman_game()
        user_consent()
        break
    else:
        print("See you later!")
        break

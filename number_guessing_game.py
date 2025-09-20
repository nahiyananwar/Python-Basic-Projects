'''
Write a program to have the computer randomly select a number between 1 and
100, and then prompt the player to guess the number. The program should give
hints if the guess is too high or too low.

-> Allow the user to specify the minimum and maximum values for the number
range before the game starts. This gives the player more control over the
difficulty level. 
-> Implement a feature that limits the number of guesses a player can make. If
the player runs out of attempts, the game should end, and the correct number
should be revealed. 
-> Add a feature that keeps track of the fewest attempts it took to guess the
number correctly. The program should display this "best score" at the end of
each game. 

'''

import random

print()
print("NUMBER GUESSING GAME!!!!!")
print("=" * 60)
print("\n1. You need to set the difficulty by selecting the upper & lower bound of the number."
      "\n2. You will have 7 chances to guess the numebr.")


def number_guessing_game():

    print("\nLet's get started....")
    upper_bound = input("\nEnter the upper bound of the number: ")
    lower_bound = input("\nEnter the lower bound of the number: ")

    number = random.randint(int(lower_bound), int(upper_bound))
    attempt_counter = 0
    num_of_guess = 7

    print("\nThe secret number is generated.")

    while (num_of_guess >= 0):

        try:
            guess = int(input("\nEnter your guess: "))

            attempt_counter += 1
            num_of_guess -= 1

            if guess == number:
                print(
                    f"\nThe secret number was {number}. CONGRATULATION!!!! You've guessed the number correctly! \nAttempts taken: {attempt_counter}")
                print()
                break

            elif guess > number and num_of_guess != 0:
                print(
                    f"\nYour guess is too high! Make a lower guess. Number of chances remaining: {num_of_guess}")

            elif guess < number and num_of_guess != 0:
                print(
                    f"\nYour guess is too low! Make a higher guess. Number of chances remaining: {num_of_guess}")

            elif guess != number and num_of_guess == 0:
                print(
                    f"\nNo more chances!! YOU LOST!!!! The number was {number}.")
                break

        except ValueError:
            print("\nPlease enter a Valid number.")


def user_consent():
    while True:
        print()
        print("Would you like to play again?")
        print("1. Yes\n2. No")

        ans = int(input("> "))

        if ans == 1:
            print("\nGreat! Let's play again!")
            number_guessing_game()

        else:
            print("\nThank you for playing!\n")
            break


while True:
    print("\nNow, would you like to play the game?")
    print("\n1. Yes\n2. No")

    answer = input("> ")

    print("=" * 60)

    if answer == "1":
        number_guessing_game()
        user_consent()
        break
    else:
        print("\nThank you for playing the game!\n")

'''
Write a program that simulates rolling a pair of dice. Each time the program runs, it
should randomly generate two numbers between 1 and 6 (inclusive), representing
the result of each die. The program should then display the results and ask if the
user would like to roll again.

-> Modify the program so the user can specify how many dice they want to roll.
-> Add a feature that keeps track of how many times the user has rolled the dice
during the session. This will require a counter that increments each time the
dice are rolled. 

'''

import random

while True:
    print("\nDo you want to play the Dice-Rolling game?")
    print("1. Yes\n2. No")

    answer = input("> ")

    if answer == "1":
        print("\nHi, Welcome to the Dice-Rolling game. Let's get started!")
        print("=" * 50)

        print("\nHow many times do you want to roll the dice?")
        ans = int(input("> "))

        roll_tracker = 0

        while ans != 0:

            dice_1 = random.randint(1, 6)
            dice_2 = random.randint(1, 6)

            roll_tracker += 1
            ans -= 1

            print(f"\nNumber of times the dice rolled: {roll_tracker}")
            print(f"\nFirst dice: {dice_1}\nSecond dice: {dice_2}")

        else:
            print(
                f"\nYou have rolled {roll_tracker} times. Thanks for playing!")

    else:
        print("\nSee you later!")

        break

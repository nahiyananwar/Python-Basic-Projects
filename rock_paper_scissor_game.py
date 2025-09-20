'''
Write a program to simulate a game of Rock, Paper, Scissors.
The game will prompt the player to choose rock, paper, or scissors by typing 'r',
'p', or 's'. The computer will randomly select its choice. The game will then display
both choices using emojis and determine the winner based on the rules.

-> Modify the game so that the first player (or computer) to win two out of three
rounds is declared the overall winner. This adds a competitive aspect to the
game. 
-> Keep a tally of how many times the player wins, loses, or ties with the
computer. Display these statistics at the end of the game.
-> Add an option for two players to play against each other, taking turns to input
their choices. The program should then determine the winner based on their
inputs. 

'''

import random
import pwinput

ROCK = 'r'
PAPER = 'p'
SCISSORS = 's'


def user_consent():  # Asks the user if he wants to play the game or not

    while True:
        print("\nDo you want to play Rock, Papers & Scissors game?")
        print("1. Yes\n2. No")

        answer = input("> ")

        for char in answer:
            if not char.isdigit():
                print("\nInvalid Input. Enter 1 for YES and 2 for NO.")
            else:
                return char


def user_consent_validation():  # Validates the user response

    ans = user_consent()

    while True:
        for answer in ans:
            if not answer.isdigit():
                print("\nEnter a valid number.")

        if ans == "1":
            print("Great! Let's get started.\n")
            return ans

        elif ans == "2":
            print("\nSee you later!\n")
            return ans

        else:
            print("\nEnter either 1 or 2.")
            break


def solo_or_dual():  # Asks the user if he wants to play pvp or against the computer
    while True:
        response = input(
            "\nDo you want to play solo or dual?\n1. Solo (Against Computer)\n2. Dual (Player vs Player)\n> ")

        for res in response:
            if not res.isdigit():
                print("\nEnter a NUMBER.")

            elif response == "1":
                print("\nComputer is ready to play!!!")
                return response  # Returns the user response

            elif response == "2":
                print("\nBoth players get ready!!!")
                return response  # Returns the user response

            else:
                print("\nEnter either 1 or 2.")
                continue
            break


def no_of_games():  # Asks the user, how many games he wants to play
    while True:
        games = input("\nHow many games do you want to play?\n> ")

        for game in games:
            if not game.isdigit():
                print("\nEnter a number.")

            else:
                return games
            break


def game_rules_against_comp():  # Main game logic

    games = no_of_games()
    print(f"\nNumber of games to be played: {games}")

    winner = (int(games) // 2) + 1

    print(f"\nWhoever wins {winner} games, will win the match.")

    p1_wins = 0
    p2_wins = 0
    draw = 0
    games_played = 0

    letters = {ROCK: 'Rock''🪨', PAPER: 'Paper''📃', SCISSORS: 'Scissor''✂️'}
    word = [ROCK, PAPER, SCISSORS]

    while p1_wins < winner and p2_wins < winner and games_played != int(games):
        comp = random.choice(word)
        print()
        user = input(
            "Choose between rock(r), paper(p), or scissors(s): ").lower()

        if user not in word:
            print(
                "\nInvalid Choice. Type 'r' for Rock, 'p' for Paper, or 's' for Scissor.")

        if user == comp:
            print(
                f"\nUser choice: {letters[user]}\nComputer choice: {letters[comp]}")
            print("\nIt's a TIE.")

            draw += 1
            print(
                f"\nUser wins: {p1_wins}\nComputer wins: {p2_wins}\nGames Played = {games_played}")

        elif ((user == ROCK and comp == SCISSORS)
                or (user == PAPER and comp == ROCK)
                or (user == SCISSORS and comp == PAPER)):
            print(
                f"\nUser choice: {letters[user]}\nComputer choice: {letters[comp]}")
            print(f"\n{letters[user]} BEATS {letters[comp]}\nYou Win!!!")

            p1_wins += 1
            games_played += 1

            print(
                f"\nUser wins: {p1_wins}\nComputer wins: {p2_wins}\nGames Played = {games_played}")

        elif ((user == ROCK and comp == PAPER)
                or (user == PAPER and comp == SCISSORS)
                or (user == SCISSORS and comp == ROCK)):
            print(
                f"\nUser choice: {letters[user]}\nComputer choice: {letters[comp]}")
            print(f"\n{letters[comp]} BEATS {letters[user]}\nYou LOSE!!!")

            p2_wins += 1
            games_played += 1

            print(
                f"\nUser wins: {p1_wins}\nComputer wins: {p2_wins}\nGames Played = {games_played}")

    return p1_wins, p2_wins, draw, games_played


def game_rules_pvp():
    games = no_of_games()
    print(f"\nNumber of games to be played: {games}")

    winner = (int(games) // 2) + 1

    print(f"\nWhoever wins {winner} games, will win the match.")

    p1_wins = 0
    p2_wins = 0
    draw = 0
    games_played = 0

    letters = {ROCK: 'Rock''🪨', PAPER: 'Paper''📃', SCISSORS: 'Scissor''✂️'}
    word = tuple(letters.keys())

    while p1_wins < winner and p2_wins < winner and games_played != int(games):
        print()
        player_1 = pwinput.pwinput(
            "Player-1: Choose between rock(r), paper(p), or scissors(s): ").lower()

        player_2 = pwinput.pwinput(
            "Player-2: Choose between rock(r), paper(p), or scissors(s): ").lower()

        if (player_1 and player_2) not in word:
            print(
                "\nInvalid Choice. Type 'r' for Rock, 'p' for Paper, or 's' for Scissor.")

        if player_1 == player_2:
            print(
                f"\nPlayer-1 choice: {letters[player_1]}\nPlayer-2 choice: {letters[player_2]}")
            print("\nIt's a TIE.")

            draw += 1
            if p1_wins > 0 and p2_wins > 0:
                print(
                    f"\nPlayer-1 wins: {p1_wins}\nPlayer-2 wins: {p2_wins}\nGames Played = {games_played}")

            else:
                print()

        elif ((player_1 == ROCK and player_2 == SCISSORS)
                or (player_1 == PAPER and player_2 == ROCK)
                or (player_1 == SCISSORS and player_2 == PAPER)):
            print(
                f"\nPlayer-1 choice: {letters[player_1]}\nPlayer-2 choice: {letters[player_2]}")
            print(
                f"\n{letters[player_1]} BEATS {letters[player_2]}\nPlayer-1 Wins!!!")

            p1_wins += 1
            games_played += 1

            print(
                f"\nPlayer-1 wins: {p1_wins}\nPlayer-2 wins: {p2_wins}\nGames Played = {games_played}")

        elif ((player_1 == ROCK and player_2 == PAPER)
                or (player_1 == PAPER and player_2 == SCISSORS)
                or (player_1 == SCISSORS and player_2 == ROCK)):
            print(
                f"\nPlayer-1 choice: {letters[player_1]}\nPlayer-2 choice: {letters[player_2]}")
            print(
                f"\n{letters[player_2]} BEATS {letters[player_1]}\nPlayer-2 Wins!!!")

            p2_wins += 1
            games_played += 1

            print(
                f"\nPlayer-1 wins: {p1_wins}\nPlayer-2 wins: {p2_wins}\nGames Played = {games_played}")

    return p1_wins, p2_wins, draw, games_played


def statistics_vs_comp():  # Displays the result

    statistics_vs_comp = game_rules_against_comp()

    user_win = statistics_vs_comp[0]
    comp_win = statistics_vs_comp[1]
    draws = statistics_vs_comp[2]
    no_of_games = statistics_vs_comp[3]

    print("\nFinal Result:")

    print(
        f"\nUser wins: {user_win}\nComputer Wins: {comp_win}\nNumber of Draws: {draws}\nTotal Number of Games Played: {no_of_games}")
    print()

    if user_win > comp_win:
        print("You are the Winner!!!")

    else:
        print("You lost!!!")


def statistics_pvp():

    pvp_statistics = game_rules_pvp()

    player_1_win = pvp_statistics[0]
    player_2_win = pvp_statistics[1]
    draws = pvp_statistics[2]
    no_of_games = pvp_statistics[3]

    print("\nFinal Result:\n")

    print(
        f"\nPlayer-1 wins: {player_1_win}\nPlayer-2 Wins: {player_2_win}\nNumber of Draws: {draws}\nTotal Number of Games Played: {no_of_games}")
    print()

    if player_1_win > player_2_win:
        print("Player-1 is the Winner!!!")

    else:
        print("Player-2 is the winner!!!")


def would_continue():

    while True:
        answer = input("\n\nWould you like to play again?\n1. Yes\n2. No\n> ")

        for ans in answer:
            if not ans.isdigit():
                print("\nInvalid input. Enter a number.")

            elif answer == "1":
                return answer

            elif answer == "2":
                print("\nThank You for playing!!!")
                break
            else:
                print("\nEnter either 1 or 2.")
        break


def rock_paper_scissors():  # Main game function

    answer = user_consent_validation()

    if answer == "1":
        while True:
            player = solo_or_dual()
            if player == "1":
                statistics_vs_comp()
                answer = would_continue()

                if answer == "1":
                    continue

                else:
                    print()
                    break

            elif player == "2":
                statistics_pvp()
                answer = would_continue()

                if answer == "1":
                    continue

                else:
                    print()
                    break


rock_paper_scissors()

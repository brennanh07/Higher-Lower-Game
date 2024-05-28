from game_data import data
import random
import os
from art import logo
from art import vs


def clear():
    os.system("cls")


def calculate_higher(celeb1, celeb2):
    followers1 = celeb1["follower_count"]
    followers2 = celeb2["follower_count"]
    if followers1 > followers2:
        return "A"
    else:
        return "B"


def main():

    print(logo)
    print("Welcome to the Higher-Lower Game!")
    print("\nYou will be given two celebrities to compare, and you must guess which one has more Instagram followers.\n")

    a_celeb = random.choice(data)

    play_game = True

    score = 0

    while play_game:

        b_celeb = random.choice(data)
        while b_celeb == a_celeb:
            b_celeb = random.choice(data)

        more_followers = calculate_higher(a_celeb, b_celeb)

        print(f"A: {a_celeb['name']}, a {a_celeb['description']} from {a_celeb['country']}.")

        print(vs)

        print(f"B: {b_celeb['name']}, a {b_celeb['description']} from {b_celeb['country']}.")

        guess = input("\nWho has more followers? Type 'A' or 'B': ").upper()

        if guess == more_followers:
            a_celeb = b_celeb
            score += 1
            clear()
            print(f"\nThat's correct! Current score: {score}.\n")
        else:
            print(f"\nSorry, that's incorrect. Final score: {score}.")
            play_game = False

    play_again = input("\nWould you like to play again? Type 'y' or 'n': ")
    if play_again == "y":
        main()


main()


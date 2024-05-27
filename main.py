from game_data import data
import random
from os import system


def calculate_higher(celeb1, celeb2):
    followers1 = celeb1["follower_count"]
    followers2 = celeb2["follower_count"]
    if followers1 > followers2:
        return "A"
    else:
        return "B"


print("Welcome to the Higher-Lower Game!")
print("You will be given two celebrities to compare, and you must guess which one has more Instagram followers.")

a_celeb = random.choice(data)

play_game = True

score = 0

while play_game:

    b_celeb = random.choice(data)
    while b_celeb == a_celeb:
        b_celeb = random.choice(data)

    more_followers = calculate_higher(a_celeb, b_celeb)
    print(more_followers)

    print(f"A: {a_celeb["name"]}, a {a_celeb["description"]} from {a_celeb["country"]}.")

    print(f"B: {b_celeb["name"]}, a {b_celeb["description"]} from {b_celeb["country"]}.")

    guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    system("cls")

    if guess == more_followers:
        a_celeb = b_celeb
        score += 1
        print(f"That's correct! Current score: {score}.")
    else:
        print(f"Sorry, that's incorrect. Final score: {score}.")
        play_game = False




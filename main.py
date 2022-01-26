# Name: Ruben Sanduleac
# Date: January 25th, 2022
# Description: This game the user puts themselfs to the test to see if they know
#              which are the most popular influencers on Instagram.  Simply decide which Person
#              has the most follower count searched for the most by selecting higher or lower.
#              The objective is to get the most right in a row.
import random
from data import data
from cover_art import logo
from cover_art import vs


def compare(pla1, pla2):
    """This function compares two follower counts between two users."""

    if (pla1['follower_count']) > (pla2['follower_count']):
        return 1
    elif (pla1['follower_count']) < (pla2['follower_count']):
        return 0


def game():
    """This function is the main game function responsible for the core function of the game
    """
    # Keeps track of the users streak score
    counter = 0
    # print logo
    game_over = False
    # print the random player1 description
    while not game_over:
        player1 = random.choice(data)
        player2 = random.choice(data)
        print(logo)
        if counter > 0:
            print(f"You are right! Current score: {counter}.")
        print(
            f"Compare A: {player1['name']}, a {player1['description']} from {player1['country']}")
        # print the vs logo
        print(vs)
        # select a random playerin the dictionary
        # print the random player1 description
        print(
            f"Compare B: {player2['name']}, a {player2['description']} from {player2['country']}")

        choice = input("Who has more followers? Type 'A' or 'B': ").upper()

        if choice == 'A':
            if compare(player1, player2) == 1:
                counter += 1
            elif compare(player1, player2) == 0:
                print(f"Sorry, that's wrong. Final score: {counter}.")
                break
        elif choice == 'B':
            if compare(player1, player2) == 0:
                print("Im here B")
                counter += 1
            elif compare(player1, player2) == 1:
                print(f"Sorry, that's wrong. Final score: {counter}.")
                break
        print(counter)


game()
# TODO (DONE) Add higher lower logo
# TODO (DONE) randomly pickout from dictionary make, sure its not the same
# TODO (DONE) print the account name, discription, then country
# TODO (DONE) print the 'Vs' Logo
# TODO (DONE) print the vs account name, discription, then country
# TODO (DONE) print who has more follower_count
# TODO (DONE) compare and give user the prompt "Who has more followers? Type 'A' or 'B':"
# TODO (DONE) repeat propt until the user guesses incorrectly 'Sorry, that's wrong. Final score:'
# TODO create a counter for final score

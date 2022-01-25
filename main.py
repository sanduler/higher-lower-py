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


def game():
    # print logo
    print(logo)
    # select a random playerin the dictionary
    player1 = random.choice(data)
    # print the random player1 description
    print(
        f"Compare A: {player1['name']}, a {player1['description']} from {player1['country']}")
    # print the vs logo
    print(vs)
    # select a random playerin the dictionary
    player2 = random.choice(data)
    # print the random player1 description
    print(
        f"Compare B: {player2['name']}, a {player2['description']} from {player2['country']}")


game()
# TODO Add higher lower logo
# TODO randomly pickout from dictionary make, sure its not the same
# TODO print the account name, discription, then country
# TODO print the 'Vs' Logo
# TODO print the vs account name, discription, then country
# TODO print who has more follower_count
# TODO compare and give user the prompt "Who has more followers? Type 'A' or 'B':"
# TODO repeat propt until the user guesses incorrectly 'Sorry, that's wrong. Final score:'
# TODO create a counter for final score

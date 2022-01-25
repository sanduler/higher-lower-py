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

# select a random playerin the dictionary
PLAYER_1 = random.choice(data)
PLAYER_2 = random.choice(data)


def compare():
    if PLAYER_1['follower_count'] > PLAYER_2['follower_count']:
        return True
    else:
        return False


def game():
    counter = 0
    # print logo
    print(logo)
    # print the random player1 description
    print(
        f"Compare A: {PLAYER_1['name']}, a {PLAYER_1['description']} from {PLAYER_1['country']}")
    # print the vs logo
    print(vs)
    # select a random playerin the dictionary
    # print the random player1 description
    print(
        f"Compare B: {PLAYER_2['name']}, a {PLAYER_2['description']} from {PLAYER_2['country']}")

    choice = input("Who has more followers? Type 'A' or 'B': ")

    if choice == 'A' and compare() == True:
        counter += 1
    elif choice == 'B' and compare() == True:
        counter += 1
    elif choice == 'A' and compare() == False:
        print("You lost!")
    else:
        print("You lost!")

    print(counter)


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

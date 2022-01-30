from consts import *
from util import *
from solver import *
import sys


#############
# Text mode #
#############
def text_mode(gc):
    print("Starting new game, text mode")
    game_over = False
    while not game_over:
        print_cards(gc.cards_in_play)
        selected_cards = get_input(gc)

        print("Selected Cards:")
        print(selected_cards)
        if len(selected_cards) == 3:
            if check_set(selected_cards):
                gc.cards_in_play = gc.replace_cards(selected_cards,gc.new_deal())
                print("It is a set! {0} cards remaining in deck".format(len(gc.deck)))
            else:
                print("Not a set, please try again!")
        elif selected_cards == '0':
            if not gc.skip():
                print("Game Over, no valid combination anymore!")
                sys.exit(0)
        else:
            print("Invalid Input, please try again!")
        game_over = len(gc.cards_in_play) == 0


def get_input(gc):
    cards = gc.cards_in_play
    if AUTOMATED:
        # valid_combinations = try_combination(cards)  # If we were to use lib_solver we use this
        valid_combinations=solve(gc.cards_in_play)
        if valid_combinations:
            print("A: ", valid_combinations[0])
            return valid_combinations[0]
            # For original solvers_check method!
            # print("A: ", valid_combinations[0][0])
            # return valid_combinations[0][0]
            
        else:
            print("No combination found, asking for skipping!")
            return '0'
    else:
        return get_user_input(cards)
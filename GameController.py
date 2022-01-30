from consts import *
from Card import *
from util import check_set
import random


class GameController:
    def __init__(self):
        self.cards_in_play = []
        self.deck = self.generate_deck()
        self.first_deal()

    def generate_deck(self):
        deck = []
        count = 0
        for colour in COLOURS:
            for quantity in QUANTITIES:
                for form in FORMS:
                    for plenty in PLENTIES:
                        count += 1
                        deck.append(Card('Card' + str(count), colour, quantity, form, plenty))
        return deck

    def first_deal(self):
        choices = random.sample(self.deck, k=TABLE_SIZE)
        self.cards_in_play.extend(choices)
        for choice in choices:
            self.deck.remove(choice)

    # TODO: make sample variable!
    def new_deal(self, set_size=SET_SIZE):
        choices = []
        if 0 < len(self.deck):
            choices = random.sample(self.deck, k=set_size)

        for choice in choices:
            self.deck.remove(choice)
        # self.deck = [self.deck.remove(c) for c in choices]
        return choices

    def replace_cards(self, selected_cards, new_cards):
        # TODO: very bad style and not pythonic
        count = 0
        new_cards_in_play = []
        for card_in_play in self.cards_in_play:
            if card_in_play in selected_cards:
                if new_cards:
                    new_cards_in_play.append(new_cards[count])
                    count += 1
            else:
                new_cards_in_play.append(card_in_play)
        return new_cards_in_play

    def remove_set(self, selected_cards):
        new_cards = self.new_deal()
        if check_set(selected_cards):
            self.cards_in_play = self.replace_cards(selected_cards, new_cards)
            return True
        return False

    def skip(self):
        skip_range = 3
        cards_to_skip = random.sample(self.cards_in_play, k=skip_range)
        new_deal = self.new_deal()
        if new_deal:
            self.cards_in_play = self.replace_cards(cards_to_skip, new_deal)
            return True
        return False

    def info_text(self, selected_cards):
        if check_set(selected_cards):
            return 'Its a SET! Go on'
        else:
            return 'No SET! Try again'

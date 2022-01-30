from consts import *
from util import *

def solve(cards_in_play):
    # make all combo
    combos = combo_of_each_set_per_deal(cards_in_play)

    # use all combos to get valid combos
    solved = []
    for card1, card2, card3 in combos:
        #FIXME ?hier wird vorläufig die alte check Funktion gerufen
        if check_set([card1,card2,card3]):
            solved.append([card1,card2,card3])
    #TODO print the reason of valid SET!
        # a = solvers_check_set(card1, card2, card3)
        # if a:
        #     solved.append(a)
    
    return solved

def solvers_check_set(card1, card2, card3):
    list_sets = []
    setA = set((card1.colour, card1.form, card1.plenty, card1.quantity))
    setB = set((card2.colour, card2.form, card2.plenty, card2.quantity))
    setC = set((card3.colour, card3.form, card3.plenty, card3.quantity))
    # hier werden alle Elemente gespeichert, die eine Differenzmenge bilden mathematisch gesehen A ∆ B, B ∆ C, A ∆ C
    difference1, difference2, difference3 = \
        setA.symmetric_difference(setB), setB.symmetric_difference(setC), setA.symmetric_difference(setC)

    set_differences = difference1.union(difference2, difference3)

    # hier werden die Schnittmengen gebildet Mathematisch gesehen A u B, B u C, A u C
    gemeinsamkeitenA, gemeinsamkeitenB, gemeinsamkeitenC = \
        setA.intersection(setB), setB.intersection(setC), setA.intersection(setC)

    # hier werden die Schnittmengen vereint
    set_gemeinsamkeiten = gemeinsamkeitenA.union(gemeinsamkeitenB, gemeinsamkeitenC)

    if 3 * len(set_gemeinsamkeiten) + len(set_differences) == 12:
        if DEBUG:
            print('Yes we have a set ' + str(card1) + str(card2) + str(card3)
                    + '\nThis is a set because we have this similarities\n' + str(set_gemeinsamkeiten)
                    + '\nAnd the everything else is different ' + str(set_differences))
        list_sets.append([card1, card2, card3])
    else:
        reason_no_set = set_gemeinsamkeiten.intersection(set_differences)
        if DEBUG:
            print('Sorry this combinations is no set we found this element ' + str(reason_no_set)
                    + ' just in two cards which is a no go for sets: {'
                    + str(card1) + ", " + str(card2) + ", " + str(card3) + "}")
    return list_sets

def combo_of_each_set_per_deal(play_cards):
    list_variation_playing_cards = [[play_cards[i], play_cards[j], play_cards[k]]
                                    for i in range(len(play_cards))
                                    for j in range(len(play_cards))
                                    for k in range(len(play_cards))
                                    if i != j and i != k and j != k if i < j and i < k and j < k]

    return list_variation_playing_cards


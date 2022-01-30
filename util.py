from Card import Card

def print_cards(cards: list[Card]):
    print('---------------------------------------------')
    for c in cards:
        padding = 30 - len(c.__str__())
        print('| ', c,' ' * padding , ' |')
    print('---------------------------------------------')

def get_user_input(cards_in_play):
    user_input = input("Please select 3 selected_cards(comma separated):")

    selected_cards = user_input.split(',')
    selected_cards = sorted(selected_cards, reverse=True)
    
    # Validation
    selected_cards = [s for s in cards_in_play if s.name in selected_cards]
    if len(selected_cards) == 3 and not(selected_cards[0] == selected_cards[1] == selected_cards[2]):
        return selected_cards
    return None

'''Returns a numbers position, as a tuple (row, col) e.g. number 4 is second row (counting starts with 0, so 1) and second column: 1,0'''
def get_pos(num):
    return (num // 3, num % 3)


def check_set(cards) -> bool:
    if len(cards) != 3:
        return False

    card1, card2, card3 = cards[0], cards[1], cards[2]
    pro_set = 1 if card1.colour == card2.colour == card3.colour else 0
    pro_set += 1 if card1.form == card2.form == card3.form else 0
    pro_set += 1 if card1.plenty == card2.plenty == card3.plenty else 0
    pro_set += 1 if card1.quantity == card2.quantity == card3.quantity else 0
    if pro_set >= 3:

        return True
    
    anti_set = 1 if card1.colour != card2.colour != card3.colour  and card1.colour != card3.colour else 0
    anti_set += 1 if card1.form != card2.form != card3.form  and card1.form != card3.form else 0
    anti_set += 1 if card1.plenty != card2.plenty != card3.plenty  and card1.plenty != card3.plenty else 0
    anti_set += 1 if card1.quantity != card2.quantity != card3.quantity  and card1.quantity != card3.quantity else 0
    if (anti_set == 3 and pro_set == 1) or anti_set == 4 :

        return True

    return False
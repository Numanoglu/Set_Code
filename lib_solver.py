from itertools import combinations
from util import check_set


def try_combination(cards):
    valid_combo = []
    for comb in combinations(cards, 3):
        if check_set(comb):
            valid_combo.append(comb)
    return valid_combo

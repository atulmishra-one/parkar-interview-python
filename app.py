"""
@author atulmishra.one@gmail.com
@usage python app.py zaay zaac
"""

import re
from collections import Counter
from collections import defaultdict

words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', \
         'w', 'x', 'y', 'z']

words.sort(reverse=True)


def validate_player(value):
    if not isinstance(value, str):
        raise TypeError('Please enter only string')
    return value


def validate_minimum_required(value):
    if len(value) < 1:
        raise ValueError('Please enter minimum one character for player.')
    return value


def declare_draw_if_no(player_one, player_two):
    """
    Return True to continue
    """

    if player_one.find('no') > 1:
        return None
    elif player_two.find('no') > 1:
        return None
    else:
        return True


def declare_draw_if_number_or_symbol(player_one, player_two):
    """
    Return True to continue
    """

    player_one_int = [int(s) for s in player_one if s.isdigit()]

    player_two_int = [int(s) for s in player_two if s.isdigit()]

    player_one_sym = re.match(r'^[a-zA-Z0-9]*$', player_one)

    player_two_sym = re.match(r'^[a-zA-Z0-9]*$', player_two)

    if len(player_one_int) or not player_one_sym:
        return None
    elif len(player_two_int) or not player_two_sym:
        return None
    else:
        return True


def get_winner(player_one, player_two):
    player_a = Counter(player_one).most_common()
    player_b = Counter(player_two).most_common()

    a = defaultdict(list)
    for i in player_a:
        a[i[0]] = i[1]

    b = defaultdict(list)
    for i in player_b:
        b[i[0]] = i[1]

    max_value_a = max(a.values())
    max_value_b = max(b.values())

    for i, v in enumerate(words):
        if words[0] in a.keys() and a[v] == max_value_a:
            return player_one
        elif words[0] in a.keys() and words[0] in b.keys() and b[v] == max_value_b and a[v] == max_value_a:
            if words[1] in a.keys() and a[v] == max_value_a:
                return player_one
            else:
                return None
        elif words[0] in a.keys() and words[1] == max_value_a:
            return player_one
        else:
            return None

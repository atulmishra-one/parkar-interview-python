"""
@author atulmishra.one@gmail.com
@usage python app.py zaay zaac
"""

import re
import sys

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


def get_players_strings(string_name, player):
    strings = []
    for z in player:
        if z == string_name:
            strings.append(z)
    return strings


def get_valid_strings_of_player(player):
    result = []
    for i in words:
        chars = get_players_strings(i, player)
        if chars:
            result.append(chars)
        else:
            continue
    return chars


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
    winner = None
    for i in words:
        ch1 = get_players_strings(i, player_one)
        if not ch1 or len(ch1) == 1:
            continue

    for i in words:
        ch2 = get_players_strings(i, player_two)
        if not ch2 or len(ch2) == 1:
            continue

    if not declare_draw_if_number_or_symbol(player_one, player_two):
        winner = None
    elif not declare_draw_if_no(player_one, player_two):
        winner = None
    elif not len(ch1) and not len(ch2):
        winner = None
    elif len(ch1) == len(ch2):
        winner = player_one
    elif not winner:
        winner = player_two
    return winner

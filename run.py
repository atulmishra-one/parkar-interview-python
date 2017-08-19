import sys
from app import *

if __name__ == '__main__':
    player_one = validate_player(sys.argv[1])
    player_two = validate_player(sys.argv[2])

    validate_minimum_required(player_one)
    validate_minimum_required(player_two)

    print("==::Starting Game With Player one : {0} And Player two : {1}::==".format(player_one, player_two), end="\n")

    draw = declare_draw_if_no(player_one, player_two)
    draw = declare_draw_if_number_or_symbol(player_one, player_two)

    the_winner = get_winner(player_one, player_two)

    if draw is not None and the_winner:
        print("Congratulations! You win {}".format(the_winner))
    else:
        print("Game Drawn")

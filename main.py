import sys
import re

input1 = sys.argv[1]
input2 = sys.argv[2]

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

player_one = validate_player(sys.argv[1])
player_two = validate_player(sys.argv[2])

validate_minimum_required(player_one)
validate_minimum_required(player_two)

def declare_draw_if_no(player_one, player_two):
    """
    Return True to continue
    """

    if player_one.find('no') >= 1:
        return None
    elif player_two.find('no') >= 1:
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

if not declare_draw_if_number_or_symbol(player_one, player_two):
        print("Draw")
	sys.exit()
elif not declare_draw_if_no(player_one, player_two):
        print("Draw")
	sys.exit()

for i in words:
	if i in input1 and i not in input2:
		print("Winner {0}".format(input1))
		break
	if i in input2 and i not in input1:
		print("Winner {0}".format(input2))
		break
	if i in input1 and i in input2:
		if input1.count(i) > input2.count(i):
			print("Winner {0}".format(input1))
			break
		if input1.count(i) < input2.count(i):
			print("Winner {0}".format(input2))
			break
		if input1.count(i) == input2.count(i):
			continue

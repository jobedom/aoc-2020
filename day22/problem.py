import re

from misc import init_day
from input import get_file_contents

init_day(__file__, 22)


def parse_input(input):
    input = re.sub(r'.*Player 1:', '', input)
    deck_1_string, deck_2_string = input.split('Player 2:')
    deck_1 = [int(number) for number in re.findall(r'\d+', deck_1_string)]
    deck_2 = [int(number) for number in re.findall(r'\d+', deck_2_string)]
    return deck_1, deck_2


def deck_points(deck):
    deck_length = len(deck)
    return sum((deck_length - index) * card for index, card in enumerate(deck))


def solve_part_1(input):
    deck_1, deck_2 = parse_input(input)
    while len(deck_1) > 0 and len(deck_2) > 0:
        card_1 = deck_1.pop(0)
        card_2 = deck_2.pop(0)
        if card_1 > card_2:
            deck_1 += [card_1, card_2]
        else:
            deck_2 += [card_2, card_1]
    return deck_points(deck_1 or deck_2)


def solve_part_2(input):
    def recursive_combat(deck_1, deck_2):
        seen_worlds = set()
        while deck_1 and deck_2:
            world = (tuple(deck_1), tuple(deck_2))
            if world in seen_worlds:
                return 1
            seen_worlds.add(world)
            card_1 = deck_1.pop(0)
            card_2 = deck_2.pop(0)
            if len(deck_1) >= card_1 and len(deck_2) >= card_2:
                winner = recursive_combat(deck_1[:card_1], deck_2[:card_2])
            else:
                winner = 1 if card_1 > card_2 else 2
            if winner == 1:
                deck_1 += [card_1, card_2]
            else:
                deck_2 += [card_2, card_1]
        return 1 if deck_1 else 2

    deck_1, deck_2 = parse_input(input)
    recursive_combat(deck_1, deck_2)
    return deck_points(deck_1 or deck_2)


test_input = get_file_contents('test.txt')
problem_input = get_file_contents('input.txt')

assert solve_part_1(test_input) == 306
part_1_response = solve_part_1(problem_input)
print(f'Part 1: {part_1_response}')

assert solve_part_2(test_input) == 291
part_2_response = solve_part_2(problem_input)
print(f'Part 2: {part_2_response}')

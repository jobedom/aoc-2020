import re
from functools import reduce
from collections import Counter

from misc import init_day
from input import get_file_lines_with_no_blanks

init_day(__file__, 24)

MOVEMENT_DELTAS = {
    'e': (1, 0),
    'w': (-1, 0),
    'ne': (0, 1),
    'sw': (0, -1),
    'se': (1, -1),
    'nw': (-1, 1),
}


def sum_coords(coord_1, coord_2):
    return (coord_1[0] + coord_2[0], coord_1[1] + coord_2[1])


def sum_all_coords(coords_list):
    return reduce(sum_coords, coords_list, (0, 0))


def get_blacks_for_movements(input):
    movements = [re.findall(r'se|sw|nw|ne|e|w', line) for line in input]
    flips = Counter(sum_all_coords([MOVEMENT_DELTAS[direction] for direction in movement]) for movement in movements)
    return {position for position, flip_count in flips.items() if flip_count % 2 == 1}


def solve_part_1(input):
    return len(get_blacks_for_movements(input))


def solve_part_2(input):
    blacks = get_blacks_for_movements(input)
    for _ in range(100):
        neighbour_counts = Counter(
            sum_coords(coords, deltas) for coords in blacks for deltas in MOVEMENT_DELTAS.values()
        )
        blacks = set(
            position for position, neighbour_count in neighbour_counts.items()
            if neighbour_count == 2 or position in blacks and neighbour_count == 1
        )
    return len(blacks)


test_input = get_file_lines_with_no_blanks('test.txt')
problem_input = get_file_lines_with_no_blanks('input.txt')

assert solve_part_1(test_input) == 10
part_1_response = solve_part_1(problem_input)
print(f'Part 1: {part_1_response}')

assert solve_part_2(test_input) == 2208
part_2_response = solve_part_2(problem_input)
print(f'Part 2: {part_2_response}')

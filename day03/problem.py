import math

from misc import init_day
from input import get_file_lines

init_day(__file__, 3)

forest = get_file_lines('./input.txt')


def get_tree_count(slope_horizontal, slope_vertical):
    tree_count = 0
    pos = 0
    for index, row in enumerate(forest):
        if index % slope_vertical == 0:
            if row[pos] == '#':
                tree_count += 1
            pos = (pos + slope_horizontal) % len(row)
    return tree_count


result_1 = get_tree_count(3, 1)
result_2 = math.prod(get_tree_count(h, v) for (h, v) in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)])

print(f'Part 1: {result_1}')
print(f'Part 2: {result_2}')

import re

from misc import init_day
from lists import list_difference
from input import get_file_lines_with_no_blanks

init_day(__file__, 5)


def get_boarding_pass_id(boarding_pass):
    return int(re.sub(r'[FL]', '0', re.sub(r'[BR]', '1', boarding_pass)), 2)


def solve_part_1(boarding_passes):
    return max(get_boarding_pass_id(boarding_pass) for boarding_pass in boarding_passes)


def solve_part_2(boarding_passes):
    boarding_pass_ids = [get_boarding_pass_id(boarding_pass) for boarding_pass in boarding_passes]
    full_plane_ids = list(range(0, 2 ** len(boarding_passes[0])))
    missing_ids = list_difference(full_plane_ids, boarding_pass_ids)
    for boarding_pass_id in missing_ids:
        if (boarding_pass_id - 1) in boarding_pass_ids and (boarding_pass_id + 1) in boarding_pass_ids:
            return boarding_pass_id


boarding_passes_test_1 = get_file_lines_with_no_blanks('test1.txt')
assert (solve_part_1(boarding_passes_test_1) == 820)

boarding_passes_input = get_file_lines_with_no_blanks('input.txt')

result_part_1 = solve_part_1(boarding_passes_input)
print(f'Part 1: {result_part_1}')

result_part_2 = solve_part_2(boarding_passes_input)
print(f'Part 2: {result_part_2}')

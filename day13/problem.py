from math import prod

from misc import init_day
from input import get_file_lines_with_no_blanks

init_day(__file__, 13)


def solve_part_1(timestamp, ids_text):
    ids = [int(id) for id in ids_text.split(',') if id != 'x']
    ids_with_remainders = [(id, id - (timestamp % id)) for id in ids]
    good_id, good_wait_time = min(ids_with_remainders, key=lambda item: item[1])
    return good_id * good_wait_time


def solve_part_2(ids_text):
    def chinese_remainder(divisors, remainders):
        #  Chinese remainder will give a number that when divided by some divisors leaves certain remainders.
        product = prod(divisors)
        return sum(r * pow(product // d, -1, d) * (product // d) for d, r in zip(divisors, remainders)) % product

    ids = [0 if id == 'x' else int(id) for id in ids_text.split(',')]
    buses = [(index, id) for index, id in enumerate(ids) if id != 0]
    actual_ids = [id for id in ids if id != 0]
    bus_offsets = [timestamp - index for index, timestamp in buses]
    return chinese_remainder(actual_ids, bus_offsets)


test_input = get_file_lines_with_no_blanks('test.txt')
test_timestamp, test_ids_text = int(test_input[0]), test_input[1]

assert solve_part_1(test_timestamp, test_ids_text) == 295

assert solve_part_2('7,13,x,x,59,x,31,19') == 1068781
assert solve_part_2('17,x,13,19') == 3417
assert solve_part_2('67,7,59,61') == 754018
assert solve_part_2('67,x,7,59,61') == 779210
assert solve_part_2('67,7,x,59,61') == 1261476
assert solve_part_2('1789,37,47,1889') == 1202161486

problem_input = get_file_lines_with_no_blanks('input.txt')
timestamp, ids_text = int(problem_input[0]), problem_input[1]

part_1_response = solve_part_1(timestamp, ids_text)
print(f'Part 1: {part_1_response}')

part_2_response = solve_part_2(ids_text)
print(f'Part 2: {part_2_response}')

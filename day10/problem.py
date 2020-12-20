from functools import cache

from misc import init_day
from input import get_file_numbers

init_day(__file__, 10)


def solve_part_1(part1_input):
    adaptors = sorted(part1_input[:])
    adaptors.append(max(adaptors) + 3)
    joltage = 0
    previous_joltage = 0
    diff_count = {1: 0, 3: 0}
    while len(adaptors) > 0:
        next_adaptor = next(adaptor for adaptor in adaptors if (adaptor - joltage) in [1, 3])
        adaptors.remove(next_adaptor)
        joltage = next_adaptor
        diff_count[joltage - previous_joltage] += 1
        previous_joltage = joltage
    return diff_count[1] * diff_count[3]


def solve_part_2(part2_input):
    @cache
    def get_combinations(joltage, candidate_adaptors, ignore_adaptor=-1):
        next_adaptors = tuple(
            [
                adaptor for adaptor in candidate_adaptors
                if (1 <= adaptor - joltage <= 3) and (adaptor != ignore_adaptor)
            ]
        )
        if len(next_adaptors) == 0:
            return 1
        return sum(get_combinations(next_adaptor, candidate_adaptors, next_adaptor) for next_adaptor in next_adaptors)

    adaptors = sorted(part2_input[:])
    adaptors.append(max(adaptors) + 3)
    return get_combinations(0, tuple(adaptors))


test_1_input = get_file_numbers('test1.txt')
test_2_input = get_file_numbers('test2.txt')
assert solve_part_1(test_1_input) == 35
assert solve_part_1(test_2_input) == 220
assert solve_part_2(test_1_input) == 8
assert solve_part_2(test_2_input) == 19208

problem_input = get_file_numbers('input.txt')
part_1_response = solve_part_1(problem_input)
part_2_response = solve_part_2(problem_input)
print(f'Part 1: {part_1_response}')
print(f'Part 2: {part_2_response}')

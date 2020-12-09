from misc import init_day
from input import get_file_numbers

init_day(__file__, 9)


def solve_part_1(part1_input, preamble_length):
    def any_pair_sums(collection, target_sum):
        collection_length = len(collection)
        for i in range(0, collection_length - 1):
            for j in range(i + 1, collection_length):
                if collection[i] + collection[j] == target_sum:
                    return True
        return False

    for block_start in range(0, len(part1_input) - preamble_length):
        block = part1_input[block_start:block_start + preamble_length]
        number = part1_input[block_start + preamble_length]
        if not any_pair_sums(block, number):
            return number
    raise Exception('Part 1 is unsolvable!')


def solve_part_2(part1_input, target):
    input_length = len(part1_input)
    for block_size in range(2, input_length):
        for block_start in range(0, input_length - block_size + 1):
            block = part1_input[block_start:block_start + block_size]
            if sum(block) == target:
                return min(block) + max(block)
    raise Exception('Part 2 is unsolvable!')


test_input = get_file_numbers('test.txt')
assert solve_part_1(test_input, 5) == 127
assert solve_part_2(test_input, 127) == 62

problem_input = get_file_numbers('input.txt')
part_1_response = solve_part_1(problem_input, 25)
part_2_response = solve_part_2(problem_input, part_1_response)
print(f'Part 1: {part_1_response}')
print(f'Part 2: {part_2_response}')

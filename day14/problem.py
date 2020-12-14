import re
from collections import defaultdict

from misc import init_day
from input import get_file_lines_with_no_blanks

init_day(__file__, 14)


def transform_mask(mask, transform_map):
    return ''.join([transform_map.get(char, char) for char in mask])


def solve_part_1(problem_input):
    mem = defaultdict(int)
    for line in problem_input:
        mask_matches = re.match(r'^mask\s*=\s*([X01]{36})$', line)
        if mask_matches:
            mask = mask_matches.group(1)
            and_mask = int(transform_mask(mask, {'X': '1', '1': '0', '0': '0'}), 2)
            or_mask = int(transform_mask(mask, {'X': '0', '1': '1', '0': '0'}), 2)
        else:
            assign_matches = re.match(r'^mem\[(\d+)\]\s*=\s*(\d+)$', line)
            if assign_matches:
                mem_pos = int(assign_matches.group(1))
                mem_value = int(assign_matches.group(2))
                mem[mem_pos] = (mem_value & and_mask) | or_mask
    return sum(mem.values())


def solve_part_2(problem_input):
    mem = defaultdict(int)
    for line in problem_input:
        mask_matches = re.match(r'^mask\s*=\s*([X01]{36})$', line)
        if mask_matches:
            mask = mask_matches.group(1)
            and_mask = int(transform_mask(mask, {'0': '1', '1': '0', 'X': '0'}), 2)
            or_mask_string = transform_mask(mask, {'0': '0', '1': '1'})
        else:
            assign_matches = re.match(r'^mem\[(\d+)\]\s*=\s*(\d+)$', line)
            if assign_matches:
                mem_pos = int(assign_matches.group(1))
                mem_value = int(assign_matches.group(2))
                num_floating = len([char for char in or_mask_string if char == 'X'])
                for floating_bits_val in range(0, 2**num_floating):
                    floating_bits = f'{floating_bits_val:b}'
                    while len(floating_bits) < num_floating:
                        floating_bits = f'0{floating_bits}'
                    floating_or_mask_string = or_mask_string
                    while floating_bits:
                        floating_or_mask_string = floating_or_mask_string.replace('X', floating_bits[0], 1)
                        floating_bits = floating_bits[1:]
                    floating_or_mask = int(floating_or_mask_string, 2)
                    actual_mem_pos = (mem_pos & and_mask) | floating_or_mask
                    mem[actual_mem_pos] = mem_value
    return sum(mem.values())


test_input_1 = get_file_lines_with_no_blanks('test1.txt')
assert solve_part_1(test_input_1) == 165

test_input_2 = get_file_lines_with_no_blanks('test2.txt')
assert solve_part_2(test_input_2) == 208

problem_input = get_file_lines_with_no_blanks('input.txt')
part_1_response = solve_part_1(problem_input)
part_2_response = solve_part_2(problem_input)
print(f'Part 1: {part_1_response}')
print(f'Part 2: {part_2_response}')

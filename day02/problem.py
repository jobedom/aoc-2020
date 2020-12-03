import sys
import re

from misc import init
from input import get_file_lines

init(__file__, 2)

test_pattern = re.compile(r'^(\d+)-(\d+)\s+(\w)\s*:\s*(\w+)$')

lines = get_file_lines('./input.txt')
parsed_list = []
for line in lines:
    matches = test_pattern.match(line)
    if matches is None:
        print(f'Wrong test line: {line}')
        sys.exit(1)
    (num1, num2, letter, sequence) = matches.groups()
    parsed_list.append((int(num1), int(num2), letter, sequence))

valid_count_part1 = 0
for (num1, num2, letter, sequence) in parsed_list:
    count_letter = len([char for char in sequence if char == letter])
    if num1 <= count_letter <= num2:
        valid_count_part1 += 1
print(f'Part 1: {valid_count_part1}')

valid_count_part2 = 0
for (num1, num2, letter, sequence) in parsed_list:
    count_letter = len([char for char in sequence if char == letter])
    if (sequence[num1 - 1] == letter) != (sequence[num2 - 1] == letter):
        valid_count_part2 += 1
print(f'Part 2: {valid_count_part2}')

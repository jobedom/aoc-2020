from misc import init
from input import get_file_numbers
from indexes import unique_index_pairs, unique_index_triplets

init(__file__, 1)

numbers = get_file_numbers('./input.txt')
number_count = len(numbers)

for i, j in unique_index_pairs(number_count):
    if numbers[i] + numbers[j] == 2020:
        print(f'Part 1: {numbers[i] * numbers[j]}')
        break

for i, j, k in unique_index_triplets(number_count):
    if numbers[i] + numbers[j] + numbers[k] == 2020:
        print(f'Part 2: {numbers[i] * numbers[j] * numbers[k]}')
        break

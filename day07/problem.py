import re

from misc import init_day
from input import get_file_lines_with_no_blanks

init_day(__file__, 7)


def contains_bag(definitions, container, bag):
    if container == bag:
        return True
    container_definition = definitions[container]
    for number, contained_bag in container_definition:
        if contains_bag(definitions, contained_bag, bag):
            return True
    return False


def bag_contents_count(definitions, bag):
    def bag_contents_count_rec(definitions, bag):
        container_definition = definitions[bag]
        return 1 + sum(number * bag_contents_count_rec(definitions, contained_bag)
                       for number, contained_bag in container_definition)

    return bag_contents_count_rec(definitions, bag) - 1


def get_bags_definition(input):
    result = {}
    for line in input:
        matches = re.match(r'^(.+?)\s+bags contain\s+', line)
        if not matches:
            raise ValueError(f'Wrong formatted line "{line}"')
        container_bag = matches.group(1)
        matches = re.findall(r'(\d+)\s+(.+?)\s+bags?', line)
        result[container_bag] = [(int(match[0]), match[1]) for match in matches]
    return result


def solve_part_1(input):
    bag = 'shiny gold'
    bags_definition = get_bags_definition(input)
    return len([
        container for container in bags_definition.keys()
        if container != bag and contains_bag(bags_definition, container, bag)
    ])


def solve_part_2(input):
    bags_definition = get_bags_definition(input)
    return bag_contents_count(bags_definition, 'shiny gold')


test_input_1 = get_file_lines_with_no_blanks('test1.txt')
test_input_2 = get_file_lines_with_no_blanks('test2.txt')

assert solve_part_1(test_input_1) == 4
assert solve_part_2(test_input_1) == 32
assert solve_part_2(test_input_2) == 126

problem_input = get_file_lines_with_no_blanks('input.txt')

print(f'Part 1: {solve_part_1(problem_input)}')
print(f'Part 2: {solve_part_2(problem_input)}')

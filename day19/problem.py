import re

from misc import init_day
from input import get_file_lines_with_no_blanks

init_day(__file__, 19)


def parse_input(input):
    rules = {}
    messages = []
    for line in input:
        if ':' in line:
            rule_id, rule_content = line.split(': ')
            rule_id = int(rule_id)
            if '"' in rule_content:
                rules[rule_id] = rule_content[1]
            else:
                elements = [part.strip() for part in rule_content.split('|')]
                rules[rule_id] = [[int(item) for item in element.split(' ')] for element in elements]
        else:
            messages.append(line)
    return rules, messages


def message_matches(message, rules, rules_list):
    if message == '' or rules_list == []:
        return message == '' and rules_list == []
    rule = rules[rules_list[0]]
    if isinstance(rule, str):
        if message[0] in rule:
            return message_matches(message[1:], rules, rules_list[1:])
        return False
    else:
        return any(message_matches(message, rules, item + rules_list[1:]) for item in rule)


def solve_part_1(input):
    rules, messages = parse_input(input)
    return sum(message_matches(message, rules, [0]) for message in messages)


def solve_part_2(input):
    rules, messages = parse_input(input)
    rules[8] = [[42], [42, 8]]
    rules[11] = [[42, 31], [42, 11, 31]]
    return sum(message_matches(message, rules, [0]) for message in messages)


test_input_1 = get_file_lines_with_no_blanks('test1.txt')
test_input_2 = get_file_lines_with_no_blanks('test2.txt')
assert solve_part_1(test_input_1) == 2
assert solve_part_1(test_input_2) == 2

problem_input = get_file_lines_with_no_blanks('input.txt')
part_1_response = solve_part_1(problem_input)
part_2_response = solve_part_2(problem_input)
print(f'Part 1: {part_1_response}')
print(f'Part 2: {part_2_response}')

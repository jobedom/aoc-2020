from misc import init_day
from lists import list_intersection
from input import get_file_lines

init_day(__file__, 6)


def solve_part_1(part_answers):
    def get_group_answers(answer_list):
        answer_list.append('')
        result = []
        chars = ''
        for line in answer_list:
            if line == '':
                result.append(''.join(set(chars)))
                chars = ''
            else:
                chars = chars + line
        return result

    group_answers = get_group_answers(part_answers)
    return sum(len(group) for group in group_answers)


def solve_part_2(part_answers):
    def get_group_answers(answer_list):
        answer_list.append('')
        result = []
        chars = ''
        for line in answer_list:
            if line == '':
                result.append(chars)
                chars = ''
            else:
                if chars == '':
                    chars = line
                else:
                    chars = list_intersection(chars, line)
        return result

    group_answers = get_group_answers(part_answers)
    return sum(len(group) for group in group_answers)


test_answers = get_file_lines('test.txt')

assert solve_part_1(test_answers) == 11
assert solve_part_2(test_answers) == 6

answers = get_file_lines('input.txt')

print(f'Part 1: {solve_part_1(answers)}')
print(f'Part 2: {solve_part_2(answers)}')

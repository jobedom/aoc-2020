import re
import math

from misc import init_day
from input import get_file_lines_with_no_blanks

init_day(__file__, 18)


def tokenize(text):
    return [int(item) if item.isdigit() else item for item in re.findall(r'(\d+|\(|\)|[+*])', text)]


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.count() == 0

    def not_empty(self):
        return not self.is_empty()

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def count(self):
        return len(self.items)

    def __repr__(self):
        return ', '.join(str(item) for item in self.items)


def evaluate_expression(expression, operator_precedences):
    expression = re.sub(r'([\(\)])', r' \1 ', expression)
    expression = re.sub(r'\s+', r' ', expression)
    tokens = expression.split()

    operations = {
        '+': lambda x, y: x + y,
        '*': lambda x, y: x * y,
    }

    precedences = {'(': 0, ')': 0} | operator_precedences
    operator_stack = Stack()
    operand_stack = Stack()
    for token in tokens:
        if token.isdigit():
            operand_stack.push(token)
        elif token == '(':
            operator_stack.push(token)
        elif token == ')':
            while operator_stack.not_empty() and operator_stack.peek() != '(':
                operator = operator_stack.pop()
                value_1 = int(operand_stack.pop())
                value_2 = int(operand_stack.pop())
                operand_stack.push(operations[operator](value_1, value_2))
            operator_stack.pop()
        else:
            while operator_stack.not_empty() and precedences[operator_stack.peek()] >= precedences[token]:
                operator = operator_stack.pop()
                value_1 = int(operand_stack.pop())
                value_2 = int(operand_stack.pop())
                result = operations[operator](value_1, value_2)
                operand_stack.push(result)
            operator_stack.push(token)
    while operator_stack.not_empty():
        operator = operator_stack.pop()
        value_1 = int(operand_stack.pop())
        value_2 = int(operand_stack.pop())
        operand_stack.push(operations[operator](value_1, value_2))
    return operand_stack.pop()


def evaluate_expression_part_1(expression):
    return evaluate_expression(expression, {'+': 1, '*': 1})


def solve_part_1(problem_input):
    return sum(evaluate_expression_part_1(line) for line in problem_input)


def evaluate_expression_part_2(expression):
    return evaluate_expression(expression, {'+': 2, '*': 1})


def solve_part_2(problem_input):
    return sum(evaluate_expression_part_2(line) for line in problem_input)


assert evaluate_expression_part_1('1 + 2 * 3 + 4 * 5 + 6') == 71
assert evaluate_expression_part_1('5 + 7 * 3 + 2') == 38
assert evaluate_expression_part_1('1 + (2 * 3) + (4 * (5 + 6))') == 51
assert evaluate_expression_part_1('2 * 3 + (4 * 5)') == 26
assert evaluate_expression_part_1('5 + (8 * 3 + 9 + 3 * 4 * 3)') == 437
assert evaluate_expression_part_1('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))') == 12240
assert evaluate_expression_part_1('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2') == 13632

problem_input = get_file_lines_with_no_blanks('input.txt')
part_1_response = solve_part_1(problem_input)
part_2_response = solve_part_2(problem_input)
print(f'Part 1: {part_1_response}')
print(f'Part 2: {part_2_response}')

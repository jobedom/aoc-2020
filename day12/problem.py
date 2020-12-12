from misc import init_day
from input import get_file_lines_with_no_blanks

init_day(__file__, 12)


def parse_instructions(instructions_input):
    return [(line[0], int(line[1:])) for line in instructions_input]


direction_deltas = {
    'N': (0, -1),
    'S': (0, 1),
    'E': (1, 0),
    'W': (-1, 0),
}


def solve_part_1(instructions):
    x = 0
    y = 0
    heading_deltas = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    heading = 0
    for instruction, amount in instructions:
        dx, dy = 0, 0
        if instruction == 'R':
            heading = (heading + int(amount / 90.0) + 4) % 4
        elif instruction == 'L':
            heading = (heading - int(amount / 90.0) + 4) % 4
        elif instruction == 'F':
            dx, dy = heading_deltas[heading]
        else:
            dx, dy = direction_deltas[instruction]
        x += dx * amount
        y += dy * amount
    return abs(x) + abs(y)


def solve_part_2(instructions):
    ship_x = 0
    ship_y = 0
    waypoint_x = 10
    waypoint_y = -1
    for instruction, amount in instructions:
        if instruction == 'R':
            for rotation in range(0, int(amount / 90.0)):
                waypoint_x, waypoint_y = -waypoint_y, waypoint_x
        elif instruction == 'L':
            for rotation in range(0, int(amount / 90.0)):
                waypoint_x, waypoint_y = waypoint_y, -waypoint_x
        elif instruction == 'F':
            ship_x += waypoint_x * amount
            ship_y += waypoint_y * amount
        else:
            dx, dy = direction_deltas[instruction]
            waypoint_x += dx * amount
            waypoint_y += dy * amount
    return abs(ship_x) + abs(ship_y)


test_input = get_file_lines_with_no_blanks('test.txt')
test_instructions = parse_instructions(test_input)
assert solve_part_1(test_instructions) == 25
assert solve_part_2(test_instructions) == 286

problem_input = get_file_lines_with_no_blanks('input.txt')
problem_instructions = parse_instructions(problem_input)

part_1_response = solve_part_1(problem_instructions)
part_2_response = solve_part_2(problem_instructions)
print(f'Part 1: {part_1_response}')
print(f'Part 2: {part_2_response}')

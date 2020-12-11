from copy import deepcopy

from misc import init_day
from input import get_file_lines_with_no_blanks

init_day(__file__, 11)


def state_from_input(state_input):
    return [list(line) for line in state_input]


def printable_state(state):
    return '\n'.join([' '.join(row) for row in state]) + '\n\n'


def stable_state_after_iterations(state, next_state_generator):
    while True:
        state, changed = next_state_generator(state)
        if not changed:
            break
    return state


def count_occupied(state):
    return ''.join(''.join(row) for row in state).count('#')


def next_state(state, cell_transformer):
    height = len(state)
    width = max(len(row) for row in state)
    result = deepcopy(state)
    changed = False
    for row in range(0, height):
        for column in range(0, width):
            new_cell = cell_transformer(height, width, row, column)
            if new_cell is not None:
                result[row][column] = new_cell
                changed = True
    return result, changed


def next_state_part_1(state):
    def get_adjacent_occupied_count(current_state, height, width, i, j, match):
        matching_count = 0
        for dy in range(-1, 2):
            if i + dy < 0 or i + dy >= height:
                continue
            for dx in range(-1, 2):
                if (dx == 0 and dy == 0) or (j + dx < 0 or j + dx >= width):
                    continue
                if current_state[i + dy][j + dx] == match:
                    matching_count += 1
        return matching_count

    def cell_transformer(height, width, row, column):
        if state[row][column] == '.':
            return None
        adjacent_occupied_count = get_adjacent_occupied_count(state, height, width, row, column, '#')
        if state[row][column] == 'L' and adjacent_occupied_count == 0:
            return '#'
        elif state[row][column] == '#' and adjacent_occupied_count >= 4:
            return 'L'
        return None

    return next_state(state, cell_transformer)


def next_state_part_2(state):
    def get_seen_occupied_count(current_state, height, width, i, j, match):
        matching_count = 0
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                if dx == 0 and dy == 0:
                    continue
                moving_i = i + dy
                moving_j = j + dx
                while 0 <= moving_i < height and 0 <= moving_j < width:
                    cell = current_state[moving_i][moving_j]
                    if cell != '.':
                        if cell == match:
                            matching_count += 1
                        break
                    moving_i += dy
                    moving_j += dx
        return matching_count

    def cell_transformer(height, width, row, column):
        if state[row][column] == '.':
            return None
        seen_occupied_count = get_seen_occupied_count(state, height, width, row, column, '#')
        if state[row][column] == 'L' and seen_occupied_count == 0:
            return '#'
        elif state[row][column] == '#' and seen_occupied_count >= 5:
            return 'L'
        return None

    return next_state(state, cell_transformer)


def solve_part_1(state):
    return count_occupied(stable_state_after_iterations(state, next_state_part_1))


def solve_part_2(state):
    return count_occupied(stable_state_after_iterations(state, next_state_part_2))


test_input = get_file_lines_with_no_blanks('test.txt')
test_state = state_from_input(test_input)
assert solve_part_1(test_state) == 37
assert solve_part_2(test_state) == 26

problem_input = get_file_lines_with_no_blanks('input.txt')
problem_state = state_from_input(problem_input)
part_1_response = solve_part_1(problem_state)
part_2_response = solve_part_2(problem_state)
print(f'Part 1: {part_1_response}')
print(f'Part 2: {part_2_response}')

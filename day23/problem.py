from misc import init_day

init_day(__file__, 23)


def cups_clockwise_map(input, num_cups, move_count):
    cups = [int(cup) for cup in list(str(input))]
    if num_cups >= 10:
        cups += [cup for cup in range(10, num_cups + 1)]
    cup_clockwise_from = {}
    for index in range(num_cups):
        if index == num_cups - 1:
            cup_clockwise_from[cups[index]] = cups[0]
        else:
            cup_clockwise_from[cups[index]] = cups[index + 1]
    current = cups[0]
    for _ in range(move_count):
        pick_1 = cup_clockwise_from[current]
        pick_2 = cup_clockwise_from[pick_1]
        pick_3 = cup_clockwise_from[pick_2]
        cup_clockwise_from[current] = cup_clockwise_from[pick_3]
        destination = current - 1
        while destination in [pick_1, pick_2, pick_3] or destination < 1:
            destination -= 1
            if destination < 1:
                destination = num_cups
        cup_clockwise_from[pick_3] = cup_clockwise_from[destination]
        cup_clockwise_from[destination] = pick_1
        current = cup_clockwise_from[current]
    return cup_clockwise_from


def solve_part_1(input, num_cups, move_count):
    cup_clockwise_from = cups_clockwise_map(input, num_cups, move_count)
    result = ''
    cup = 1
    for _ in range(num_cups - 1):
        cup = cup_clockwise_from[cup]
        result += str(cup)
    return int(result)


def solve_part_2(input, num_cups, move_count):
    cup_clockwise_from = cups_clockwise_map(input, num_cups, move_count)
    return cup_clockwise_from[1] * cup_clockwise_from[cup_clockwise_from[1]]


assert solve_part_1(389125467, 9, 10) == 92658374
assert solve_part_1(389125467, 9, 100) == 67384529
part_1_response = solve_part_1(364289715, 9, 100)
print(f'Part 1: {part_1_response}')

assert solve_part_2(389125467, 1000000, 10000000) == 149245887792
part_2_response = solve_part_2(364289715, 1000000, 10000000)
print(f'Part 2: {part_2_response}')

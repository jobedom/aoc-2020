from misc import init_day

init_day(__file__, 15)


def get_numbers(numbers_list):
    return [int(n) for n in numbers_list.split(',')]


def solve(numbers_list, position):
    numbers = get_numbers(numbers_list)
    count = len(numbers)

    track = dict((number, index + 1) for index, number in enumerate(numbers))

    while count <= position:
        last_number = numbers[count - 1]
        tracked = track.get(last_number)
        if tracked:
            number = count - tracked
        else:
            number = 0
        track[last_number] = count
        numbers.append(number)
        count += 1
    return last_number


assert solve('0,3,6', 2020) == 436
assert solve('1,3,2', 2020) == 1
assert solve('2,1,3', 2020) == 10
assert solve('1,2,3', 2020) == 27
assert solve('2,3,1', 2020) == 78
assert solve('3,2,1', 2020) == 438
assert solve('3,1,2', 2020) == 1836

assert solve('0,3,6', 30000000) == 175594
assert solve('1,3,2', 30000000) == 2578
assert solve('2,1,3', 30000000) == 3544142
assert solve('1,2,3', 30000000) == 261214
assert solve('2,3,1', 30000000) == 6895259
assert solve('3,2,1', 30000000) == 18
assert solve('3,1,2', 30000000) == 362

part_1_response = solve('8,13,1,0,18,9', 2020)
print(f'Part 1: {part_1_response}')

part_2_response = solve('8,13,1,0,18,9', 30000000)
print(f'Part 2: {part_2_response}')

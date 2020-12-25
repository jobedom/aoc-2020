from misc import init_day

init_day(__file__, 25)


def transform_subject_number(subject_number, loop_size):
    value = 1
    for _ in range(loop_size):
        value *= subject_number
        value = value % 20201227
    return value


def find_loop_size(public_key, subject_number):
    loop_size = 1
    calculated_publick_key = 1
    while True:
        calculated_publick_key *= subject_number
        calculated_publick_key = calculated_publick_key % 20201227
        if calculated_publick_key == public_key:
            return loop_size
        loop_size += 1


def solve_part_1(card_public_key, door_public_key, check_key_match):
    card_loop_size = find_loop_size(card_public_key, 7)
    door_loop_size = find_loop_size(door_public_key, 7)
    encryption_key = transform_subject_number(card_public_key, door_loop_size)
    if check_key_match:
        encryption_key_2 = transform_subject_number(door_public_key, card_loop_size)
        assert encryption_key == encryption_key_2
    return encryption_key


assert solve_part_1(5764801, 17807724, True) == 14897079
part_1_response = solve_part_1(2084668, 3704642, False)
print(f'Part 1: {part_1_response}')

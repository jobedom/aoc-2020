import re
from math import prod

from misc import init_day
from input import get_file_lines_with_no_blanks

init_day(__file__, 16)


def parse_input(problem_input):
    def parse_int_list(number_list):
        return [int(number) for number in number_list.split(',')]

    tickets = []
    fields = []
    for line in problem_input:
        if re.match(r'^[\d,]+$', line):
            tickets.append(line)
        else:
            field_matches = re.match(r'^(.+)\s*:', line)
            if field_matches:
                field = field_matches.group(1)
                ranges = [(int(range_min), int(range_max))
                          for range_min, range_max in re.findall(r'(\d+)\-(\d+)', line)]
                fields.append((field, ranges))
    my_ticket = parse_int_list(tickets[0])
    nearby_tickets = [parse_int_list(ticket) for ticket in tickets[1:]]
    return my_ticket, nearby_tickets, fields


def is_value_in_any_range(value, ranges):
    return any(range_min <= value <= range_max for range_min, range_max in ranges)


def is_value_invalid_for_all_fields(value, fields):
    return not any(is_value_in_any_range(value, field_ranges) for field, field_ranges in fields)


def is_ticket_invalid(ticket, fields):
    return any(is_value_invalid_for_all_fields(value, fields) for value in ticket)


def valid_tickets(tickets, fields):
    return [ticket for ticket in tickets if not is_ticket_invalid(ticket, fields)]


def filtered_dict_by_key_prefix(dictionary, prefix):
    return {key: value for key, value in dictionary.items() if key.startswith(prefix)}


def first_unique_field(candidates):
    def get_item_set_length(item):
        return len(item[1])

    position, fields_set = sorted(candidates.items(), key=get_item_set_length)[0]
    return position, fields_set.pop()


def solve_part_1(problem_input):
    my_ticket, nearby_tickets, fields = parse_input(problem_input)
    return sum(value for ticket in nearby_tickets for value in ticket if is_value_invalid_for_all_fields(value, fields))


def solve_part_2(problem_input):
    my_ticket, nearby_tickets, fields = parse_input(problem_input)
    candidates = {
        position: set(name for name, ranges in fields if all(is_value_in_any_range(value, ranges) for value in values))
        for position, values in enumerate(zip(*valid_tickets(nearby_tickets, fields)))
    }
    fields_position = {}
    while candidates:
        position, name = first_unique_field(candidates)
        fields_position[name] = position
        candidates.pop(position)
        for names in candidates.values():
            names -= {name}
    departure_fields_position = filtered_dict_by_key_prefix(fields_position, 'departure')
    return prod(my_ticket[position] for position in departure_fields_position.values())


test_input = get_file_lines_with_no_blanks('test.txt')

assert solve_part_1(test_input) == 71

problem_input = get_file_lines_with_no_blanks('input.txt')
part_1_response = solve_part_1(problem_input)
print(f'Part 1: {part_1_response}')
part_2_response = solve_part_2(problem_input)
print(f'Part 2: {part_2_response}')

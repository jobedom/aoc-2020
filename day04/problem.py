import re

from misc import init_day
from input import get_file_lines
from lists import list_intersection

init_day(__file__, 4)

passport_parts = re.compile(r'(\w{3}):(\S+)')


def no_validation(value, regexp_matches):
    return True


PASSPORT_VALIDATIONS = {
    'byr': (r'\d{4}', lambda v, m: 1920 <= int(v) <= 2002),
    'iyr': (r'\d{4}', lambda v, m: 2010 <= int(v) <= 2020),
    'eyr': (r'\d{4}', lambda v, m: 2020 <= int(v) <= 2030),
    'hgt': (r'(\d+)(cm|in)', lambda v, m: (150 <= int(m[0]) <= 193) if m[1] == 'cm' else (59 <= int(m[0]) <= 76)),
    'hcl': (r'#[a-f0-9]{6}', no_validation),
    'ecl': (r'(amb|blu|brn|gry|grn|hzl|oth)', no_validation),
    'pid': (r'\d{9}', no_validation),
}
REQUIRED_PASSPORT_KEYS = PASSPORT_VALIDATIONS.keys()
REQUIRED_PASSPORT_KEY_COUNT = len(REQUIRED_PASSPORT_KEYS)


def parse_passports(passport_input_lines):
    passport_input_lines.append('')
    passports_list = []
    passport = {}
    for line in passport_input_lines:
        line = line.strip()
        if line == '':
            passports_list.append(passport)
            passport = {}
        else:
            passport = passport | dict(passport_parts.findall(line))
    return passports_list


def solve_part_1(passport_list):
    valid_count = 0
    for passport in passport_list:
        passport_keys = passport.keys()
        passport_required_keys = list_intersection(passport_keys, REQUIRED_PASSPORT_KEYS)
        if len(passport_required_keys) == REQUIRED_PASSPORT_KEY_COUNT:
            valid_count += 1
    return valid_count


def solve_part_2(passport_list):
    def part2_passport_is_valid(passport):
        for key in REQUIRED_PASSPORT_KEYS:
            passport_value = passport.get(key)
            if passport_value is None:
                return False
            (regexp, validator) = PASSPORT_VALIDATIONS[key]
            matches = re.match(f'^{regexp}$', passport_value)
            if not matches or not validator(passport_value, matches.groups()):
                return False
        return True

    return sum(int(part2_passport_is_valid(passport)) for passport in passport_list)


test_passports_1 = parse_passports(get_file_lines('test1.txt'))
result_test_part_1 = solve_part_1(test_passports_1)
assert result_test_part_1 == 2

test_passports_2 = parse_passports(get_file_lines('test2.txt'))
result_test_part_2 = solve_part_2(test_passports_2)
assert result_test_part_2 == 4

passports = parse_passports(get_file_lines('./input.txt'))

result_part_1 = solve_part_1(passports)
print(f'Part 1: {result_part_1}')

result_part_2 = solve_part_2(passports)
print(f'Part 2: {result_part_2}')

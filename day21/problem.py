import re

from misc import init_day
from input import get_file_lines_with_no_blanks

init_day(__file__, 21)


def parse_input(input):
    all_ingredients = []
    allergen_reference = dict()
    index = 0
    for line in input:
        matches = re.match(r'^([a-z\s]+) \(contains ([a-z,\s]+)\)$', line)
        ingredients_list = matches.group(1).split()
        allergens = matches.group(2).split(', ')
        all_ingredients.append(ingredients_list)
        for allergen in allergens:
            allergen_reference[allergen] = allergen_reference.get(allergen, [])
            allergen_reference[allergen].append(index)
        index += 1
    allergen_candidates = {
        key: set.intersection(*[set(all_ingredients[k]) for k in allergen_reference[key]])
        for key, value in allergen_reference.items()
    }
    no_ingredient = set(ingredient for ingredients_list in all_ingredients for ingredient in ingredients_list)
    no_ingredient = no_ingredient.difference(set.union(*(allergen_candidates.values())))
    return all_ingredients, no_ingredient, allergen_candidates


def solve_part_1(input):
    ingredients, no_ingredient, allergen_candidates = parse_input(input)
    return len(
        [
            ingredient for ingredients_list in ingredients for ingredient in ingredients_list
            if ingredient in no_ingredient
        ]
    )


def solve_part_2(input):
    ingredients, no_ingredient, allergen_candidates = parse_input(input)
    already_visited = set()
    while any(len(candidates) > 1 for candidates in allergen_candidates.values()):
        for key_1, value_1 in allergen_candidates.items():
            if len(value_1) == 1 and key_1 not in already_visited:
                already_visited.add(key_1)
                break
        for key_2, value_2 in allergen_candidates.items():
            if key_2 != key_1:
                value_2.difference_update(value_1)
    result_ingredients = [list(value)[0] for _, value in sorted(allergen_candidates.items())]
    return ','.join(result_ingredients)


test_input = get_file_lines_with_no_blanks('test.txt')
assert solve_part_1(test_input) == 5
assert solve_part_2(test_input) == 'mxmxvkd,sqjhc,fvjkl'

problem_input = get_file_lines_with_no_blanks('input.txt')
part_1_response = solve_part_1(problem_input)
part_2_response = solve_part_2(problem_input)
print(f'Part 1: {part_1_response}')
print(f'Part 2: {part_2_response}')

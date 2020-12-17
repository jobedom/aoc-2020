from collections import defaultdict

from misc import init_day
from input import get_file_lines_with_no_blanks

init_day(__file__, 17)


def parse_input(problem_input, dimensions):
    def complete_coords(coords):
        return coords + [0] * abs((len(coords) - dimensions))

    world = defaultdict(bool)
    for y, line in enumerate(problem_input):
        for x, char in enumerate(line):
            coords_list = complete_coords([x, y, 0])
            coord = tuple(coords_list)
            world[coord] = char == '#'
    return world


def get_world_limits_1(world):
    coords = world.keys()
    xs = [x for x, _, _ in coords]
    ys = [y for _, y, _ in coords]
    zs = [z for _, _, z in coords]
    min_x = min(xs)
    max_x = max(xs)
    min_y = min(ys)
    max_y = max(ys)
    min_z = min(zs)
    max_z = max(zs)
    return min_x, max_x, min_y, max_y, min_z, max_z


def get_active_neighbours_count_1(x, y, z, world):
    count = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            for dz in range(-1, 2):
                if dx == 0 and dy == 0 and dz == 0:
                    continue
                if world.get((x + dx, y + dy, z + dz), False):
                    count += 1
    return count


def evolve_1(world):
    min_x, max_x, min_y, max_y, min_z, max_z = get_world_limits_1(world)
    new_world = defaultdict(bool)
    for x in range(min_x - 3, max_x + 2):
        for y in range(min_y - 3, max_y + 2):
            for z in range(min_z - 3, max_z + 2):
                cube_active = world.get((x, y, z), False)
                active_neighbours_count = get_active_neighbours_count_1(x, y, z, world)
                if cube_active:
                    if 2 <= active_neighbours_count <= 3:
                        new_world[(x, y, z)] = True
                else:
                    if active_neighbours_count == 3:
                        new_world[(x, y, z)] = True
    return new_world


def get_world_limits_2(world):
    coords = world.keys()
    xs = [x for x, _, _, _ in coords]
    ys = [y for _, y, _, _ in coords]
    zs = [z for _, _, z, _ in coords]
    ks = [k for _, _, _, k in coords]
    min_x = min(xs)
    max_x = max(xs)
    min_y = min(ys)
    max_y = max(ys)
    min_z = min(zs)
    max_z = max(zs)
    min_k = min(ks)
    max_k = max(ks)
    return min_x, max_x, min_y, max_y, min_z, max_z, min_k, max_k


def get_active_neighbours_count_2(x, y, z, k, world):
    count = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            for dz in range(-1, 2):
                for dk in range(-1, 2):
                    if dx == 0 and dy == 0 and dz == 0 and dk == 0:
                        continue
                    if world.get((x + dx, y + dy, z + dz, k + dk), False):
                        count += 1
    return count


def evolve_2(world):
    min_x, max_x, min_y, max_y, min_z, max_z, min_k, max_k = get_world_limits_2(world)
    new_world = defaultdict(bool)
    for x in range(min_x - 3, max_x + 2):
        for y in range(min_y - 3, max_y + 2):
            for z in range(min_z - 3, max_z + 2):
                for k in range(min_k - 3, max_k + 2):
                    cube_active = world.get((x, y, z, k), False)
                    active_neighbours_count = get_active_neighbours_count_2(x, y, z, k, world)
                    if cube_active:
                        if 2 <= active_neighbours_count <= 3:
                            new_world[(x, y, z, k)] = True
                    else:
                        if active_neighbours_count == 3:
                            new_world[(x, y, z, k)] = True
    return new_world


def solve_part_1(problem_input):
    world = parse_input(problem_input, 3)
    for i in range(0, 6):
        world = evolve_1(world)
    return len(world)


def solve_part_2(problem_input):
    world = parse_input(problem_input, 4)
    for i in range(0, 6):
        world = evolve_2(world)
    return len(world)


test_input = get_file_lines_with_no_blanks('test.txt')

assert solve_part_1(test_input) == 112
assert solve_part_2(test_input) == 848

problem_input = get_file_lines_with_no_blanks('input.txt')
part_1_response = solve_part_1(problem_input)
part_2_response = solve_part_2(problem_input)
print(f'Part 1: {part_1_response}')
print(f'Part 2: {part_2_response}')

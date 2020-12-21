import math
import re
from collections import defaultdict

from misc import init_day
from input import get_file_contents

init_day(__file__, 20)


def parse_input(s):
    tiles = {}
    for block in s.split('\n\n'):
        lines = block.splitlines()
        matches = re.fullmatch(r'Tile (\d+):', lines[0])
        tile_id = int(matches.group(1))
        tiles[tile_id] = [list(line) for line in lines[1:]]
    return tiles


def tile_edges(tile):
    top_edge = tile[0]
    right_edge = ''.join(row[-1] for row in tile)
    bottom_edge = tile[-1]
    left_edge = ''.join(row[0] for row in tile)
    return (top_edge, right_edge, bottom_edge, left_edge)


def tile_variants(tile):
    result = []
    for item in sum([tile_rotations(flipped_tile) for flipped_tile in tile_flips(tile)], []):
        if item not in result:
            result.append(item)
    return result


def tile_flips(tile):
    tile_rows_reversed = [row[::-1] for row in tile]
    return [
        tile,
        tile[::-1],
        tile_rows_reversed,
        tile_rows_reversed[::-1],
    ]


def tile_rotations(tile):
    size = len(tile)
    result = [tile]
    for count in range(0, 3):
        previous = tile
        tile = [row[:] for row in tile]
        for row in range(0, size):
            for column in range(0, size):
                tile[row][column] = previous[size - column - 1][row]
        result.append(tile)
    return result


def get_tiles_variants(tiles):
    return {tile_id: tile_variants(tile) for tile_id, tile in tiles.items()}


def generate_tiling(tile_variants_edges):
    side = int(math.sqrt(len(tile_variants_edges)))

    def generate_tiling_rec(tiling, row, column, seen):
        if row == side:
            return tiling
        next_column = column + 1
        next_row = row
        if next_column == side:
            next_column = 0
            next_row += 1
        for tile_id, options in tile_variants_edges.items():
            if tile_id in seen:
                continue
            seen.add(tile_id)
            for index, edges in options.items():
                top_edge, right_edge, bottom_edge, left_edge = edges
                if column > 0:
                    neighbor_tile_id, neighbor_variant = tiling[column - 1][row]
                    neighbor_top_edge, neighbor_right_edge, neighbor_bottom_edge, neighbor_left_edge = \
                        tile_variants_edges[neighbor_tile_id][neighbor_variant]
                    if neighbor_right_edge != left_edge:
                        continue
                if row > 0:
                    neighbor_tile_id, neighbor_variant = tiling[column][row - 1]
                    neighbor_top_edge, neighbor_right_edge, neighbor_bottom_edge, neighbor_left_edge = \
                        tile_variants_edges[neighbor_tile_id][neighbor_variant]
                    if neighbor_bottom_edge != top_edge:
                        continue
                tiling[column][row] = (tile_id, index)
                response = generate_tiling_rec(tiling, next_row, next_column, seen)
                if response is not None:
                    return response
            seen.remove(tile_id)
        tiling[column][row] = None
        return None

    tiling = []
    for counter in range(0, side):
        tiling.append([None] * side)
    seen = set()
    return generate_tiling_rec(tiling, 0, 0, seen)


def get_tiling(tiles):
    tiles_variants = get_tiles_variants(tiles)
    tile_variants_edges = defaultdict(dict)
    for tile_id, variants in tiles_variants.items():
        for index, variant in enumerate(variants):
            tile_variants_edges[tile_id][index] = tile_edges(variant)
    return generate_tiling(tile_variants_edges)


def solve_part_1(input):
    tiles = parse_input(input)
    tiling = get_tiling(tiles)
    corners = [tiling[0][0], tiling[0][-1], tiling[-1][0], tiling[-1][-1]]
    return math.prod([tile_id for tile_id, tile in corners])


def build_complete_image(tile_variants, tiling):
    result = []
    for row in tiling:
        tiles = []
        for tile_id, variant in row:
            tile = [line[1:-1] for line in tile_variants[tile_id][variant][1:-1]]
            tiles.append(tile)
        tile_row_count = len(tiles[0])
        tile_column_count = len(tiles[0][0])
        for column in range(tile_column_count):
            new_row = []
            for index in range(len(tiles)):
                new_row.extend(tiles[index][tile_row][column] for tile_row in range(0, tile_row_count))
            result.append(''.join(new_row))
    return result


def not_monsters_rough_cells_count(monster_pattern, image):
    monster_cells = []
    max_column = 0
    max_row = 0
    for row, line in enumerate(monster_pattern.splitlines()):
        for column, character in enumerate(line):
            if character == '#':
                monster_cells.append((row, column))
                if column > max_column:
                    max_column = column
                if row > max_row:
                    max_row = row
    monster_image_cells = set()
    rows_size = len(image)
    column_size = len(image[0])
    for row in range(0, rows_size):
        if row + max_row >= rows_size:
            break
        for column in range(0, column_size):
            if column + max_column >= column_size:
                break
            if all(image[row + cell_row][column + cell_column] == '#' for cell_row, cell_column in monster_cells):
                for cell_row, cell_column in monster_cells:
                    monster_image_cells.add((column + cell_column, row + cell_row))
    if len(monster_image_cells) == 0:
        return None
    return ''.join(sum(image, [])).count('#') - len(monster_image_cells)


def solve_part_2(input):
    tiles = parse_input(input)
    tiles_variants = get_tiles_variants(tiles)
    tiling = get_tiling(tiles)
    monster_pattern = get_file_contents('monster.txt')
    image = build_complete_image(tiles_variants, tiling)
    image_candidates = tile_variants([list(item) for item in image])
    for candidate in image_candidates:
        result = not_monsters_rough_cells_count(monster_pattern, candidate)
        if result is not None:
            return result


test_input = get_file_contents('test.txt')
problem_input = get_file_contents('input.txt')

assert solve_part_1(test_input) == 20899048083289
part_1_response = solve_part_1(problem_input)
print(f'Part 1: {part_1_response}')

assert solve_part_2(test_input) == 273
part_2_response = solve_part_2(problem_input)
print(f'Part 2: {part_2_response}')

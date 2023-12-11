from copy import deepcopy
from itertools import combinations

from pathlib import Path

PATH = Path(__file__).parent
INPUT_PATH = PATH / "input.txt"
SAMPLE_PATH = PATH / "sample.txt"


def parse_input(path: Path) -> list:
    with open(path, "r") as f:
        lines = [l.strip() for l in f.read().split("\n")]
        return lines


def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def enhanced_manhattan(p1, p2, row_idxs, col_idxs, x):
    min_r, max_r = min(p1[0], p2[0]), max(p1[0], p2[0])
    min_c, max_c = min(p1[1], p2[1]), max(p1[1], p2[1])
    return manhattan(p1, p2) + (x - 1) * (
        sum(min_r < row < max_r for row in row_idxs)
        + sum(min_c < col < max_c for col in col_idxs)
    )


def get_blanks(grid):
    row_idxs = []
    for r in range(len(grid)):
        if all(v == "." for v in grid[r]):
            row_idxs.append(r)

    col_idxs = []
    g2 = list(zip(*grid))
    for r in range(len(g2)):
        if all(v == "." for v in g2[r]):
            col_idxs.append(r)
    return row_idxs, col_idxs


def get_galaxies(grid):
    galaxies = []
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "#":
                galaxies.append((r, c))
    return galaxies


def part_1(data: list):
    grid = []
    for line in data:
        grid.append([x for x in line])

    row_idxs, col_idxs = get_blanks(grid)
    galaxies = get_galaxies(grid)

    return sum(
        [
            enhanced_manhattan(*c, row_idxs, col_idxs, 2)
            for c in combinations(galaxies, 2)
        ]
    )


def part_2(data: list):
    grid = []
    for line in data:
        grid.append([x for x in line])

    row_idxs, col_idxs = get_blanks(grid)
    galaxies = get_galaxies(grid)

    return sum(
        [
            enhanced_manhattan(*c, row_idxs, col_idxs, 1_000_000)
            for c in combinations(galaxies, 2)
        ]
    )


def run():
    sample = parse_input(SAMPLE_PATH)
    data = parse_input(INPUT_PATH)

    print("\n** Part 1 **")
    print(f"sample: {part_1(deepcopy(sample))}")
    print(f"data: {part_1(deepcopy(data))}")

    print("\n** Part 2 **")
    print(f"sample: {part_2(sample)}")
    print(f"data: {part_2(data)}")


# 834911817 too low
if __name__ == "__main__":
    run()

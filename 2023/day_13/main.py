from collections import defaultdict
from copy import deepcopy
from pathlib import Path

PATH = Path(__file__).parent
INPUT_PATH = PATH / "input.txt"
SAMPLE_PATH = PATH / "sample.txt"


def parse_input(path: Path) -> list:
    with open(path, "r") as f:
        lines = [l.strip() for l in f.read().split("\n\n")]
        return lines


def get_mirror(grid):
    R = len(grid)
    for r in range(1, R):
        size = min(r, R - r)
        if grid[r - size : r] == grid[r : r + size][::-1]:
            return r
    return None


def compare(grid, other):
    R = len(grid)
    C = len(grid[0])
    diffs = defaultdict(int)
    for r in range(R):
        for c in range(C):
            if grid[r][c] != other[r][c]:
                diffs[r + 1] += 1
    return sum(diffs.values()) == 1


def get_mirror_smudged(grid):
    R = len(grid)
    for r in range(1, R):
        size = min(r, R - r)
        if compare(grid[r - size : r], grid[r : r + size][::-1]):
            return r
    return None


def part_1(data: list):
    total = 0
    for line in data:
        grid = [list(l) for l in line.split()]
        horizontal = get_mirror(grid)
        if horizontal:
            total += 100 * horizontal
        else:
            vertical = get_mirror(list(zip(*grid)))
            if vertical:
                total += vertical
    return total


def part_2(data: list):
    total = 0
    for line in data:
        grid = [list(l) for l in line.split()]
        horizontal = get_mirror_smudged(grid)
        if horizontal:
            total += 100 * horizontal
        else:
            vertical = get_mirror_smudged(list(zip(*grid)))
            if vertical:
                total += vertical
    return total


def run():
    sample = parse_input(SAMPLE_PATH)
    data = parse_input(INPUT_PATH)

    print("\n** Part 1 **")
    print(f"sample: {part_1(deepcopy(sample))}")
    print(f"data: {part_1(deepcopy(data))}")

    print("\n** Part 2 **")
    print(f"sample: {part_2(sample)}")
    print(f"data: {part_2(data)}")


if __name__ == "__main__":
    run()

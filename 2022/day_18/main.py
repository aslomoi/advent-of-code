from collections import deque
from copy import deepcopy
import numpy as np
from pathlib import Path

PATH = Path(__file__).parent
INPUT_PATH = PATH / "input.txt"
SAMPLE_PATH = PATH / "sample.txt"


def parse_input(path: Path) -> set:
    with open(path, "r") as f:
        lines = set(
            tuple(int(x) for x in l.strip().split(",")) for l in f.read().split("\n")
        )
        return lines


directions = [
    np.array([1, 0, 0]),
    np.array([-1, 0, 0]),
    np.array([0, 1, 0]),
    np.array([0, -1, 0]),
    np.array([0, 0, 1]),
    np.array([0, 0, -1]),
]


def part_1(data: set):

    area = 0
    for (x, y, z) in data:
        cube = np.array([x, y, z])
        for d in directions:
            if tuple(cube + d) not in data:
                area += 1
    return area


def part_2(data: set):
    xmin, xmax = min(x for x, _, _ in data), max(x for x, _, _ in data)
    ymin, ymax = min(y for _, y, _ in data), max(y for _, y, _ in data)
    zmin, zmax = min(z for _, _, z in data), max(z for _, _, z in data)

    space = set()
    for x in range(xmin, xmax + 1):
        for y in range(ymin, ymax + 1):
            for z in range(zmin, zmax + 1):
                if (x, y, z) not in data:
                    space.add((x, y, z))

    start = (xmin, ymin, zmin)
    assert start not in data
    Q = deque([start])

    seen = set()
    while Q:
        (x, y, z) = cube = Q.popleft()

        if (
            cube in seen
            or x < xmin - 1
            or x > xmax + 1
            or y < ymin - 1
            or y > ymax + 1
            or z < zmin - 1
            or z > zmax + 1
        ):
            continue

        seen.add(cube)
        if cube in data:
            continue

        for d in directions:
            Q.append(tuple(cube + d))

    air = space - seen
    sphere = data | air
    area = 0
    for cube in sphere:
        for d in directions:
            if tuple(cube + d) not in sphere:
                area += 1

    return area


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

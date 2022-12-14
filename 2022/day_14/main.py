from collections import defaultdict, Counter, deque
from copy import deepcopy
import numpy as np
import re
from pathlib import Path

PATH = Path(__file__).parent
INPUT_PATH = PATH / "input.txt"
SAMPLE_PATH = PATH / "sample.txt"


def parse_input(path: Path):
    with open(path, "r") as f:
        lines = [l.strip() for l in f.read().split("\n")]
        grid = {}
        for line in lines:
            coords = [
                (int(pts.split(",")[0]), int(pts.split(",")[1]))
                for pts in line.split(" -> ")
            ]
            for (x1, y1), (x2, y2) in zip(coords, coords[1:]):
                x, y = x1, y1
                dx, dy = np.sign(x2 - x1), np.sign(y2 - y1)
                while True:
                    grid[(x, y)] = "#"
                    if x == x2 and y == y2:
                        break
                    x += dx
                    y += dy
        return grid


def show(grid):
    Xmin, Xmax = min(x for x, _ in grid.keys()), max(x for x, _ in grid.keys())
    Ymin, Ymax = min(y for _, y in grid.keys()), max(y for _, y in grid.keys())

    for y in range(Ymin, Ymax + 1):
        ln = ""
        for x in range(Xmin, Xmax + 1):
            if (x, y) in grid:
                ln += grid[(x, y)]
            else:
                ln += "."
        print(ln)


def part_1(grid):
    floor = max(y for _, y in grid.keys())
    falling = deque([(500, 0)])
    grid[(500, 0)] = "+"
    count = 0
    while True:
        x, y = falling[-1]

        if y == floor + 1:
            return count

        if (new := (x, y + 1)) not in grid:
            grid[new] = "+"
            falling.append(new)
        elif (new := (x - 1, y + 1)) not in grid:
            grid[new] = "+"
            falling.append(new)
        elif (new := (x + 1, y + 1)) not in grid:
            grid[new] = "+"
            falling.append(new)
        else:
            grid[(x, y)] = "o"
            falling.pop()
            count +=1


def part_2(grid):
    floor = max(y for _, y in grid.keys()) + 2
    falling = deque([(500, 0)])
    grid[(500, 0)] = "+"
    count = 0
    while True:
        x, y = falling[-1]

        if (new := (x, y + 1)) not in grid and y + 1 < floor:
            grid[new] = "+"
            falling.append(new)
        elif (new := (x - 1, y + 1)) not in grid and y + 1 < floor:
            grid[new] = "+"
            falling.append(new)
        elif (new := (x + 1, y + 1)) not in grid and y + 1 < floor:
            grid[new] = "+"
            falling.append(new)
        else:
            grid[(x, y)] = "o"
            falling.pop()
            count += 1

        if not falling:
            return count


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

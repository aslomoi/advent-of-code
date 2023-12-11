from collections import defaultdict, Counter, deque
from copy import deepcopy
import numpy as np
import re
from pathlib import Path

PATH = Path(__file__).parent
INPUT_PATH = PATH / "input.txt"
SAMPLE_PATH = PATH / "sample.txt"


def parse_input(path: Path) -> list:
    with open(path, "r") as f:
        lines = [l.strip() for l in f.read().split("\n")]
        return lines


def make_loop(grid: list[list[int]]) -> deque[tuple[int, int]]:
    loop: deque[tuple[int, int]] = deque()
    R = len(grid)
    C = len(grid[0])
    start = None
    for r in range(R):
        for c in range(C):
            if grid[r][c] == "S":
                start = (r, c)
                loop.append(start)
                new = []
                for rr, cc in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                    if r + rr < 0 or r + rr >= len(grid):
                        continue
                    if c + cc < 0 or c + cc >= len(grid[0]):
                        continue
                    if cc == 1 and grid[r + rr][c + cc] in ["-", "7", "J"]:
                        new.append((r + rr, c + cc))
                    elif cc == -1 and grid[r + rr][c + cc] in ["-", "F", "L"]:
                        new.append((r + rr, c + cc))
                    elif rr == 1 and grid[r + rr][c + cc] in ["|", "J", "L"]:
                        new.append((r + rr, c + cc))
                    elif rr == -1 and grid[r + rr][c + cc] in ["|", "F", "7"]:
                        new.append((r + rr, c + cc))
                    else:
                        continue
                break
        if start is not None:
            break
    last = new[0]
    loop.append(new[1])

    while loop[-1] != last:
        r, c = loop[-1]
        val = grid[r][c]
        for rr, cc in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            if r + rr == loop[-2][0] and c + cc == loop[-2][1]:
                continue
            if r + rr < 0 or r + rr >= len(grid):
                continue
            if c + cc < 0 or c + cc >= len(grid[0]):
                continue

            if (
                cc == 1
                and val in ["-", "F", "L"]
                and grid[r + rr][c + cc] in ["-", "7", "J"]
            ):
                loop.append((r + rr, c + cc))
                break
            elif (
                cc == -1
                and val in ["-", "7", "J"]
                and grid[r + rr][c + cc] in ["-", "F", "L"]
            ):
                loop.append((r + rr, c + cc))
                break
            elif (
                rr == 1
                and val in ["|", "F", "7"]
                and grid[r + rr][c + cc] in ["|", "J", "L"]
            ):
                loop.append((r + rr, c + cc))
                break
            elif (
                rr == -1
                and val in ["|", "J", "L"]
                and grid[r + rr][c + cc] in ["|", "F", "7"]
            ):
                loop.append((r + rr, c + cc))
                break
    return loop


def part_1(data: list):
    grid = [[c for c in line] for line in data]
    loop = make_loop(grid)
    return len(loop) // 2


def part_2(data: list):
    grid = [[c for c in line] for line in data]
    R = len(grid)
    C = len(grid[0])

    loop = set(make_loop(grid))

    total = 0
    for r in range(R):
        ln = []
        for c in range(C):
            if (r, c) in loop:
                ln.append(grid[r][c])
            else:
                counts = Counter(ln)
                if (
                    counts.get("F", 0) + counts.get("7", 0) + counts.get("|", 0)
                ) % 2 == 1:
                    total += 1
                ln.append(".")
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

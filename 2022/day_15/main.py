from collections import defaultdict, Counter, deque
from copy import deepcopy
import numpy as np
import re
from pathlib import Path
from operator import itemgetter

PATH = Path(__file__).parent
INPUT_PATH = PATH / "input.txt"
SAMPLE_PATH = PATH / "sample.txt"


def parse_input(path: Path) -> list:
    with open(path, "r") as f:
        lines = [list(map(int, re.findall(r"-?\d+", l))) for l in f.read().split("\n")]
        return lines


def manhattan(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)


def part_1(data: list, sample=False):
    pos = {}
    dists = {}
    bad = set()

    if sample:
        row = 10
    else:
        row = 2000000

    for sx, sy, bx, by in data:
        pos[(sx, sy)] = "S"
        pos[(bx, by)] = "B"
        man = manhattan(sx, sy, bx, by)
        dists[(sx, sy)] = man

        num = manhattan(sx, sy, sx, row)
        if num < man:
            diff = abs(num - man)
            bad.update(list(range(sx - diff, sx + diff + 1)))

    for (sx, sy), v in pos.items():
        if sy == row and v == "B" and sx in bad:
            bad.remove(sx)

    return len(bad)


def part_2(data: list, sample=False):
    pos = {}
    dists = {}
    first = itemgetter(0)

    if sample:
        N = 20
    else:
        N = 4_000_000

    for sx, sy, bx, by in data:
        pos[(sx, sy)] = "S"
        pos[(bx, by)] = "B"
        man = manhattan(sx, sy, bx, by)
        dists[(sx, sy)] = man

    for row in range(N):
        ranges = []
        for (sx, sy), d in dists.items():
            num = manhattan(sx, sy, sx, row)
            man = dists[(sx, sy)]
            if num < man:
                diff = abs(num - man)
                ranges.append((max(0, sx - diff), min(N, sx + diff)))

        ranges = sorted(ranges, key=first)

        last = None
        for x1, x2 in ranges:
            if not last:
                if x1 == 1:
                    return (x1 - 1) * 4000000 + row
                else:
                    last = x2
            elif x1 <= last:
                if x2 >= last:
                    last = x2
                    if last == N:
                        break
            else:
                return (x1 - 1) * 4000000 + row


def run():
    sample = parse_input(SAMPLE_PATH)
    data = parse_input(INPUT_PATH)

    print("\n** Part 1 **")
    print(f"sample: {part_1(deepcopy(sample), sample=True)}")
    print(f"data: {part_1(deepcopy(data))}")
    print("\n** Part 2 **")
    print(f"sample: {part_2(sample, sample=True)}")
    print(f"data: {part_2(data)}")


if __name__ == "__main__":
    run()

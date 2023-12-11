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


def part_1(data: list):
    history = [[int(i) for i in line.split()] for line in data]
    result = 0
    for line in history:
        all_diffs = []
        while any(i != 0 for i in line):
            all_diffs.append(line)
            line = [b - a for a, b in zip(line, line[1:])]
        result += sum(l[-1] for l in all_diffs)
    return result


def part_2(data: list):
    history = [[int(i) for i in line.split()] for line in data]
    result = 0
    for line in history:
        all_diffs = []
        while any(i != 0 for i in line):
            all_diffs.append(line)
            line = [b - a for a, b in zip(line, line[1:])]
        result += sum(d[0] for d in all_diffs[::2]) - sum(d[0] for d in all_diffs[1::2])
    return result


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

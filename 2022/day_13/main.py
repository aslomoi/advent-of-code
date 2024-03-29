from copy import deepcopy
import json
import numpy as np
from functools import cmp_to_key
from pathlib import Path

PATH = Path(__file__).parent
INPUT_PATH = PATH / "input.txt"
SAMPLE_PATH = PATH / "sample.txt"


def parse_input(path: Path) -> list:
    with open(path, "r") as f:
        lines = [l.strip() for l in f.read().split("\n\n")]
        return lines


def compare(l1, l2):
    for l, r in zip(l1, l2):
        match (l, r):
            case (int(), int()) if l == r:
                continue
            case (int(), int()):
                return l < r
            case (list(), list()):
                out = compare(l, r)
            case (list(), int()):
                out = compare(l, [r])
            case (int(), list()):
                out = compare([l], r)
            case _:
                assert False

        if out is not None:
            return out

    return None if len(l1) == len(l2) else len(l1) < len(l2)


def part_1(data: list):

    correct = []
    for idx, pair in enumerate(data, 1):
        l1, l2 = [json.loads(x) for x in pair.splitlines()]
        if compare(l1, l2) is True:
            correct.append(idx)
    return sum(correct)


def part_2(data: list):
    dividers = [[[2]], [[6]]]
    packets = [*dividers]
    for idx, pair in enumerate(data, 1):
        packets.extend([json.loads(x) for x in pair.splitlines()])

    ordered = sorted(packets, key=cmp_to_key(lambda x, y: -1 if compare(x, y) else 1))
    return np.prod([ordered.index(x) + 1 for x in dividers])


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

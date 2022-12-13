from copy import deepcopy
import numpy as np
import functools
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
        if type(l) == type(r) == int:
            if l == r:
                continue
            elif l < r:
                return True
            else:
                return False
        elif type(l) == type(r) == list:
            out = compare(l, r)
        elif type(l) == list:
            out = compare(l, [r])
        elif type(r) == list:
            out = compare([l], r)
        else:
            assert False

        if out is True:
            return True
        elif out is False:
            return False
    return None if len(l1) == len(l2) else len(l1) < len(l2)


def part_1(data: list):

    correct = []
    for idx, pair in enumerate(data, 1):
        l1, l2 = [eval(x) for x in pair.splitlines()]
        out = compare(l1, l2)
        if out is True:
            correct.append(idx)
    return sum(correct)


def part_2(data: list):
    dividers = [[[2]], [[6]]]
    packets = [*dividers]
    for idx, pair in enumerate(data, 1):
        packets.extend([eval(x) for x in pair.splitlines()])

    ordered = sorted(
        packets, key=functools.cmp_to_key(lambda x, y: -1 if compare(x, y) else 1)
    )
    return np.prod([ordered.index(x) + 1 for x in dividers])


def run():
    sample = parse_input(SAMPLE_PATH)
    data = parse_input(INPUT_PATH)

    print("\n** Part 1 **")
    print(f"sample: {part_1(deepcopy(sample))}")
    print(f"data: {part_1(deepcopy(data))}")

    # print("\n** Part 2 **")
    print(f"sample: {part_2(sample)}")
    print(f"data: {part_2(data)}")
    # not 6402373705728000


if __name__ == "__main__":
    run()

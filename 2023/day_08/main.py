from copy import deepcopy
from math import lcm
from pathlib import Path
from itertools import cycle

PATH = Path(__file__).parent
INPUT_PATH = PATH / "input.txt"
SAMPLE_PATH = PATH / "sample.txt"


def parse_input(path: Path) -> list:
    with open(path, "r") as f:
        lines = [l.strip() for l in f.read().split("\n")]
        return lines


def part_1(data: list):
    instructions = [i for i in data.pop(0)]
    data.pop(0)
    mapping = {}
    for line in data:
        src, part = line.split(" = ")
        mapping[src] = part[1:-1].split(", ")

    position = "AAA"
    end = "ZZZ"
    moves = cycle(instructions)
    steps = 0
    while position != end:
        position = mapping[position][1 if next(moves) == "R" else 0]
        steps += 1
    return steps


def part_2(data: list):
    instructions = [i for i in data.pop(0)]
    data.pop(0)
    mapping = {}
    for line in data:
        src, part = line.split(" = ")
        mapping[src] = part[1:-1].split(", ")
    positions = [node for node in mapping.keys() if node[-1] == "A"]
    ends = set(node for node in mapping.keys() if node[-1] == "Z")

    distances = []
    for pos in positions:
        jumps = [pos]
        moves = cycle(instructions)
        while jumps and jumps[-1] not in ends:
            jumps.append(mapping[jumps[-1]][1 if next(moves) == "R" else 0])
        distances.append(len(jumps) - 1)
    return lcm(*distances)


def run():
    sample = parse_input(SAMPLE_PATH)
    data = parse_input(INPUT_PATH)

    print("\n** Part 1 **")
    # print(f"sample: {part_1(deepcopy(sample))}")
    print(f"data: {part_1(deepcopy(data))}")

    print("\n** Part 2 **")
    print(f"sample: {part_2(sample)}")
    print(f"data: {part_2(data)}")


if __name__ == "__main__":
    run()

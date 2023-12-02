from copy import deepcopy
from functools import reduce
import operator
from pathlib import Path

PATH = Path(__file__).parent
INPUT_PATH = PATH / "input.txt"
SAMPLE_PATH = PATH / "sample.txt"


def parse_input(path: Path) -> list:
    with open(path, "r") as f:
        lines = [l.strip() for l in f.read().split("\n")]
        return lines


def part_1(data: list):
    bad = set()
    colours = {"red": 12, "green": 13, "blue": 14}
    for i, line in enumerate(data):
        sets = line.split(":")[1].split(";")
        for set_ in sets:
            cubes = [x.strip() for x in set_.split(",")]
            for cube in cubes:
                num, colour = cube.split(" ")
                if int(num) > colours[colour]:
                    bad.add(i + 1)
                    break
    return sum(range(len(data) + 1)) - sum(bad)


def part_2(data: list):
    powers = []
    for line in data:
        colours = {"red": 0, "green": 0, "blue": 0}
        sets = line.split(":")[1].split(";")
        for set_ in sets:
            cubes = [x.strip() for x in set_.split(",")]
            for cube in cubes:
                num, colour = cube.split(" ")
                colours[colour] = max(colours[colour], int(num))
        powers.append(reduce(operator.mul, colours.values(), 1))
    return sum(powers)


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

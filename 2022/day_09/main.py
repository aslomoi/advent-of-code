import numpy as np
from pathlib import Path

PATH = Path(__file__).parent
INPUT_PATH = PATH / "input.txt"
SAMPLE_PATH = PATH / "sample.txt"


def parse_input(path: Path) -> list:
    with open(path, "r") as f:
        lines = [
            (l.strip().split()[0], int(l.strip().split()[1]))
            for l in f.read().split("\n")
        ]
        return lines


DIR_MAP = {
    "U": np.array([0, 1]),
    "D": np.array([0, -1]),
    "L": np.array([-1, 0]),
    "R": np.array([1, 0]),
}


def unique_tail_positions(data, knots) -> int:
    visited = set()
    pos = [np.array([0, 0]) for _ in range(knots)]
    for line in data:
        dir_, count = line
        for _ in range(count):
            pos[0] += DIR_MAP[dir_]
            for idx in range(1, len(pos)):
                diff = pos[idx - 1] - pos[idx]
                if np.any(abs(diff) == 2):
                    pos[idx] += np.array([np.sign(i) for i in diff])

            visited.add(tuple(pos[-1]))

    return len(visited)


def part_1(data: list):
    return unique_tail_positions(data, knots=2)


def part_2(data: list):
    return unique_tail_positions(data, knots=10)


def run():
    sample = parse_input(SAMPLE_PATH)
    data = parse_input(INPUT_PATH)

    print("\n** Part 1 **")
    print(f"sample: {part_1(sample)}")
    print(f"data: {part_1(data)}")

    print("\n** Part 2 **")
    print(f"sample: {part_2(sample)}")
    print(f"data: {part_2(data)}")


if __name__ == "__main__":
    run()

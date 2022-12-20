from copy import deepcopy
from pathlib import Path

PATH = Path(__file__).parent
INPUT_PATH = PATH / "input.txt"
SAMPLE_PATH = PATH / "sample.txt"


def parse_input(path: Path) -> list:
    with open(path, "r") as f:
        lines = [int(l.strip()) for l in f.read().split("\n")]
        return lines


def part_1(data: list):
    L = len(data)
    moves = data.copy()
    data = [(x, False) for x in data]

    for move in moves:
        idx = data.index((move, False))
        data = data[idx + 1:] + data[:idx]
        idx2 = move % (L - 1)
        data.insert(idx2, (move, True))

    zero = data.index((0, True))
    return (
        data[(zero + 1000) % L][0]
        + data[(zero + 2000) % L][0]
        + data[(zero + 3000) % L][0]
    )


def part_2(data: list):
    L = len(data)
    zero_find_by = data.index(0)
    data = [(x * 811589153, -1) for x in data]
    moves = [x[0] for x in data]
    print(moves)

    for i in range(10):
        for j, move in enumerate(moves):
            if i == 0:
                find_by = -1
            else:
                find_by = j
            idx = data.index((move, find_by))
            data = data[idx + 1:] + data[:idx]
            idx2 = move % (L - 1)
            data.insert(idx2, (move, j))

    zero = data.index((0, zero_find_by))
    return (
        data[(zero + 1000) % L][0]
        + data[(zero + 2000) % L][0]
        + data[(zero + 3000) % L][0]
    )


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

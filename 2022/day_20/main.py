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
    zero_find_by = data.index(0)
    moves = data.copy()
    data = [(x, i) for i, x in enumerate(data)]

    for i, move in enumerate(moves):
        idx = data.index((move, i))
        data = data[idx + 1:] + data[:idx]
        idx2 = move % (L - 1)
        data.insert(idx2, (move, i))

    zero = data.index((0, zero_find_by))
    return (
        data[(zero + 1000) % L][0]
        + data[(zero + 2000) % L][0]
        + data[(zero + 3000) % L][0]
    )


def part_2(data: list):
    L = len(data)
    zero_find_by = data.index(0)
    data = [(x * 811589153, i) for i, x in enumerate(data)]
    moves = [x[0] for x in data]

    for _ in range(10):
        for i, move in enumerate(moves):
            idx = data.index((move, i))
            data = data[idx + 1:] + data[:idx]
            idx2 = move % (L - 1)
            data.insert(idx2, (move, i))

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

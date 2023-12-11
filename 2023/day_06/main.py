from copy import deepcopy
from pathlib import Path

PATH = Path(__file__).parent
INPUT_PATH = PATH / "input.txt"
SAMPLE_PATH = PATH / "sample.txt"


def parse_input(path: Path) -> list:
    with open(path, "r") as f:
        lines = [l.strip() for l in f.read().split("\n")]
        return lines


def part_1(data: list):
    times = [int(i) for i in data[0].split()[1:]]
    records = [int(i) for i in data[1].split()[1:]]
    result = 1
    for time, record in zip(times, records):
        result *= sum(1 for i in range(time + 1) if i + (time - 1 - i) * i > record)
    return result


def part_2(data: list):
    time = int("".join(data[0].split()[1:]))
    record = int("".join(data[1].split()[1:]))
    return sum(1 for i in range(time + 1) if i + (time - 1 - i) * i > record)


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

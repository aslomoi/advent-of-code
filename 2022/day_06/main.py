from collections import Counter
from pathlib import Path

PATH = Path(__file__).parent
INPUT_PATH = PATH / "input.txt"
SAMPLE_PATH = PATH / "sample.txt"


def parse_input(path: Path) -> str:
    with open(path, "r") as f:
        lines = f.read()
        return lines


def part_1(data: list):
    for i in range(len(data) - 4):
        c = Counter(data[i : i + 4])
        if all((i == 1 for i in c.values())):
            return i + 4


def part_2(data: list):
    for i in range(len(data) - 14):
        c = Counter(data[i : i + 14])
        if all((i == 1 for i in c.values())):
            return i + 14


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

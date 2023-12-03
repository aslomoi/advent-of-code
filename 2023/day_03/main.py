from collections import defaultdict
from copy import deepcopy
import re
from pathlib import Path

PATH = Path(__file__).parent
INPUT_PATH = PATH / "input.txt"
SAMPLE_PATH = PATH / "sample.txt"


def parse_input(path: Path) -> list:
    with open(path, "r") as f:
        lines = [l.strip() for l in f.read().split("\n")]
        return lines


def has_symbol(substring: str) -> bool:
    return bool(re.findall(r"[^0-9.]", substring))


def part_1(data: list):
    total = 0
    end = 0
    for r, row in enumerate(data):
        matches = re.finditer(r"\d+", row)
        for match_ in matches:
            start = match_.start()
            end = match_.end()
            num = int(match_.group())
            if r > 1 and has_symbol(
                data[r - 1][max(start - 1, 0) : min(end + 1, len(row))],
            ):
                total += num
            elif r < len(data) and has_symbol(
                data[r + 1][max(start - 1, 0) : min(end + 1, len(row))]
            ):
                total += num
            elif start > 0 and has_symbol(row[start - 1]):
                total += num
            elif end < len(row) and has_symbol(row[end]):
                total += num

    return total


def part_2(data: list):
    end = 0
    gears = defaultdict(list)
    for r, row in enumerate(data):
        matches = re.finditer(r"\d+", row)
        for match_ in matches:
            start = match_.start()
            end = match_.end()
            num = int(match_.group())
            if r > 1 and has_symbol(
                data[r - 1][max(start - 1, 0) : min(end + 1, len(row))]
            ):
                for c in range(max(start - 1, 0), min(end + 1, len(row))):
                    if data[r - 1][c] == "*":
                        gears[(r - 1, c)].append(num)
            elif r < len(data) and has_symbol(
                data[r + 1][max(start - 1, 0) : min(end + 1, len(row))]
            ):
                for c in range(max(start - 1, 0), min(end + 1, len(row))):
                    if data[r + 1][c] == "*":
                        gears[(r + 1, c)].append(num)
            elif start > 0 and has_symbol(row[start - 1]):
                if row[start - 1] == "*":
                    gears[(r, start - 1)].append(num)
            elif end < len(row) and has_symbol(row[end]):
                if row[end] == "*":
                    gears[(r, end)].append(num)
    return sum(v[0] * v[1] for v in gears.values() if len(v) == 2)


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

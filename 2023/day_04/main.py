from copy import deepcopy
from functools import lru_cache
from pathlib import Path

PATH = Path(__file__).parent
INPUT_PATH = PATH / "input.txt"
SAMPLE_PATH = PATH / "sample.txt"


def parse_input(path: Path) -> list:
    with open(path, "r") as f:
        lines = [l.strip() for l in f.read().split("\n")]
        return lines


def part_1(data: list):
    total = 0
    for line in data:
        winners, yours = line.split(":")[1].split(" | ")
        winners = [w.strip() for w in winners.split(" ") if w.strip() != ""]
        yours = [y.strip() for y in yours.split(" ") if y.strip() != ""]
        matches = len(set(winners) & set(yours))
        total += 2 ** (matches - 1) if matches else 0

    return total


def part_2(data: list):
    vals = []
    for line in data:
        winners, yours = line.split(":")[1].split(" | ")
        winners = [w.strip() for w in winners.split(" ") if w.strip() != ""]
        yours = [y.strip() for y in yours.split(" ") if y.strip() != ""]
        vals.append(len(set(winners) & set(yours)))

    copies = {i: list(range(i + 1, i + v + 1)) for i, v in enumerate(vals, 1)}

    @lru_cache(maxsize=None)
    def get_counts(idx):
        return 1 + sum(get_counts(i) for i in copies[idx])

    return sum(get_counts(i) for i in copies.keys())


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

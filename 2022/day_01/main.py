from pathlib import Path

PATH = Path(__file__).parent
INPUT_PATH = PATH / "input.txt"
SAMPLE_PATH = PATH / "sample.txt"


def parse_input(path: Path) -> list:
    with open(path, "r") as f:
        lines = [l.strip() for l in f.read().split("\n\n")]
        final = [[int(y) for y in x.splitlines()] for x in lines]
        return final


def part_1(data: list):
    sums = sorted([sum(x) for x in data])
    return sums[-1]


def part_2(data: list):
    sums = sorted([sum(x) for x in data])
    return sum(sums[-3:])


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

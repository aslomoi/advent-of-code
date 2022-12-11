from pathlib import Path

PATH = Path(__file__).parent
INPUT_PATH = PATH / "input.txt"
SAMPLE_PATH = PATH / "sample.txt"


def parse_input(path: Path) -> list:
    with open(path, "r") as f:
        lines = [l.strip() for l in f.read().split("\n")]
        data = []
        for line in lines:
            e1_ = list(int(x) for x in line.split(",")[0].split("-"))
            e1 = set(range(e1_[0], e1_[1] + 1))
            e2_ = list(int(x) for x in line.split(",")[1].split("-"))
            e2 = set(range(e2_[0], e2_[1] + 1))
            data.append((e1, e2))
        return data


def part_1(data: list):
    num = 0
    for e1, e2 in data:
        if e1.issubset(e2) or e1.issuperset(e2):
            num += 1
    return num


def part_2(data: list):
    num = 0
    for e1, e2 in data:
        if e1.intersection(e2):
            num += 1
    return num


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

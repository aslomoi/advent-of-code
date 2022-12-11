from pathlib import Path

PATH = Path(__file__).parent
INPUT_PATH = PATH / "input.txt"
SAMPLE_PATH = PATH / "sample.txt"


def parse_input(path: Path) -> list:
    with open(path, "r") as f:
        lines = [l.strip() for l in f.read().split("\n")]
        return lines


def part_1(data: list):
    ints = []
    for line in data:
        set_a = set(line[: len(line) // 2])
        set_b = set(line[len(line) // 2 :])
        ints.append((set_a & set_b).pop())
    return sum(convert_char(x) for x in ints)


def convert_char(old):
    if len(old) != 1:
        return 0
    new = ord(old)
    if 65 <= new <= 90:
        # Upper case letter
        return new - 64 + 26
    elif 97 <= new <= 122:
        # Lower case letter
        return new - 96
    # Unrecognized character
    return 0


def part_2(data: list):
    ints = []
    for i, j, k in zip(*(iter(data),) * 3):
        ints.append((set(i) & set(j) & set(k)).pop())
    return sum(convert_char(x) for x in ints)


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

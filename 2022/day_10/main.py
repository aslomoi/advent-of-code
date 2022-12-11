from pathlib import Path

PATH = Path(__file__).parent
INPUT_PATH = PATH / "input.txt"
SAMPLE_PATH = PATH / "sample.txt"


def parse_input(path: Path) -> list:
    with open(path, "r") as f:
        lines = [l.strip().split() for l in f.read().split("\n")]
        return lines


def part_1(data: list):
    X = 1
    signals = []
    cycles = 0

    def cycle():
        nonlocal cycles
        cycles += 1
        if (cycles - 20) % 40 == 0:
            signals.append(X * cycles)

    for line in data:
        cycle()
        match line:
            case ["noop"]:
                pass
            case ["addx", num]:
                cycle()
                X += int(num)

    return sum(signals)


def part_2(data: list):
    X = 1
    pixels = ""
    cycles = 0

    def cycle():
        nonlocal pixels
        nonlocal cycles
        c = cycles % 40

        if c in range(X - 1, X + 2):
            pixels += "#"
        else:
            pixels += " "

        cycles += 1
        if cycles % 40 == 0:
            pixels += "\n"

    for line in data:
        cycle()
        match line:
            case ["noop"]:
                pass
            case ["addx", num]:
                cycle()
                X += int(num)

    return "\n" + pixels


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

from collections import defaultdict
from copy import deepcopy
from pathlib import Path

PATH = Path(__file__).parent
INPUT_PATH = PATH / "input.txt"
SAMPLE_PATH = PATH / "sample.txt"


def parse_input(path: Path) -> str:
    with open(path, "r") as f:
        return f.read()


def get_hash(word):
    val = 0
    for c in word:
        val += ord(c)
        val *= 17
        val = val % 256
    return val


def part_1(data: str):
    return sum([get_hash(word) for word in data.split(",")])


def part_2(data: str):
    boxes = defaultdict(list)
    for cmd in data.split(","):
        if "=" in cmd:
            label, val = cmd.split("=")
            box = get_hash(label)
            length = int(val)
            for lens in boxes[box]:
                if lens[0] == label:
                    lens[1] = length
                    break
            else:
                boxes[box].append([label, length])
        else:
            label = cmd[:-1]
            box = get_hash(label)
            for i in range(len(boxes[box])):
                if boxes[box][i][0] == label:
                    boxes[box].pop(i)
                    break
    total = 0
    for box, lenses in boxes.items():
        for i, (_, length) in enumerate(lenses, 1):
            total += (box + 1) * i * length
    return total


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

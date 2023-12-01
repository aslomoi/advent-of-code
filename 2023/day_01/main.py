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
    sum = 0
    for word in data:
        nums = [letter for letter in word if letter.isdigit()]
        sum += int(nums[0] + nums[-1])
    return sum


def part_2(data: list):
    sum = 0
    strs = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]
    for word in data:
        nums = []
        for i, letter in enumerate(word):
            if letter.isdigit():
                nums.append(letter)
            else:
                for j, n in enumerate(strs):
                    if word[i:].startswith(n):
                        nums.append(str(j + 1))
        sum += int(nums[0] + nums[-1])
    return sum


def run():
    sample = parse_input(SAMPLE_PATH)
    data = parse_input(INPUT_PATH)

    print("\n** Part 1 **")
    # print(f"sample: {part_1(deepcopy(sample))}")
    print(f"data: {part_1(deepcopy(data))}")

    print("\n** Part 2 **")
    # print(f"sample: {part_2(sample)}")
    print(f"data: {part_2(data)}")


if __name__ == "__main__":
    run()

import re
from copy import deepcopy
from pathlib import Path

PATH = Path(__file__).parent
INPUT_PATH = PATH / "input.txt"
SAMPLE_PATH = PATH / "sample.txt"


def parse_input(path: Path) -> list:

    with open(path, "r") as f:
        stack_str, move_str = f.read().split("\n\n")

        stacks = [
            list("".join(reversed(i)).strip())
            for i in zip(*reversed(stack_str.splitlines()[:-1]))
            if i[0].isalpha()
        ]

        moves = [list(map(int, re.findall(r"\d+", l))) for l in move_str.splitlines()]
        return [stacks, moves]


def part_1(data: list):
    stacks, moves = data
    for num, frm, to in moves:
        crates = [stacks[frm - 1].pop(0) for _ in range(num)]
        stacks[to - 1] = [*reversed(crates), *stacks[to - 1]]
    return "".join(i[0] for i in stacks)


def part_2(data: list):
    stacks, moves = data
    for num, frm, to in moves:
        crates = [stacks[frm - 1].pop(0) for _ in range(num)]
        stacks[to - 1] = [*crates, *stacks[to - 1]]
    return "".join(i[0] for i in stacks)


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

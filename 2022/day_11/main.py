from copy import deepcopy
import numpy as np
from pathlib import Path
import re

PATH = Path(__file__).parent
INPUT_PATH = PATH / "input.txt"
SAMPLE_PATH = PATH / "sample.txt"


def parse_input(path: Path) -> list:
    with open(path, "r") as f:
        lines = [l.strip() for l in f.read().split("\n\n")]
        monkeys = []
        for monkey in lines:
            for i, line in enumerate([l.strip() for l in monkey.split("\n")]):
                match i:
                    case 0:
                        pass
                    case 1:
                        items = [int(i) for i in line.split(": ")[1].split(", ")]
                    case 2:
                        op = line.split(" = ")[1]
                        # verify before eval
                        assert re.match(r"^(old|\d+) (\*|\+) (old|\d+)$", op)
                    case 3:
                        test = int(line.split("by ")[1])
                    case 4:
                        true = int(line.split("monkey ")[1])
                    case 5:
                        false = int(line.split("monkey ")[1])
            monkeys.append(
                Monkey(items, lambda old, op=op: eval(op), test, true, false)
            )
        return monkeys


class Monkey:
    def __init__(self, items, op, test, true, false):
        self.items = items
        self.worry = 0
        self.op = op
        self.test = test
        self.true = true
        self.false = false
        self.inspected = 0

    def turn(self, limit=None):
        global monkeys
        while self.items:
            self.inspected += 1
            worry = self.op(self.items.pop())
            if limit:
                worry %= limit
            else:
                worry //= 3

            next_ = self.true if worry % self.test == 0 else self.false
            monkeys[next_].items.append(worry)


monkeys: list[Monkey] = []


def part_1(data: list):
    global monkeys
    monkeys = deepcopy(data)
    for _ in range(20):
        for monkey in monkeys:
            monkey.turn()

    inspected = sorted([monk.inspected for monk in monkeys])
    return inspected[-2] * inspected[-1]


def part_2(data: list):
    global monkeys
    monkeys = deepcopy(data)

    limit = np.prod([m.test for m in monkeys])

    for _ in range(10000):
        for monkey in monkeys:
            monkey.turn(limit)

    inspected = sorted([monk.inspected for monk in monkeys])
    return inspected[-2] * inspected[-1]


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

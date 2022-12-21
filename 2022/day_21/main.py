from copy import deepcopy
from pathlib import Path

PATH = Path(__file__).parent
INPUT_PATH = PATH / "input.txt"
SAMPLE_PATH = PATH / "sample.txt"


def parse_input(path: Path):
    with open(path, "r") as f:
        lines = [l.strip() for l in f.read().split("\n")]
        monkeys = {}
        for line in lines:
            name, inst = line.split(": ")
            try:
                monkeys[name] = int(inst)
            except ValueError:
                m1, op, m2 = inst.split()
                monkeys[name] = [m1, m2, op]
        return monkeys


def part_1(monkeys):
    def yell(monkey):
        cmd = monkeys[monkey]
        if isinstance(cmd, int):
            return cmd
        m1, m2, op = cmd
        match op:
            case "+":
                return yell(m1) + yell(m2)
            case "-":
                return yell(m1) - yell(m2)
            case "*":
                return yell(m1) * yell(m2)
            case "/":
                return yell(m1) / yell(m2)

    return int(yell("root"))


def part_2(monkeys):
    def yell(monkey):
        if monkey == "humn":
            return "x"

        cmd = monkeys[monkey]
        if isinstance(cmd, int):
            return int(cmd)

        m1, m2, op = cmd

        if monkey == "root":
            y1, y2 = yell(m1), yell(m2)
            if isinstance(y1, int):
                return (y1, y2)
            return (y2, y1)

        y1, y2 = yell(m1), yell(m2)

        if isinstance(y1, int) and isinstance(y2, int):
            match op:
                case "+":
                    return int(y1 + y2)
                case "-":
                    return int(y1 - y2)
                case "*":
                    return int(y1 * y2)
                case "/":
                    return int(y1 / y2)
        else:
            if op == "-" and isinstance(y1, int):
                op = "--"
            if isinstance(y1, int):
                return (op, (y1, y2))
            return (op, (y2, y1))

    def unwrap(num, hum):
        op, (n, h) = hum
        if h == "x":
            match op:
                case "+":
                    return num - n
                case "-":
                    return num + n
                case "*":
                    return num / n
                case "/":
                    return num * n
            return (num, hum)
        match op:
            case "+":
                return unwrap(num - n, h)
            case "-":
                return unwrap(num + n, h)
            case "*":
                return unwrap(num / n, h)
            case "/":
                return unwrap(num * n, h)
            case "--":
                return unwrap(n - num, h)

    o1, o2 = yell("root")

    return int(unwrap(o1, o2))


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

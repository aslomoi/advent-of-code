from collections import defaultdict
from copy import deepcopy
from pathlib import Path

PATH = Path(__file__).parent
INPUT_PATH = PATH / "input.txt"
SAMPLE_PATH = PATH / "sample.txt"


def parse_input(path: Path):
    with open(path, "r") as f:
        lines = [l.strip() for l in f.read().split("\n")]
        elves = set()
        for r, row in enumerate(lines):
            for c, v in enumerate(row):
                if v == "#":
                    elves.add((r, c))
        return elves


def north(x):
    if x["N"] or x["NE"] or x["NW"]:
        return False
    return (x["og"][0] - 1, x["og"][1])


def south(x):
    if x["S"] or x["SE"] or x["SW"]:
        return False
    return (x["og"][0] + 1, x["og"][1])


def east(x):
    if x["E"] or x["SE"] or x["NE"]:
        return False
    return (x["og"][0], x["og"][1] + 1)


def west(x):
    if x["W"] or x["SW"] or x["NW"]:
        return False
    return (x["og"][0], x["og"][1] - 1)


def part_1(elves: list):
    dirs = [north, south, west, east]

    for rnd in range(10):

        props = defaultdict(list)
        keep = set()

        for (r, c) in elves:
            X = {
                "og": (r, c),
                "N": (r - 1, c) in elves,
                "NE": (r - 1, c + 1) in elves,
                "NW": (r - 1, c - 1) in elves,
                "S": (r + 1, c) in elves,
                "SE": (r + 1, c + 1) in elves,
                "SW": (r + 1, c - 1) in elves,
                "E": (r, c + 1) in elves,
                "W": (r, c - 1) in elves,
            }

            if not (
                X["N"]
                or X["NE"]
                or X["NW"]
                or X["S"]
                or X["SE"]
                or X["SW"]
                or X["E"]
                or X["W"]
            ):
                keep.add((r, c))
            else:
                for d in dirs:
                    if (new := d(X)) is not False:
                        props[new].append((r, c))
                        break
                else:
                    keep.add((r, c))

        for prop, es in props.items():
            if len(es) == 1:
                keep.add(prop)
            else:
                for e in es:
                    keep.add(e)

        dirs.append(dirs.pop(0))
        if elves == keep:
            break
        elves = keep

    xmin, xmax = min(x for _, x in elves), max(x for _, x in elves)
    ymin, ymax = min(y for y, _ in elves), max(y for y, _ in elves)
    cnt = 0
    for y in range(ymin, ymax + 1):
        for x in range(xmin, xmax + 1):
            if (y, x) not in elves:
                cnt += 1
    return cnt


def part_2(elves):
    dirs = [north, south, west, east]

    rnd = 1
    while True:

        props = defaultdict(list)
        keep = set()

        for (r, c) in elves:
            X = {
                "og": (r, c),
                "N": (r - 1, c) in elves,
                "NE": (r - 1, c + 1) in elves,
                "NW": (r - 1, c - 1) in elves,
                "S": (r + 1, c) in elves,
                "SE": (r + 1, c + 1) in elves,
                "SW": (r + 1, c - 1) in elves,
                "E": (r, c + 1) in elves,
                "W": (r, c - 1) in elves,
            }

            if not (
                X["N"]
                or X["NE"]
                or X["NW"]
                or X["S"]
                or X["SE"]
                or X["SW"]
                or X["E"]
                or X["W"]
            ):
                keep.add((r, c))
            else:
                for d in dirs:
                    if (new := d(X)) is not False:
                        props[new].append((r, c))
                        break
                else:
                    keep.add((r, c))

        for prop, es in props.items():
            if len(es) == 1:
                keep.add(prop)
            else:
                for e in es:
                    keep.add(e)

        dirs.append(dirs.pop(0))
        if elves == keep:
            return rnd
        elves = keep
        rnd += 1


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

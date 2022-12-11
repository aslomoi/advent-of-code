from pathlib import Path

PATH = Path(__file__).parent
INPUT_PATH = PATH / "input.txt"
SAMPLE_PATH = PATH / "sample.txt"


def parse_input(path: Path) -> list:
    with open(path, "r") as f:
        lines = [l.strip() for l in f.read().split("\n")]
        trees = {}
        for r, row in enumerate(lines):
            for c, val in enumerate(row):
                trees[(r, c)] = int(val)
        return [(len(lines), len(lines[0])), trees]


def part_1(data):
    (R, C), trees = data
    vis = []

    for (r, c), val in trees.items():
        if r in [0, R - 1] or c in [0, C - 1]:
            vis.append((r, c))
        elif all(trees[(r1, c)] < val for r1 in range(r)):
            vis.append((r, c))
        elif all(trees[(r1, c)] < val for r1 in range(r + 1, R)):
            vis.append((r, c))
        elif all(trees[(r, c1)] < val for c1 in range(c)):
            vis.append((r, c))
        elif all(trees[(r, c1)] < val for c1 in range(c + 1, C)):
            vis.append((r, c))

    return len(vis)


def part_2(data: list):
    (R, C), trees = data
    vis = {}
    for (r, c), val in trees.items():
        count = [0, 0, 0, 0]
        if (r, c) == (2, 1):
            print(1)

        for r1 in reversed(range(r)):
            count[0] += 1
            if trees[(r1, c)] < val:
                continue
            break
        for r1 in range(r + 1, R):
            count[1] += 1
            if trees[(r1, c)] < val:
                continue
            break
        for c1 in reversed(range(c)):
            count[2] += 1
            if trees[(r, c1)] < val:
                continue
            break
        for c1 in range(c + 1, C):
            count[3] += 1
            if trees[(r, c1)] < val:
                continue
            break
        vis[(r, c)] = count

    return max(i[0] * i[1] * i[2] * i[3] for i in vis.values())


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

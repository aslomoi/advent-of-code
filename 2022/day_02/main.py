from pathlib import Path

PATH = Path(__file__).parent
INPUT_PATH = PATH / "input.txt"
SAMPLE_PATH = PATH / "sample.txt"


def parse_input(path: Path) -> list:
    with open(path, "r") as f:
        lines = [l.strip() for l in f.read().split("\n")]
        lines = [x.split(" ") for x in lines]
        return lines


def part_1(data: list):
    score = {"X": 1, "Y": 2, "Z": 3}
    elf = {"A": 1, "B": 2, "C": 3}
    scores = []
    for bet in data:
        his = elf[bet[0]]
        mine = score[bet[1]]
        if mine == his:
            scores.append(3 + mine)
        elif mine - his % 3 == 1:
            scores.append(6 + mine)
        else:
            scores.append(mine)
    return sum(scores)


def part_2(data: list):
    vals = [1, 2, 3]
    score = {"X": 0, "Y": 3, "Z": 6}
    elf = {"A": 1, "B": 2, "C": 3}
    scores = []
    for bet in data:
        his = elf[bet[0]]
        res = score[bet[1]]
        if res == 3:
            scores.append(his + res)
        elif res == 6:
            mine = vals[vals.index(his) - 2]
            scores.append(6 + mine)
        else:
            mine = vals[vals.index(his) - 1]
            scores.append(mine)
    return sum(scores)


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

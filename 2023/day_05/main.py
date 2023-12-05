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
    seeds = [int(i) for i in data.pop(0).split(": ")[1].split()]
    data.pop(0)
    data.append("")
    for line in data:
        if "map" in line:
            mapping = []
        elif line == "":
            new_seeds = []
            for seed in seeds:
                for src_start, dst_start, ran in mapping:
                    if seed >= src_start and seed < src_start + ran:
                        new_seeds.append(dst_start + seed - src_start)
                        break
                else:
                    new_seeds.append(seed)
            seeds = new_seeds
        else:
            dst_start, src_start, ran = (int(i) for i in line.split())
            mapping.append((src_start, dst_start, ran))
    return min(seeds)


def part_2(data: list):
    seed_rules = [int(i) for i in data.pop(0).split(": ")[1].split()]
    seeds = [
        (start, start + end - 1)
        for start, end in zip(seed_rules[::2], seed_rules[1::2])
    ]
    data.pop(0)
    data.append("")
    for line in data:
        if "map" in line:
            mapping = []
        elif line == "":
            new_seeds = []
            while seeds:
                seed = seeds.pop(0)
                for src_start, dst_start, ran in mapping:
                    offset = dst_start - src_start
                    if max(seed[0], src_start) <= min(seed[1], src_start + ran - 1):
                        overlap = (
                            max(seed[0], src_start),
                            min(seed[1], src_start + ran - 1),
                        )
                        new_seeds.append(
                            (
                                overlap[0] + offset,
                                overlap[1] + offset,
                            )
                        )
                        if seed[0] < overlap[0]:
                            seeds.append((seed[0], overlap[0] - 1))
                        if seed[1] > overlap[1]:
                            seeds.append((overlap[1] + 1, seed[1]))
                        break
                else:
                    new_seeds.append(seed)
            seeds = new_seeds
        else:
            dst_start, src_start, ran = (int(i) for i in line.split())
            mapping.append((src_start, dst_start, ran))
    return min(s[0] for s in seeds)


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

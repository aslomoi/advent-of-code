from pathlib import Path

PATH = Path(__file__).parent
INPUT_PATH = PATH / "input.txt"
SAMPLE_PATH = PATH / "sample.txt"


def parse_input(path: Path) -> list:
    with open(path, "r") as f:
        lines = [l.strip() for l in f.read().split("\n$")]
        return lines


def get_parents(ds):
    return ["/".join(ds[: i + 1]) for i in range(len(ds))]


def get_dirs(data):
    dirs = {"/": {"size": 0, "dirs": []}}
    wd = ["/"]
    for cmd in data[1:]:
        lines = cmd.splitlines()
        if lines[0].startswith("ls"):
            for line in lines[1:]:
                p1, p2 = line.split()
                if p1 == "dir":
                    new_dir = "/".join([*wd, p2])
                    dirs["/".join(wd)]["dirs"].append(new_dir)
                    dirs[new_dir] = {"size": 0, "dirs": []}
                else:
                    for d in get_parents(wd):
                        dirs[d]["size"] += int(p1)
        elif lines[0].startswith("cd"):
            dir_ = lines[0].split()[1]
            if dir_ == "..":
                wd.pop()
            elif dir_ == "/":
                wd = ["/"]
            else:
                wd.append(dir_)
    return dirs


def part_1(data: list):
    dirs = get_dirs(data)
    return sum(v["size"] for v in dirs.values() if v["size"] < 100_000)


def part_2(data: list):
    dirs = get_dirs(data)
    sizes = sorted(v["size"] for v in dirs.values())
    return min(s for s in sizes if s > sizes[-1] - 40000000)


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

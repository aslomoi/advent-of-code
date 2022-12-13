from collections import defaultdict, Counter


with open("input.txt") as f:
    lines = f.read().splitlines()

root_mapping = defaultdict(list)
for line in lines:
    a, b = line.split('-')
    if b != "start" and a != "end":
        root_mapping[a].append(b)
    if a != "start" and b != "end":
        root_mapping[b].append(a)

paths = []


def find_paths(path, node):
    if node not in ["start", "end"] and node.islower():
        # Part 1
        # if node in path:
        #     return []
        # Part 2
        count = Counter([x for x in path if x.islower()])
        if any((v > 1 for v in count.values())) and count[node] >= 1:
            return []
    if node == "start" and len(path) > 0:
        return []
    path.append(node)
    if node == "end":
        paths.append(path)
        return []

    children = list(filter(None, (find_paths(path.copy(), child) for child in root_mapping[node])))
    return children


find_paths([], "start")

print(len(paths))

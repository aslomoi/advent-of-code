from itertools import product
with open("input.txt") as f:
    grid = [row for row in f.read().splitlines()]
    grid = [[int(l) for l in x] for x in grid]

MAP = {
    0:1,
    1:2,
    2:3,
    3:4,
    4:5,
    5:6,
    6:7,
    7:8,
    8:9,
    9:1,
    10:2,
    11:3,
    12:4,
    13:5,
    14:6,
    15:7,
    16:8,
    17:9
}
def update(grid):
    l1 = [ line + [MAP[i] for i in line] + [MAP[i+1] for i in line] + [MAP[i+2] for i in line] + [MAP[i+3] for i in line] for line in grid.copy()]
    l2 = [[MAP[i] for i in line] + [MAP[i+1] for i in line] + [MAP[i+2] for i in line] + [MAP[i+3] for i in line]+ [MAP[i+4] for i in line] for line in grid.copy()]
    l3 = [[MAP[i+1] for i in line] + [MAP[i+2] for i in line] + [MAP[i+3] for i in line] + [MAP[i+4] for i in line] + [MAP[i+5] for i in line] for line in grid.copy()]
    l4 = [[MAP[i+2] for i in line] + [MAP[i+3] for i in line] + [MAP[i+4] for i in line] + [MAP[i+5] for i in line] + [MAP[i+6] for i in line] for line in grid.copy()]
    l5 = [[MAP[i+3] for i in line] + [MAP[i+4] for i in line] + [MAP[i+5] for i in line] + [MAP[i+6] for i in line] + [MAP[i+7] for i in line] for line in grid.copy()]
    l1.extend(l2)
    l1.extend(l3)
    l1.extend(l4)
    l1.extend(l5)
    return l1

def dijkstras(grid):
    start = (0, 0)
    end = (len(grid[0]) - 1, len(grid) - 1)

    distance = [[float('inf') for i in range(len(grid[0]))] for j in range(len(grid))]
    distance[0][0] = 0
    prev = [[(-1, -1) for i in range(len(grid[0]))] for j in range(len(grid))]

    queue = list(product(range(len(grid)), repeat=2))
    while queue:
        min_idx = -1
        min_v = float("inf")
        for idx,q in enumerate(queue):
            if distance[q[1]][q[0]] < min_v:
                min_idx = idx
                min_v = distance[q[1]][q[0]]

        loc = queue.pop(min_idx)

        for neib in [(loc[0] - 1, loc[1]), (loc[0] + 1, loc[1]), (loc[0], loc[1] - 1), (loc[0], loc[1] + 1) ]:
            if 0 <= neib[0] <= end[0] and 0 <= neib[1] <= end[1] and neib in queue:
                alt = distance[loc[1]][loc[0]] + grid[neib[1]][neib[0]]
                if alt < distance[neib[1]][neib[0]]:
                    distance[neib[1]][neib[0]] = alt
                    prev[neib[1]][neib[0]] = loc


        if loc == end:
            break
        [print(d) for d in distance]
        print()
    [print(d) for d in distance]

dijkstras((grid))
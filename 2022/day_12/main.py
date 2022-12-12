from copy import deepcopy
import heapq
from pathlib import Path

PATH = Path(__file__).parent
INPUT_PATH = PATH / "input.txt"
SAMPLE_PATH = PATH / "sample.txt"


def parse_input(path: Path):
    with open(path, "r") as f:
        data = [l.strip() for l in f.read().split("\n")]

        R = len(data)
        C = len(data[0])
        maps = {}
        for r in range(R):
            for c in range(C):
                maps[(r, c)] = data[r][c]
                if data[r][c] == "E":
                    end = (r, c)
                    maps[(r, c)] = "z"
        return maps, (R, C), end


def dijkstras(w, h, maps, start=None):
    # Dijkstra's Algorithm
    if not start:
        start = (0, 0)
    shortestDistFromStart = {start: 0}  # shortest distances from start to this position
    visited = {}  # positions of all visited cells
    prev = {}

    #  priority queue initialized with the start and it's shortest distance
    heap = []
    heapq.heappush(heap, (0, start))  # !! important - distance is first in the tuple

    while len(heap):

        minVal, index = heapq.heappop(heap)
        x, y = index

        visited[index] = True

        # get all adjacent neighors
        neighbors = [(x + dx, y + dy) for dx, dy in [(0, -1), (-1, 0), (0, 1), (1, 0)]]
        # that are not out of bounds
        neighbors = [
            (x, y) for x, y in neighbors if x >= 0 and x < w and y >= 0 and y < h
        ]
        # and not already visited
        neighbors = [neighbor for neighbor in neighbors if neighbor not in visited]

        # custom rule
        neighbors = [
            neighbour
            for neighbour in neighbors
            if ord(maps[neighbour]) - ord(maps[(x, y)]) <= 1 or maps[(x, y)] == "S"
        ]

        if shortestDistFromStart[index] < minVal:
            continue

        for neighbor in neighbors:

            # calculate distance of this neighbor from start
            nx, ny = neighbor
            newDistance = shortestDistFromStart[index] + 1
            # if this new distance is better or not set, set it and put this neighbor

            # on the queue
            if (
                neighbor not in shortestDistFromStart
                or newDistance < shortestDistFromStart[neighbor]
            ):
                shortestDistFromStart[neighbor] = newDistance
                prev[neighbor] = index
                heapq.heappush(heap, (newDistance, neighbor))

    return shortestDistFromStart


def part_1(data):
    maps, (R, C), end = data
    paths = dijkstras(R, C, maps=maps)
    return paths[end]


def part_2(data):
    maps, (R, C), end = data
    starts = [k for k, v in maps.items() if v == "a"]

    outs = []
    for start in starts:
        paths = dijkstras(R, C, maps=maps, start=start)
        if end in paths:
            outs.append(paths[end])

    return min(outs)


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

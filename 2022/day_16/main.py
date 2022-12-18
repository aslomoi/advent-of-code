from collections import defaultdict, Counter, deque
from copy import deepcopy
import numpy as np
import re
import heapq
from pathlib import Path
import sys
import itertools as it

sys.setrecursionlimit(5000)
PATH = Path(__file__).parent
INPUT_PATH = PATH / "input.txt"
SAMPLE_PATH = PATH / "sample.txt"


def parse_input(path):
    with open(path, "r") as f:
        lines = [l.strip() for l in f.read().split("\n")]
        return lines


# def best(cur, open_, vs):
#     new_open = [*open_, cur]
#     goto = (new_open,0)
#     for nxt in vs[cur]['to']:
#         if nxt in new_open:
#             continue
#         amt = best(nxt, new_open, vs)
#         if not goto[0] or amt[1] > goto[1]:
#             goto = amt
#     return (goto[0], vs[cur]['r'] + goto[1] + 1)

# def best(paths, remaining, vs):
#     for path in paths:
#         amt = 0
#         for t,v in enumerate(path[1:],1):
#             amt += vs[v]['r'] * (remaining-t)
#         print(path, amt)


# def all_paths(cur, path, open_, vs):
#     path = [*path, cur]
#     paths = []
#     found = None
#     for nxt in vs[cur]['to']:
#         if nxt not in open_:
#             found = True
#             paths.extend(all_paths(nxt, path, vs))
#     if not found:
#         paths = [path]
#     return paths


def time_to(vs):
    dists = {}
    for start in vs.keys():
        shortestDistFromStart = {
            start: 0
        }  # shortest distances from start to this position
        visited = {}  # positions of all visited cells
        prev = {}
        #  priority queue initialized with the start and it's shortest distance
        heap = []
        heapq.heappush(
            heap, (0, start)
        )  # !! important - distance is first in the tuple

        while len(heap):
            minVal, valve = heapq.heappop(heap)
            visited[valve] = True
            # get all adjacent neighors
            neighbors = vs[valve]["to"]

            if shortestDistFromStart[valve] < minVal:
                continue

            for neighbor in neighbors:
                # calculate distance of this neighbor from start
                newDistance = shortestDistFromStart[valve] + 1
                # if this new distance is better or not set, set it and put this neighbor
                # on the queue
                if (
                    neighbor not in shortestDistFromStart
                    or newDistance < shortestDistFromStart[neighbor]
                ):
                    shortestDistFromStart[neighbor] = newDistance
                    prev[neighbor] = valve
                    heapq.heappush(heap, (newDistance, neighbor))
        del shortestDistFromStart[start]
        dists[start] = shortestDistFromStart
    return dists


def parse_valves(data):
    vs = {}
    openable = set()
    for line in data:
        p1, p2 = line.split(";")
        v = p1.split()[1]
        rate = int(p1.split("rate=")[1])
        if "valves" in p2:
            valves = p2.split("valves ")[1].split(", ")
        else:
            valves = [p2.split()[-1]]

        vs[v] = {"r": rate, "to": valves}
        if rate:
            openable.add(v)
    return vs, openable


def get_pressure(parts, vs, dists, mins):
    total = 0
    final = 0
    for part in parts:
        try:
            steps = [dists[a][b] + 1 for a, b in zip(["AA", *part], part)]
        except KeyError:
            continue
        capped_steps = np.array([x for x in np.cumsum(steps) if x < mins])
        if len(capped_steps) < len(steps):
            final += 1
        cum_steps = mins - capped_steps
        total += np.dot(cum_steps, [vs[v]["r"] for v in part[: len(cum_steps)]])
    return total, final == len(parts)


def part_1(data):
    vs, openable = parse_valves(data)
    dists = time_to(vs)

    MINS = 30
    starts = [[]]

    RETAIN = 10
    LOOKAHEAD = 3
    INCR = 1

    already = 0
    best = 0

    while True:
        scores = defaultdict(int)
        for start in starts:
            options = openable - set(start)
            if not options:
                pressure, _ = get_pressure([[*start]], vs, dists, MINS)
                best = max(best, pressure)
                continue
            for perm in it.permutations(options, min(len(options), LOOKAHEAD)):
                trial = (*start, *perm)
                pressure, final = get_pressure([trial], vs, dists, MINS)
                if final:
                    best = max(best, pressure)
                else:
                    key = trial[: already + INCR]
                    scores[key] = max(pressure, scores[key])
        starts = set(
            x[0]
            for x in sorted(scores.items(), key=lambda x: x[1], reverse=True)[:RETAIN]
        )
        if not starts:
            return best
        already += INCR
    return False


def part_2(data):
    vs, openable = parse_valves(data)
    dists = time_to(vs)

    MINS = 26
    starts = [[(), ()]]

    RETAIN = 400
    LOOKAHEAD = 3
    INCR = 2

    best = 0
    already = 0

    while True:
        scores = defaultdict(int)
        for ix, start in enumerate(starts):
            options = openable - set(v for c in start for v in c)

            if not options:
                pressure, _ = get_pressure(start, vs, dists, MINS)
                best = max(best, pressure)
                continue

            mid = min(len(options), LOOKAHEAD) // 2
            for i, perm in enumerate(
                it.permutations(options, min(len(options), LOOKAHEAD))
            ):
                trials = [(perm[mid:], perm[:mid]), (perm[mid + 1 :], perm[: mid + 1])]

                for trial in trials:
                    p1 = (*start[0], *trial[0])
                    p2 = (*start[1], *trial[1])
                    pressure, final = get_pressure([p1, p2], vs, dists, MINS)
                    if final:
                        best = max(best, pressure)
                    else:
                        key = tuple(set([p1[: already + INCR], p2[: already + INCR]]))
                        scores[key] = max(pressure, scores[key])

        starts = set(
            x[0]
            for x in sorted(scores.items(), key=lambda x: x[1], reverse=True)[:RETAIN]
        )
        if not starts:
            return best
        already += INCR
    return False


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

import math
from collections import defaultdict
with open('day10/input.txt') as f:
    input_raw = f.read().strip()
    grid = input_raw.splitlines()

h,w = len(grid), len(grid[0])

def compute_sight(pos, grid):
    angles = set()
    for j in range(h):
        for i in range(w):
            if grid[j][i] == '#' and (i,j) != pos:
                angle = (math.atan2(j - pos[1], i - pos[0]))
                angles.add(angle)
    return angles


def find_asteroids_in_sight(grid):
    asteroids = {}
    for j in range(h):
        for i in range(w):
            if grid[j][i] == '#':
                in_sight = compute_sight((i,j), grid)
                asteroids[(i,j)] = len(in_sight)
                # print(len(in_sight), end='')
            # else:
            #     # print(chr(9608), end='')
    return asteroids

## Part 1
asteroids = find_asteroids_in_sight(grid)
pos = max(asteroids, key=asteroids.get)
print(f"Part 1: Position: {pos}, {asteroids[pos]} detected")



## Part 2
def cart_to_polar(origin, coord):
    angle = ( (0.5*math.pi) - math.atan2(coord[1] - origin[1], coord[0] - origin[0]) ) % (math.pi*2)
    r = math.sqrt( math.pow(coord[1] - origin[1],2) + math.pow(coord[0] - origin[0],2) )
    return (r, angle)

def polar_asteroid_map(origin, grid):
    a_map = defaultdict(list)
    for j in range(h):
        for i in range(w):
            if grid[j][i] == '#' and (i,j) != pos:
                pol = cart_to_polar(origin, (i,j))
                a_map[pol[1]].append(pol[0])
    return {k:sorted(v) for k,v in a_map.items()}


def vaporize(pos, grid):
    vaporized = []
    asteroids = polar_asteroid_map(pos, grid)
    while len(asteroids) > 0:
        for a in sorted(asteroids):
            vaporized.append((asteroids[a].pop(0), a))
            if asteroids[a] == []:
                del asteroids[a]
    return vaporized

pos = (11,13)
vaporized = vaporize(pos,grid)
whatth = 1
xth = (pos[0] - vaporized[whatth][0]*math.sin(vaporized[whatth][1]) , pos[1] - vaporized[whatth][0]*math.cos(vaporized[whatth][1]))
print(xth)
pass
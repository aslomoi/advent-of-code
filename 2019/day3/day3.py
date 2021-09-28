with open('day3/input.txt') as f:
    input_raw = f.read().splitlines()
    wire_1 = input_raw[0].split(',')
    wire_2 = input_raw[1].split(',')

def wire_path(wire):
    path = [(0,0)] 

    for instruction in wire:
        (end_x, end_y) = path[-1]

        direction = instruction[:1]
        length = int(instruction[1:])

        if direction == 'R':
            new_path = [(end_x + x, end_y) for x in range(1,length+1)]
        if direction == 'L':
            new_path = [(end_x - x, end_y) for x in range(1,length+1)]
        if direction == 'U':
            new_path = [(end_x, end_y + y) for y in range(1,length+1)]
        if direction == 'D':
            new_path = [(end_x, end_y - y) for y in range(1,length+1)]   

        path.extend(new_path)
        
    return path


def path_cross(path_1, path_2):
    set_1 = set(path_1)
    set_2 = set(path_2)
    crosses = set_1.intersection(set_2)
    crosses.remove((0,0))
    return crosses

manhattan = lambda x: x[0] + x[1]


path_1 = wire_path(wire_1)
path_2 = wire_path(wire_2)
crosses = path_cross(path_1, path_2)

## Part 1
distance = min([manhattan(x) for x in crosses])
print(f"Part 1: {distance}")

## Part 2
min_steps = 1_000_000
for x in crosses:
    steps = path_1.index(x) + path_2.index(x)
    if steps < min_steps:
        min_steps = steps

print(f"Part 2: {min_steps}")
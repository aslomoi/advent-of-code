from collections import defaultdict

with open('day6/input.txt') as f:
        input_raw = f.readlines()
        mappings = [x.strip().split(')') for x in input_raw]

network = defaultdict(list)
reverse_network = {}

for mapping in mappings:
    network[mapping[0]].append(mapping[1])
    reverse_network[mapping[1]] = mapping[0] 

def distance(obj, val=0):
    return val + sum([distance(o, val + 1) for o in network[obj]])

def path(obj, p=[]):
    if not obj in reverse_network:
        return [*p, obj]
    else:
        return path(reverse_network[obj], [*p, obj])

def root(p1, p2):
    for i in p1:
        if i in p2:
            return i

def shifts(o1, o2):
    p1 = path(o1)
    p2 = path(o2)
    base = root(p1, p2)
    return p1.index(base) + p2.index(base) - 2


print(f'Part 1: {distance("COM")}')
print(f'Part 2: {shifts("YOU","SAN")}')

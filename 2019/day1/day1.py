import math

with open('day1/input.txt') as f:
    input_raw = f.read().splitlines()

def fuel(mass):
    return math.floor(mass / 3) - 2

def recursive_fuel(mass):
    new_fuel = fuel(mass)
    if new_fuel <= 0:
        return 0
    else:
        return new_fuel + recursive_fuel(new_fuel)

## Part 1
# fuels = [fuel(int(m)) for m in input_raw]
# print(f'Part 1: {sum(fuels)}')

## Part 2
fuels = [recursive_fuel(int(m)) for m in input_raw]
print(f'Part 2: {sum(fuels)}')

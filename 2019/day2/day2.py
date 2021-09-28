from itertools import permutations


global input_raw
with open('day2/input.txt') as f:
    input_raw = f.read().split(',')


def reset(*,noun, verb):
    program = [int(x) for x in input_raw]
    program[1:3] = [noun,verb] 
    return program


def iteration(pos, program):
    if program[pos] == 1:
        return program[program[pos+1]] + program[program[pos+2]]
    elif program[pos] == 2: 
        return program[program[pos+1]] * program[program[pos+2]]
    elif program[pos] == 99:
        return -1

def run(program):
    pos = 0
    while True:
        val = iteration(pos, program)
        if val == -1:
            break
        program[program[pos+3]] = val
        pos += 4
    return program[0]

print(f'Part 1: {run(reset(noun=12, verb=2))}')

## Part 2
for (noun, verb) in permutations(range(100),2):
        program = reset(noun = noun, verb = verb)
        result = run(program)
        if result == 19690720:
            val = 100*noun + verb
            break

print(f'Part 2: {val}')
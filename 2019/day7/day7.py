import itertools
def digitize(n):
    return [int(d) for d in str(n)]

class Program:
    def __init__(self):
        super().__init__()
        self._get_input() 
        self.pos = 0
        self.halt = False
        self._input_status = 0
        self.output = []

    def _get_input(self):
        with open('day7/input.txt') as f:
            self._input_raw = f.read().split(',')
            self.program = [int(x) for x in self._input_raw]

    def get_param(self, val, param_mode):
        if param_mode == 0:
            return self.program[self.program[val]]
        elif param_mode == 1:
            return self.program[val]
        raise ValueError("Invalid parameter mode")

    def iterate(self):
        op_code, param_modes = self.parse_instruction()
        if op_code == 1:
            val = self.get_param(self.pos+1, param_modes.get(0,0)) + self.get_param(self.pos+2, param_modes.get(1,0))
            self.program[self.program[self.pos+3]] = val
            self.pos += 4
        elif op_code == 2: 
            val = self.get_param(self.pos+1, param_modes.get(0,0)) * self.get_param(self.pos+2, param_modes.get(1,0))
            self.program[self.program[self.pos+3]] = val
            self.pos += 4
        elif op_code == 3:
            if not self._input_status:
                self.program[self.program[self.pos+1]] = self._phase
                self._input_status = True
            else:
                self.program[self.program[self.pos+1]] = self._input
            self.pos += 2
        elif op_code == 4:
            self.output.append(self.get_param(self.pos+1, param_modes.get(0,0)))
            self.pos += 2
            if self._input_status:
                self.pause = True
        elif op_code == 5:
            if self.get_param(self.pos+1, param_modes.get(0,0)) != 0:
                self.pos = self.get_param(self.pos+2, param_modes.get(1,0))
            else:
                self.pos +=3
        elif op_code == 6:
            if self.get_param(self.pos+1, param_modes.get(0,0)) == 0:
                self.pos = self.get_param(self.pos+2, param_modes.get(1,0))
            else:
                self.pos += 3
        elif op_code == 7:
            if self.get_param(self.pos+1, param_modes.get(0,0)) < self.get_param(self.pos+2, param_modes.get(1,0)):
                self.program[self.program[self.pos+3]] = 1
            else:
                self.program[self.program[self.pos+3]] = 0
            if self.program[self.pos+3] != self.pos:
                self.pos += 4
        elif op_code == 8:
            if self.get_param(self.pos+1, param_modes.get(0,0)) == self.get_param(self.pos+2, param_modes.get(1,0)):
                self.program[self.program[self.pos+3]] = 1
            else:
                self.program[self.program[self.pos+3]] = 0
            if self.program[self.pos+3] != self.pos:
                self.pos += 4
        elif op_code == 99:
            self.halt = True

    def parse_instruction(self):
        op_code = self.program[self.pos] % 100
        if self.program[self.pos] == op_code:
            param_modes = []
        else:
            modes = int(self.program[self.pos] / 100)
            param_modes = digitize(modes)
            param_modes.reverse()
        param_modes = dict(enumerate(param_modes))
        return op_code, param_modes

    def run(self, phase, _input):
        self._phase = phase
        self._input = _input
        self.pause = False
        while not self.halt and not self.pause:
            self.iterate()
        return self.halt

def circuit(seq, init=0):
    out = init
    amps = [Program() for i in range(5)]
    active = 0
    while not amps[-1].halt:
        amps[active].run(seq[active], out)
        out = amps[active].output[-1]
        active = (active + 1) % 5
    return out

## Part 1
# best_output = -1
# for seq in itertools.permutations(range(5),5):
#     output = circuit(seq)
#     if output > best_output:
#         best_output = output

# print(f'Part 1: {best_output}')

## Part 2
best_output = -1
for seq in itertools.permutations(range(5,10),5):
    output = circuit(seq)
    if output > best_output:
        best_output = output

print(f'Part 2: {best_output}')

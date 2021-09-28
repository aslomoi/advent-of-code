def digitize(n):
    return [int(d) for d in str(n)]

class Program:
    def __init__(self, input_v):
        super().__init__()
        self._get_input() 
        self.pos = 0
        self.halt = False
        self._input = input_v
        self.output = []

    def _get_input(self):
        with open('day5/input.txt') as f:
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
            self.program[self.program[self.pos+1]] = self._input
            self.pos += 2
        elif op_code == 4:
            self.output.append(self.get_param(self.pos+1, param_modes.get(0,0)))
            self.pos += 2
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

    def run(self):
        self.pos = 0
        while not self.halt:
            self.iterate()
        return self.program[0]

program = Program(5)
program.run()
print(f'Diagnostic Code: {program.output[-1]}')

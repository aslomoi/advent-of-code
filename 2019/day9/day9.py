from collections import defaultdict

def digitize(n):
    return [int(d) for d in str(n)]

class Program:
    def __init__(self):
        super().__init__()
        self._get_input() 
        self.pos = 0
        self.halt = False
        self.base = 0
        self.output = []

    def _get_input(self):
        with open('day9/input.txt') as f:
            self._input_raw = f.read().split(',')
            self.program = defaultdict(lambda: 0, {i:int(x) for i,x in enumerate(self._input_raw)})

    def get_param(self, val, param_mode):
        if param_mode == 0:
                return self.program[self.program[val]]
        elif param_mode == 1:
                return self.program[val]
        elif param_mode == 2:
                return self.program[self.program[val] + self.base]
        raise ValueError("Invalid parameter mode")

    def get_key(self, val, param_mode):
        if param_mode == 2:
            return self.program[val] + self.base
        else:
            return self.program[val]

    def iterate(self):
        op_code, param_modes = self.parse_instruction()
        if param_modes == {0:1, 1:1, 2:2}:
            print('yee')
        if op_code == 1:
            val = self.get_param(self.pos+1, param_modes.get(0,0)) + self.get_param(self.pos+2, param_modes.get(1,0))
            self.program[self.get_key(self.pos+3, param_modes.get(2,0))] = val
            self.pos += 4
        elif op_code == 2: 
            val = self.get_param(self.pos+1, param_modes.get(0,0)) * self.get_param(self.pos+2, param_modes.get(1,0))
            self.program[self.get_key(self.pos+3, param_modes.get(2,0))] = val
            self.pos += 4
        elif op_code == 3:
            self.program[self.get_key(self.pos+1, param_modes.get(0,0))] = self._input
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
                self.program[self.get_key(self.pos+3, param_modes.get(2,0))] = 1
            else:
                self.program[self.get_key(self.pos+3, param_modes.get(2,0))] = 0
            if self.program[self.pos+3] != self.pos:
                self.pos += 4
        elif op_code == 8:
            if self.get_param(self.pos+1, param_modes.get(0,0)) == self.get_param(self.pos+2, param_modes.get(1,0)):
                self.program[self.get_key(self.pos+3, param_modes.get(2,0))] = 1
            else:
                self.program[self.get_key(self.pos+3, param_modes.get(2,0))] = 0
            if self.program[self.pos+3] != self.pos:
                self.pos += 4
        elif op_code == 9:
            self.base += self.get_param(self.pos+1, param_modes.get(0,0))
            self.pos += 2
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

    def run(self, _input = None):
        self._input = _input
        self.pause = False
        while not self.halt and not self.pause:
            self.iterate()
        return self.halt

comp = Program()
while not comp.halt:
    comp.run(2)
    print(f'output: {comp.output}')

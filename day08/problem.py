from misc import init_day
from input import get_file_lines_with_no_blanks

init_day(__file__, 8)


class Machine:
    def __init__(self):
        self.pc = 0
        self.acc = 0
        self.memory = []
        self.looped = False

    def parse(self, mnemonics):
        self.memory = []
        for line in mnemonics:
            operation, argument = line.split(' ')
            argument = int(argument)
            self.memory.append((operation, argument))

    def run(self):
        self.pc = 0
        self.acc = 0
        self.looped = False
        pc_already_executed = {}
        memory_size = len(self.memory)
        while self.pc < memory_size:
            already_executed = pc_already_executed.get(self.pc, False)
            if already_executed:
                self.looped = True
                return
            pc_already_executed[self.pc] = True
            operation, arg = self.memory[self.pc]
            operation_method = getattr(self, f'operation_{operation}', None)
            if operation_method is None:
                raise ValueError(f'Unknown operation "{operation}"')
            operation_method(arg)

    def operation_nop(self, arg):
        self.pc += 1

    def operation_jmp(self, arg):
        self.pc += arg

    def operation_acc(self, arg):
        self.acc += arg
        self.pc += 1


def solve_part_1(part1_input):
    machine = Machine()
    machine.parse(part1_input)
    machine.run()
    return machine.acc


def solve_part_2(part2_input):
    patched_operation = {
        'nop': 'jmp',
        'jmp': 'nop',
    }
    machine = Machine()
    machine.parse(part2_input)
    original_memory = machine.memory[:]
    for patch_pc in range(0, len(original_memory)):
        machine.memory = original_memory[:]
        operation, arg = machine.memory[patch_pc]
        machine.memory[patch_pc] = (patched_operation.get(operation, operation), arg)
        machine.run()
        if not machine.looped:
            return machine.acc
    raise Exception('Unable to patch!')


test_input = get_file_lines_with_no_blanks('test.txt')

assert solve_part_1(test_input) == 5
assert solve_part_2(test_input) == 8

problem_input = get_file_lines_with_no_blanks('input.txt')

print(f'Part 1: {solve_part_1(problem_input)}')
print(f'Part 2: {solve_part_2(problem_input)}')

import re

class Computer:
    def __init__(self, a, b, c, opcodes):
        self.a, self.b, self.c = a, b, c
        self.opcodes = opcodes
        self.p = 0
        self.output = []
        self.commands = {0: self.adv, 1: self.bxl, 2: self.bst, 3: self.jnz, 4: self.bxc,
                    5: self.out, 6: self.bdv, 7: self.cdv}

    def combo(self, operand: int):
        if operand == 4:
            return self.a
        if operand == 5:
            return self.b
        if operand == 6:
            return self.c
        assert operand != 7, 'not valid program'
        return operand

    def adv(self, operand: int):
        num = self.combo(operand)
        self.a = self.a // 2 ** num
        self.p += 2

    def bxl(self, operand: int):
        self.b = self.b ^ operand
        self.p += 2

    def bst(self, operand: int):
        self.b = self.combo(operand) % 8
        self.p += 2

    def jnz(self, operand: int):
        if self.a == 0:
            self.p += 2
        else:
            self.p = operand

    def bxc(self, operand: int):
        self.b = self.b ^ self.c
        self.p += 2

    def out(self, operand: int):
        self.output.append(self.combo(operand) % 8)
        self.p += 2

    def bdv(self, operand: int):
        num = self.combo(operand)
        self.b = self.a // 2 ** num
        self.p += 2

    def cdv(self, operand: int):
        num = self.combo(operand)
        self.c = self.a // 2 ** num
        self.p += 2


def get_nums(line):
    all_nums = re.findall(r'(-?\d+)', line)
    return list(map(int, all_nums))

def get_num(line):
    nums = get_nums(line)
    assert len(nums) == 1
    return nums[0]

def part1():
    with open('input_ex.txt', 'r') as file:
        content = file.readlines()
        a, b, c = map(get_num, content[0:3])
        opcodes = get_nums(content[4])

    computer = Computer(a, b, c, opcodes)
    while True:
        if computer.p < len(opcodes) and computer.p + 1 < len(opcodes):
            operand = opcodes[computer.p + 1]
            computer.commands[opcodes[computer.p]](operand)
        else:
            break

    print(f'a: {computer.a}, b: {computer.b}, c: {computer.c}')
    print(','.join(map(str, computer.output)))

part1()
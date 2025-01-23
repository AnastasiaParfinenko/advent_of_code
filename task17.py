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

    def work(self):
        while True:
            if self.p < len(self.opcodes) and self.p + 1 < len(self.opcodes):
                operand = self.opcodes[self.p + 1]
                self.commands[self.opcodes[self.p]](operand)
            else:
                break

        return self.output


def get_nums(line):
    all_nums = re.findall(r'(-?\d+)', line)
    return list(map(int, all_nums))


def get_num(line):
    nums = get_nums(line)
    assert len(nums) == 1
    return nums[0]


def get_data():
    with open('input17.txt', 'r') as file:
        content = file.readlines()
        a, b, c = map(get_num, content[0:3])
        opcodes = get_nums(content[4])

    return Computer(a, b, c, opcodes)


def part1():
    computer = get_data()
    print(','.join(map(str, computer.work())))


def search_next_a(opcodes, a_base, end):
    i = 0
    while True:
        a = 8 * a_base + i
        computer = Computer(a, 0, 0, opcodes)
        if computer.work() == opcodes[-end:]:
            return a
        i += 1


def part2():
    with open('input17.txt', 'r') as file:
        content = file.readlines()
        opcodes = get_nums(content[4])

    a_base = 0
    for end in range(1, len(opcodes) + 1):
        a_base = search_next_a(opcodes, a_base, end)

    print(a_base)


part1()
part2()

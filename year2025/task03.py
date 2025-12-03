def get_data(name):
    with open(name, 'r', encoding='utf-8') as file:
        banks = [[int(c) for c in line.strip()] for line in file]
    return banks


def part1():
    banks = get_data('input03_1.txt')
    res = 0
    for bank in banks:
        pos, max_el_1 = max(enumerate(bank), key=lambda x: x[1])
        if pos == len(bank) - 1:
            max_el_2 = max(bank[:-1])
            res += max_el_2 * 10 + max_el_1
        else:
            max_el_2 = max(bank[pos + 1:])
            res += max_el_1 * 10 + max_el_2

    return res


def part2():
    banks = get_data('input03_1.txt')
    batteries_number = 12
    res = 0
    l = len(banks[0])
    for bank in banks:
        joltage = 0
        pos1 = 0
        pos2 = l - batteries_number + 1

        for i in range(batteries_number):
            pos, max_el = max(
                ((j, bank[j]) for j in range(pos1, pos2 + i)),
                key=lambda x: x[1]
            )
            joltage = joltage * 10 + max_el
            pos1 = pos + 1

        res += joltage

    return res


a1 = part1()
print(a1)
assert a1 == 17332, a1

a2 = part2()
print(a2)
assert a2 == 172516781546707, a2

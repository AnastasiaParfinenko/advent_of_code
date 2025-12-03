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

    print(res)


def part2():
    banks = get_data('input03_1.txt')
    batteries_number = 12
    res = 0
    l = len(banks[-1])
    for bank in banks:
        joltage = 0
        pos1, pos2 = 0, l

        count = 0
        while count < batteries_number:
            max_el = max(bank[pos1:pos2])
            pos = bank[pos1:pos2].index(max_el)
            if pos1 + pos <= l - (batteries_number - count):
                joltage = joltage * 10 + max_el
                pos1 += pos + 1
                pos2 = l
                count += 1
            else:
                pos2 = pos1 + pos

        res += joltage

    print(res)


part1()
# 17332
part2()
# 172516781546707

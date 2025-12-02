def get_data(name):
    with open(name, 'r', encoding='utf-8') as file:
        ranges = [tuple(map(int, borders.split('-'))) for borders in file.read().split(',')]
    return ranges


def part1():
    ranges = get_data('input02_1.txt')
    res = 0
    for paar in ranges:
        for n in range(paar[0], paar[1] + 1):
            str_n = str(n)
            len_n = len(str_n)
            if len_n % 2 == 0 and str_n[:len_n // 2] == str_n[len_n // 2:]:
                res += n
    print(res)


def part2():
    ranges = get_data('input02_1.txt')
    res = 0
    for paar in ranges:
        for n in range(paar[0], paar[1] + 1):
            str_n = str(n)
            len_n = len(str_n)
            for len_seq in range(1, len_n // 2 + 1):
                if len_n % len_seq == 0 and (len_n // len_seq) * str_n[:len_seq] == str_n:
                    res += n
                    break
    print(res)


part1()
# 41294979841
part2()
# 66500947346
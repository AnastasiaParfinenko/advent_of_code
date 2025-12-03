def get_data(name):
    with open(name, 'r', encoding='utf-8') as file:
        ranges = [tuple(map(int, borders.split('-'))) for borders in file.read().split(',')]
    return ranges


def part1():
    ranges = get_data('input02_1.txt')
    res = 0
    for a, b in ranges:
        for n in range(a, b + 1):
            str_n = str(n)
            len_n = len(str_n)
            if len_n % 2 == 0 and str_n[:len_n // 2] == str_n[len_n // 2:]:
                res += n
    print(res)


def part2():
    ranges = get_data('input02_1.txt')
    res = 0
    for a, b in ranges:
        for n in range(a, b + 1):
            str_n = str(n)
            if str_n in (str_n + str_n)[1:-1]:
                res += n
    print(res)


part1()
# 41294979841
part2()
# 66500947346

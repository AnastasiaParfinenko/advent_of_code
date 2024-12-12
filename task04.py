def get_table():
    with open('input4.txt', 'r') as file:
        return file.read().splitlines()


def search(table):
    return sum(line.count("XMAS") for line in table)


def back_search(table):
    return sum(line.count("SAMX") for line in table)


def back_table(table):
    return [line[::-1] for line in table]


def t_table(table):
    m = len(table)
    return [''.join([line[j] for line in table]) for j in range(m)]


def diag_table(table):
    new_table = []
    m = len(table)
    for s in range(2 * m - 1):
        new_line = ''.join([table[s - i][i] for i in range(max(0, s + 1 - m), min(m - 1,s) + 1)])
        new_table.append(new_line)
    return new_table


def part1():
    table = get_table()

    res1 = search(table)
    res2 = back_search(table)
    res3 = search(t_table(table))
    res4 = back_search(t_table(table))
    res5 = search(diag_table(table))
    res6 = back_search(diag_table(table))
    res7 = search(diag_table(back_table(table)))
    res8 = back_search(diag_table(back_table(table)))

    res = res1 + res2 + res3 + res4 + res5 + res6 + res7 + res8
    return res


def check(i, j, table):
    word1 = table[i - 1][j - 1] + table[i][j] + table[i + 1][j + 1]
    word2 = table[i + 1][j - 1] + table[i][j] + table[i - 1][j + 1]

    if word1 in {'SAM', 'MAS'} and word2 in {'SAM', 'MAS'}:
        return 1

    return 0


def part2():
    table = get_table()
    m = len(table)
    return sum(check(i,j, table) for i in range(1, m - 1) for j in range(1, m - 1))


print(part1())
print(part2())
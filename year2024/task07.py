def get_numbers():
    with open('input7.txt', 'r') as file:
        equations = []
        for line in file:
            equation = [int(num.strip(':')) for num in line.strip('\n').split()]
            equations.append(equation)

        return equations


def calculate1(eq, i, res):
    if res > eq[0]:
        return 0

    if i > len(eq) - 2:
        return eq[0] if res == eq[0] else 0

    return calculate1(eq, i + 1, res + eq[i + 1]) or calculate1(eq, i + 1, res * eq[i + 1])


def part1():
    equations = get_numbers()
    ans = 0
    for eq in equations:
        if calculate1(eq, 1, eq[1]):
            # print(eq)
            ans += calculate1(eq, 1, eq[1])
    print(ans)


def calculate2(eq, i, res):
    if res > eq[0]:
        return 0

    if i > len(eq) - 2:
        return eq[0] if res == eq[0] else 0

    return calculate2(eq, i + 1, res + eq[i + 1]) or \
           calculate2(eq, i + 1, res * eq[i + 1]) or \
           calculate2(eq, i + 1, int(str(res) + str(eq[i + 1])))


def part2():
    equations = get_numbers()
    ans = 0
    for eq in equations:
        if calculate2(eq, 1, eq[1]):
            # print(eq)
            ans += calculate2(eq, 1, eq[1])
    print(ans)


part1()
part2()
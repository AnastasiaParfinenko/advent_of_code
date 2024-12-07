def get_numbers():
    with open('input.txt', 'r') as file:
        equations = []
        for line in file:
            equation = [int(num.strip(':')) for num in line.strip('\n').split()]
            equations.append(equation)

        return equations


def calculate1(eq, i, res, results=None):
    if results is None:
        results = []

    if results or res > eq[0]:
        return

    if i > len(eq) - 2:
        if res == eq[0]:
            results.append(eq[0])
        return

    calculate1(eq, i + 1, res + eq[i + 1], results)
    calculate1(eq, i + 1, res * eq[i + 1], results)

    return results


def part1():
    equations = get_numbers()
    ans = 0
    for eq in equations:
        if calculate1(eq, 1, eq[1]):
            # print(eq)
            ans += int(calculate1(eq, 1, eq[1])[0])
    print(ans)


def calculate2(eq, i, res, results=None):
    if results is None:
        results = []

    if results or res > eq[0]:
        return

    if i > len(eq) - 2:
        if res == eq[0]:
            results.append(eq[0])
        return

    calculate2(eq, i + 1, res + eq[i + 1], results)
    calculate2(eq, i + 1, res * eq[i + 1], results)

    n = len(str(eq[i + 1]))
    calculate2(eq, i + 1, res * 10 ** n + eq[i + 1], results)

    return results


def part2():
    equations = get_numbers()
    ans = 0
    for eq in equations:
        if calculate2(eq, 1, eq[1]):
            # print(eq)
            ans += int(calculate2(eq, 1, eq[1])[0])
    print(ans)


# part1()
part2()
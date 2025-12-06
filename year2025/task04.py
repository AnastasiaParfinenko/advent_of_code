def get_data(name):
    with open(name, 'r', encoding='utf-8') as file:
        grid = [[0 if c == '.' else 1 for c in line.strip()] for line in file]
    return grid


def count_rolls(grid, size, i, j):
    count = 0
    for k in [-1, 0, 1]:
        for l in [-1, 0, 1]:
            if 0 <= i + k < size and 0 <= j + l < size and (k, l) != (0, 0):
                count += grid[i + k][j + l]
    return count


def part1():
    grid = get_data('input04_1.txt')
    size = len(grid)

    res = 0
    for i in range(size):
        for j in range(size):
            if grid[i][j] == 1 and count_rolls(grid, size, i, j) < 4:
                res += 1
    return  res


def part2():
    grid = get_data('input04_1.txt')
    size = len(grid)

    res, res1 = -1, 0
    while res != res1:
        res = res1
        for i in range(size):
            for j in range(size):
                if grid[i][j] == 1 and count_rolls(grid, size, i, j) < 4:
                    res1 += 1
                    grid[i][j] = 0
    return  res


a1 = part1()
print(a1)
assert a1 == 1451, a1

a2 = part2()
print(a2)
assert a2 == 8701, a2
def get_data():
    with open('input.txt', 'r') as file:
        very_long_line = file.read().strip('\n')

        files = {}

        for num in range(len(very_long_line) // 2 + 1):
            files[num] = int(very_long_line[2 * num])

        free_space = [int(very_long_line[2 * n + 1]) for n in range(len(very_long_line) // 2)]

        return files, free_space


def update_data1(files: dict, free_space: list):
    new_order = []

    total_files = sum(files.values())
    s = 0
    b = 0
    e = len(files) - 1
    while total_files > 0:
        new_order += [b] * files[b]
        total_files -= files[b]
        b += 1

        if s < len(free_space):
            while free_space[s] > 0 and total_files > 0:
                new_order.append(e)
                total_files -= 1
                free_space[s] -= 1
                files[e] -= 1
                if files[e] == 0:
                    e -= 1
            s += 1

    return new_order


def part1():
    files, free_space = get_data()
    new_order = update_data1(files, free_space)
    checksum = sum(i * new_order[i] for i in range(len(new_order)))
    print(checksum)


def update_data2(files: dict, free_space: list):
    new_order = []
    moved = set()
    l = len(free_space)
    new_list = [[] for _ in range(l)]
    n = len(files)

    for e in range(n - 1, 0, -1):
        for j in range(e):
            if free_space[j] >= files[e]:
                new_list[j] += [e] * files[e]
                free_space[j] -= files[e]
                moved.add(e)
                break

    for num in range(n):
        if not num in moved:
            new_order += [num] * files[num]
        else:
            new_order += ['.'] * files[num]

        if num < l:
            new_order += new_list[num]
            new_order += ['.'] * free_space[num]

    return new_order


def part2():
    files, free_space = get_data()
    new_order = update_data2(files, free_space)
    checksum = sum(i * new_order[i] for i in range(len(new_order)) if new_order[i] != '.')
    print(checksum)


part1()
part2()

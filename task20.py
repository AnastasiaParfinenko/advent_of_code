def get_data():
    with open('input.txt', 'r') as file:
        path_set = set()
        i = 0
        for line in file:
            j = 0
            for c in line:
                if c == '#':
                    pass
                elif c == '.':
                    path_set.add((i, j))
                elif c == 'S':
                    start = (i, j)
                elif c == 'E':
                    end = (i, j)
                j += 1
            i += 1

        path_set.add(end)

        return start, end, path_set


def neighbours(p):
    i, j = p
    return [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]


def get_order(start: tuple, end: tuple, path_set: set):
    cur_p = start
    num = 0
    numbered_path = {cur_p: num}
    while cur_p != end:
        for new_p in neighbours(cur_p):
            if new_p not in numbered_path and new_p in path_set:
                num += 1
                cur_p = new_p
                numbered_path[cur_p] = num
                break

    return numbered_path


def cheat(numbered_path: dict, cheat_paths: list):
    for p in numbered_path:
        for p1 in neighbours(p):
            if p1 not in numbered_path:
                for p2 in neighbours(p1):
                    if p2 in numbered_path:
                        save = numbered_path[p2] - numbered_path[p] - 2
                        cheat_paths.append(save)


def part12():
    start, end, path_set = get_data()
    numbered_path = get_order(start, end, path_set)
    cheat_paths = []
    cheat(numbered_path, cheat_paths)
    print(sum(1 for el in cheat_paths if el >= 100))


part12()
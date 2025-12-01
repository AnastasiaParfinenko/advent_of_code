from line_profiler import profile

def get_data():
    with open('input.txt', 'r') as file:
        path_set = set()
        for i, line in enumerate(file):
            for j, c in enumerate(line):
                if c == '.':
                    path_set.add((i, j))
                elif c == 'S':
                    start = (i, j)
                elif c == 'E':
                    end = (i, j)

        path_set.add(end)

        return start, end, path_set


def neighbours(p):
    i, j = p
    return [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]

@profile
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


@profile
def cheat(max_dist, min_save, numbered_path: dict):
    count = 0
    for p in numbered_path:
        for i in range(- max_dist, max_dist + 1):
            for j in range(- max_dist + abs(i), max_dist + 1 - abs(i)):
                num_p2 = numbered_path.get((p[0] + i, p[1] + j))
                if num_p2 and num_p2 - numbered_path[p] - abs(i) - abs(j) >= min_save:
                    count += 1
    return count


def part1():
    start, end, path_set = get_data()
    numbered_path = get_order(start, end, path_set)
    print(cheat(2, 100, numbered_path))


def part2():
    start, end, path_set = get_data()
    numbered_path = get_order(start, end, path_set)
    print(cheat(20, 100, numbered_path))


part1()
part2()

from heapq import heappop, heappush
from itertools import product


def get_data(name):
    with open(name, 'r') as file:
        return [tuple(map(int, line.split(','))) for line in file.read().splitlines()]


def is_inside(size, cell):
    return 0 <= cell[0] < size and 0 <= cell[1] < size


def search_path(size, bytes):
    directions = ['^', '>', 'v', '<']
    dx = {'^': 0, '>': 1, 'v': 0, '<': -1}
    dy = {'^': -1, '>': 0, 'v': 1, '<': 0}

    queue = []
    start = (0, 0)
    heappush(queue, (0, start))
    visited = {}

    while queue:
        l, (x, y) = heappop(queue)

        if (x, y) == (size - 1, size - 1):
            return l

        if (x, y) in visited and visited[(x, y)] <= l:
            continue

        visited[(x, y)] = l

        for dir in directions:
            next_cell = (x + dx[dir], y + dy[dir])
            if not is_inside(size, next_cell) or next_cell in bytes:
                continue
            if next_cell not in visited or visited[next_cell] > l + 1:
                heappush(queue, (l + 1, next_cell))

    return False


def part1(size, number_bytes, name):
    bytes = get_data(name)[:number_bytes]
    print(search_path(size, bytes))


def part2(size, name):
    all_bytes = get_data(name)
    up = len(all_bytes)
    down = 0

    work = True

    while work:
        number_bytes = down + (up - down) // 2
        bytes = all_bytes[:number_bytes]

        if not search_path(size, bytes):
            up = number_bytes
            continue

        for i in range(number_bytes, number_bytes + 1):
            byte = all_bytes[i]
            bytes.append(byte)
            if not search_path(size, set(bytes)):
                print(byte)
                work = False
                break
        else:
            down = number_bytes + 1


part1(71, 1024, 'input18.txt')
part2(71, 'input18.txt')



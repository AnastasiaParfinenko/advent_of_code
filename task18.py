from heapq import heappop, heappush
from itertools import product


def get_data(name):
    with open(name, 'r') as file:
        return [tuple(map(int, line.split(','))) for line in file.read().splitlines()]


def search_path(size, bytes):
    grid = list(product(range(size), repeat=2))
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
            if next_cell not in grid or next_cell in bytes:
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

        for i in range(number_bytes, number_bytes + 5):
            byte = all_bytes[i]
            bytes.append(byte)
            if not search_path(size, bytes):
                print(byte)
                work = False
                break
        else:
            down = number_bytes


part1(71, 1024, 'input.txt')
part2(71, 'input.txt')



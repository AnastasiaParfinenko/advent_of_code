from itertools import combinations

class Grid:
    def __init__(self):
        self.size = 0
        self.data = {}

    def get_data(self):
        with open('input8.txt', 'r') as file:
            content = file.read().splitlines()
            self.size = len(content)

            for i, line in enumerate(content, start=1):
                for j, c in enumerate(line, start=1):
                    if c != '.':
                        self.data.setdefault(c, []).append((i, j))


def get_locations(part, size, coords):
    cases = [[2], range(size)]
    locations = set()
    n = len(coords)
    for p1, p2 in combinations(coords, 2):
        for k in cases[part - 1]:
            i = p1[0] + k * (p2[0] - p1[0])
            j = p1[1] + k * (p2[1] - p1[1])
            if 0 < i <= size and 0 < j <= size:
                locations.add((i, j))
            else:
                break

        for k in cases[part - 1]:
            i = p2[0] + k * (p1[0] - p2[0])
            j = p2[1] + k * (p1[1] - p2[1])
            if 0 < i <= size and 0 < j <= size:
                locations.add((i, j))
            else:
                break

    return locations


def part(num):
    grid = Grid()
    grid.get_data()
    locations = set()
    for key in grid.data.keys():
        locations |= get_locations(num, grid.size, grid.data[key])

    print(len(locations))

part(2)
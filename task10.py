class Grid:
    def __init__(self):
        with open('input10.txt', 'r') as file:
            self.data = file.read().splitlines()
            self.size = len(self.data)
            self.nulls = [(i, j) for i in range(self.size) for j in range(self.size) if self.data[i][j] == '0']

    def search_trails(self, path, trails):
        if len(path) == 10:
            trails.append(path)
            return trails

        i, j = path[-1][1]
        for point in ((i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)):
            if not all(0 <= point[i] < self.size for i in range(2)):
                continue

            num = int(self.data[point[0]][point[1]])
            if num == path[-1][0] + 1:
                self.search_trails(path + [(num, point)], trails)

        return trails


def count_uniq_tops(trails):
    return len(set(trail[-1][1] for trail in trails))


def part12():
    grid = Grid()
    list_of_trails = [grid.search_trails([(0, null)], []) for null in grid.nulls]
    uniq_tops = sum(count_uniq_tops(t) for t in list_of_trails)
    diversity_of_trails = sum(len(t) for t in list_of_trails)

    print(uniq_tops)
    print(diversity_of_trails)


part12()
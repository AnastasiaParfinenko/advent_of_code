class Grid:
    def __init__(self):
        with open('input10.txt', 'r') as file:
            self.data = file.read().splitlines()
            self.size = len(self.data)
            self.nulls = [(i, j) for i in range(self.size) for j in range(self.size) if self.data[i][j] == '0']

    def search_trails(self, start, last_value, last_pos, result):
        if last_value == 9:
            result.append( (start, last_pos) )
            return

        i, j = last_pos
        for point in ((i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)):
            if not all(0 <= point[i] < self.size for i in range(2)):
                continue

            num = int(self.data[point[0]][point[1]])
            if num == last_value + 1:
                self.search_trails(start, last_value + 1, point, result)

        return


def part12():
    grid = Grid()
    trails = []
    for null in grid.nulls:
        grid.search_trails(null, 0, null, trails)
    uniq_tops = len(set(trails))
    diversity_of_trails = len(trails)

    print(uniq_tops)
    print(diversity_of_trails)


part12()
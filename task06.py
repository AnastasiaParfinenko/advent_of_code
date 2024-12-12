import time

class Grid:
    def __init__(self):
        self.field = self.get_field()
        self.dir = 'up'
        self.pos = self.get_pos()
        self.path = set()

    @staticmethod
    def get_field():
        with open('input6.txt', 'r') as file:
            return  [list(line.strip('\n')) for line in file]

    def get_pos(self):
        for i in range(len(self.field)):
            for j in range(len(self.field)):
                if self.field[i][j] == '^':
                    return i, j

    def action(self):
        i = self.pos[0]
        j = self.pos[1]

        if self.dir == 'up':
            if i - 1 < 0:
                self.mark(i, j)
                return "I'm free"
            elif self.field[i - 1][j] == '#':
                self.dir = 'right'
            else:
                self.mark(i, j)
                self.pos = (i - 1, j)
        elif self.dir == 'right':
            if j + 1 > len(self.field) - 1:
                self.mark(i, j)
                return "I'm free"
            elif self.field[i][j + 1] == '#':
                self.dir = 'down'
            else:
                self.mark(i, j)
                self.pos = (i, j + 1)
        elif self.dir == 'down':
            if i + 1 > len(self.field) - 1:
                self.mark(i, j)
                return "I'm free"
            elif self.field[i + 1][j] == '#':
                self.dir = 'left'
            else:
                self.mark(i, j)
                self.pos = (i + 1, j)
        elif self.dir == 'left':
            if j - 1 < 0:
                self.mark(i, j)
                return "I'm free"
            elif self.field[i][j - 1] == '#':
                self.dir = 'up'
            else:
                self.mark(i, j)
                self.pos = (i, j - 1)

    def mark(self, i, j):
        self.path.add((self.dir, (i, j)))

    def get_path(self):
        while not self.action():
            pass

        return self.path


def check_cell(grid: Grid):
    while True:
        res = grid.action()
        # for row in grid.field:
        #     print(*row)
        # print()
        if res == "I'm free":
            return False
        if (grid.dir, grid.pos) in grid.path:
            return True


def part1():
    grid = Grid()
    place_for_x = set(pos for dir, pos in grid.get_path())
    ans = len(place_for_x)

    print(ans)


def part2():
    pr_start = time.time()
    grid = Grid()
    start = grid.pos
    place_for_x = set(pos for dir, pos in grid.get_path())
    place_for_x.discard(('up', start))

    res = 0
    for cell in place_for_x:
        grid.pos = start
        grid.dir = 'up'
        grid.path = set()
        grid.field[cell[0]][cell[1]] = '#'
        if check_cell(grid):
            res += 1
        grid.field[cell[0]][cell[1]] = '.'

    print(res)
    pr_end = time.time()
    print(pr_end - pr_start)


# part1()
part2()
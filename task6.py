import copy


class Grid:

    def __init__(self, field, dir):
        self.field = copy.deepcopy(field)
        self.dir = dir
        self.pos = self.get_pos()
        self.path = set()

    def get_pos(self):
        for i in range(len(self.field)):
            for j in range(len(self.field)):
                if self.field[i][j] == '^':
                    return (i, j)

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
        self.field[i][j] = 'X'
        self.path.add((self.dir, (i, j)))


def get_field():
    with open('input.txt', 'r') as file:
        return  [list(line.strip('\n')) for line in file]


def part1():
    grid = Grid(get_field(), 'up')
    while not grid.action():
        pass

    # for line in grid.field:
    #     print(*line)

    print(sum(cell == 'X' for row in grid.field for cell in row))

    return grid.path


def check_cell(grid: Grid, cell):
    cur_grid = Grid(grid.field, 'up')
    cur_grid.field[cell[0]][cell[1]] = '#'
    while True:
        res = cur_grid.action()
        if res == "I'm free":
            return False
        if (cur_grid.dir, cur_grid.pos) in cur_grid.path:
            return True


def part2():
    grid = Grid(get_field(), 'up')
    place_for_x = set(pos for dir, pos in part1())
    place_for_x.discard(('up', grid.pos))

    res = 0
    for cell in place_for_x:
        if check_cell(grid, cell):
            res += 1

    print(res)


part2()
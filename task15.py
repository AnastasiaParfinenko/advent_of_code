class Warehouse:
    width: int
    length: int
    grid: list[list[str]]
    moves: str
    robot: tuple[int, int]

    def get_robot(self):
        for i in range(self.length):
            for j in range(self.width):
                if self.grid[i][j] == '@':
                    return i, j

    def next_p(self, p: tuple, s):
        if s == '^':
            new_p = (p[0] - 1, p[1])
        elif s == '>':
            new_p = (p[0], p[1] + 1)
        elif s == 'v':
            new_p = (p[0] + 1, p[1])
        else:  # s == '<'
            new_p = (p[0], p[1] - 1)
        return new_p

    def move(self):
        for s in self.moves:
            # self.visual()
            path = [self.robot]
            new_p = self.next_p(self.robot, s)
            while self.grid[new_p[0]][new_p[1]] != '.' and self.grid[new_p[0]][new_p[1]] != '#':
                path.append(new_p)
                new_p = self.next_p(new_p, s)

            if self.grid[new_p[0]][new_p[1]] == '#':
                pass
            elif self.grid[new_p[0]][new_p[1]] == '.':
               for p in path[::-1]:
                    self.grid[new_p[0]][new_p[1]] = self.grid[p[0]][p[1]]
                    new_p = p
               self.grid[self.robot[0]][self.robot[1]] = '.'
               self.robot = self.next_p(self.robot, s)

    def visual(self):
        for line in self.grid:
            print(*line, sep='')

    def count_price(self, box):
        price = 0
        for i in range(self.length):
            for j in range(self.width):
                if self.grid[i][j] == box:
                    price += 100 * i + j

        return price

    def double_grid(self):
        new_grid = []
        for line in self.grid:
            new_line = []
            for s in line:
                if s == 'O':
                    new_line += ['[', ']']
                elif s == '@':
                    new_line += ['@', '.']
                else:
                    new_line += [s, s]
            new_grid.append(new_line)
        return new_grid

    def move_l_or_r(self, s):
        path = [self.robot]
        new_p = self.next_p(self.robot, s)
        while self.grid[new_p[0]][new_p[1]] != '.' and self.grid[new_p[0]][new_p[1]] != '#':
            path.append(new_p)
            new_p = self.next_p(new_p, s)

        if self.grid[new_p[0]][new_p[1]] == '#':
            pass
        elif self.grid[new_p[0]][new_p[1]] == '.':
            for p in path[::-1]:
                self.grid[new_p[0]][new_p[1]] = self.grid[p[0]][p[1]]
                new_p = p
            self.grid[self.robot[0]][self.robot[1]] = '.'
            self.robot = self.next_p(self.robot, s)

    @staticmethod
    def sign(s):
        if s == '^':
            n = -1
        elif s == 'v':
            n = 1
        else:
            n = 0
        return  n

    def next_ps(self, ps: list[tuple], s):
        n = self.sign(s)

        new_ps = [(p[0] + n, p[1]) for p in ps if self.grid[p[0]][p[1]] != '.']
        if self.grid[new_ps[-1][0]][new_ps[-1][1]] == '[':
            new_ps += [(new_ps[-1][0], new_ps[-1][1] + 1)]
        if self.grid[new_ps[0][0]][new_ps[0][1]] == ']':
            new_ps = [(new_ps[0][0], new_ps[0][1] - 1)] + new_ps

        return new_ps

    def move_u_or_d(self, s):
        path = [[self.robot]]
        new_ps = self.next_ps([self.robot], s)
        while any(self.grid[p[0]][p[1]] != '.' for p in new_ps) and all(self.grid[p[0]][p[1]] != '#' for p in new_ps):
            path.append(new_ps)
            new_ps = self.next_ps(new_ps, s)

        if any(self.grid[p[0]][p[1]] == '#' for p in new_ps):
            pass
        elif all(self.grid[p[0]][p[1]] == '.' for p in new_ps):
            n = self.sign(s)
            for ps in path[::-1]:
                for p in new_ps:
                    if (p[0] - n,p[1]) in ps:
                        self.grid[p[0]][p[1]] = self.grid[p[0] - n][p[1]]
                    else:
                        self.grid[p[0]][p[1]] = '.'
                new_ps = ps
            self.grid[self.robot[0]][self.robot[1]] = '.'
            self.robot = self.next_p(self.robot, s)
        else:
            assert False, "Программа дошла до этой точки! Упс!"

    def move2(self):
        for s in self.moves:
            self.visual()
            print(s)
            if s in ['^', 'v']:
                self.move_u_or_d(s)
            else:
                self.move_l_or_r(s)


def get_data():
    with open('input_ex.txt', 'r') as file:
        house = Warehouse()
        content = file.read().splitlines()
        house.width = len(content[0])
        house.length = house.width
        house.grid = [list(line) for  line in content[:house.length]]
        house.moves = ''.join(content[house.length + 1:])
        house.robot = house.get_robot()
    return house


def part1():
    house = get_data()
    house.move()
    print(house.count_price('O'))

def part2():
    house = get_data()
    print(house.moves)
    house.grid = house.double_grid()
    house.width = 2 * house.width
    house.robot = house.get_robot()
    house.move2()
    house.visual()
    print(house.count_price('['))


# part1()
part2()
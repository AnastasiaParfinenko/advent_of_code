from collections import namedtuple


Point = namedtuple('Point', ('x', 'y'))


class Claw_Machine:
    def __init__(self):
        self.a = Point(-1, -1)
        self.b = Point(-1, -1)
        self.prize = Point(-1, -1)


def get_coords(file):
    line = file.readline().split()
    i = 2 if line[0] == 'Button' else 1
    x = int(line[i][2:].strip(','))
    y = int(line[i + 1][2:].strip('\n'))
    return Point(x, y)


def get_data():
    with open('input.txt', 'r') as file:
        machines = []
        while True:
            machine = Claw_Machine()
            for attr in ['a', 'b', 'prize']:
                setattr(machine, attr, get_coords(file))
            machines.append(machine)
            if not file.readline():
                break
    return machines


def det(p1: Point, p2: Point):
    return p1.x * p2.y - p1.y * p2.x


def solve_system(m: Claw_Machine):
    assert det(m.a, m.b) != 0, 'НУЛЕВОЙ ОПРЕДЕЛИТЕЛЬ!!!'

    x = det(m.prize, m.b) // det(m.a, m.b)
    y = det(m.a, m.prize) // det(m.a, m.b)
    if x * det(m.a, m.b) == det(m.prize, m.b) and y * det(m.a, m.b) == det(m.a, m.prize):
        return x, y

    return 0, 0


def part1():
    machines = get_data()
    total_price = sum(3 * s[0] + s[1] for m in machines if (s := solve_system(m)))
    print(total_price)


def part2():
    machines = get_data()
    total_price = 0
    for m in machines:
        m.prize = Point(m.prize.x + 10 ** 13, m.prize.y + 10 ** 13)
        s = solve_system(m)
        total_price += 3 * s[0] +  s[1]

    print(total_price)


part1()
part2()

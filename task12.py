from itertools import product


class Area:
    def __init__(self, i, j):
        self.p = 4
        self.s = 1
        self.sides = 4
        self.cells = {(i, j)}


class Grid:
    def __init__(self):
        with open('input12.txt', 'r') as file:
            self.data = file.read().splitlines()
            self.size = len(self.data)

    def get_areas(self):
        areas = []
        for i, j in product(range(self.size), repeat=2):
            up_contact = i > 0 and self.data[i][j] == self.data[i - 1][j]
            right_contact = j > 0 and self.data[i][j] == self.data[i][j - 1]

            if not (up_contact or right_contact):
                area = Area(i, j)
                areas.append(area)
            else:
                up_area, right_area = None, None
                if up_contact:
                    up_cell = (i - 1, j)
                    up_area = next((area for area in areas if up_cell in area.cells))
                if right_contact:
                    right_cell = (i, j - 1)
                    right_area = next((area for area in areas if right_cell in area.cells))

                if up_area == right_area:
                    up_area.cells.add((i, j))
                    up_area.s += 1
                    up_area.p += 0
                    if (i - 1, j + 1) not in up_area.cells:
                        up_area.sides -= 2
                elif right_area and up_area:
                    up_area.cells |= right_area.cells | {(i ,j)}
                    up_area.s += right_area.s + 1
                    up_area.p += right_area.p
                    up_area.sides += right_area.sides
                    areas.remove(right_area)
                    if (i - 1, j + 1) not in up_area.cells:
                        up_area.sides -= 2
                elif right_area:
                    right_area.cells.add((i, j))
                    right_area.s += 1
                    right_area.p += 2
                    if (i - 1, j - 1) in right_area.cells:
                        right_area.sides += 2
                elif up_area:
                    up_area.cells.add((i, j))
                    up_area.s += 1
                    up_area.p += 2
                    if (i - 1, j + 1) in up_area.cells:
                        up_area.sides += 2
                    if (i - 1, j - 1) in up_area.cells:
                        up_area.sides += 2

        return areas


def part12():
    grid = Grid()
    areas = grid.get_areas()
    price = sum(area.p * area.s for area in areas)
    print(price)
    new_price = sum(area.sides * area.s for area in areas)
    print(new_price)


part12()
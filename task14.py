import re


def parse_file_with_findall(file_path):
    p = re.compile(r'(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)')
    tuples_list = []

    with open(file_path, 'r') as file:
        for line in file:
            # Найти все совпадения в строке
            matches = p.findall(line.strip())
            # Добавить каждый найденный кортеж в список, преобразовав строки в числа
            tuples_list.extend([tuple(map(int, match)) for match in matches])

    return tuples_list


def calculate_position_with_wrap(width, height, x_start, y_start, dx, dy, tacts):
    final_x = (x_start + dx * tacts) % width
    final_y = (y_start + dy * tacts) % height
    return final_x, final_y


def after_one_tact(width, height, robot: tuple):
    final_x = (robot[0] + robot[2]) % width
    final_y = (robot[1] + robot[3]) % height
    return final_x, final_y, robot[2], robot[3]


def count_figures_in_quadrants_product(width, height, figures):
    middle_x = width // 2
    middle_y = height // 2

    quadrants = {'Q1': 0, 'Q2': 0, 'Q3': 0, 'Q4': 0}

    for (x, y) in figures:
        if x == middle_x or y == middle_y:
            continue

        if x < middle_x and y < middle_y:
            quadrants['Q1'] += 1
        elif x > middle_x and y < middle_y:
            quadrants['Q2'] += 1
        elif x < middle_x and y > middle_y:
            quadrants['Q3'] += 1
        elif x > middle_x and y > middle_y:
            quadrants['Q4'] += 1

    print(quadrants.values())

    product = quadrants['Q1'] * quadrants['Q2'] * quadrants['Q3'] * quadrants['Q4']
    return product


def pattern(on_grid):
    for j in range(103):
        for i in range(101):
            p = set([(i + k, j) for k in range(7)])
            if p.issubset(on_grid):
                return True

    return False


def print_pic(width, height, figures):
    for i in range(height):
        for j in range(width):
            if (j, i) in figures:
                print('@', end='')
            else:
                print('.', end='')
        print()


def part1():
    file_path = 'input.txt'
    tuples = parse_file_with_findall(file_path)
    width = 101
    height = 103
    # tacts = 100
    # figures = []
    # for robot in tuples:
    #     figures.append(calculate_position_with_wrap(width, height, robot[0], robot[1], robot[2], robot[3], tacts))
    # print(count_figures_in_quadrants_product(width, height, figures))
    robots = parse_file_with_findall(file_path)
    for _ in range(100):
        robots = [after_one_tact(width, height, robot) for robot in robots]
    on_grid = [(robot[0], robot[1]) for robot in robots]
    print(count_figures_in_quadrants_product(width, height, on_grid))

def part2():
    file_path = 'input.txt'
    robots = parse_file_with_findall(file_path)
    w = 101
    h = 103
    tacts = 0
    with open('output.txt', 'w') as file:
        while True:
            tacts += 1
            # print(tacts)
            robots = [after_one_tact(w, h, robot) for robot in robots]
            on_grid = set([(robot[0], robot[1]) for robot in robots])
            # if len(on_grid & cristmas_tree3(w, h)) > 350:
            #     print(len(on_grid & cristmas_tree3(w, h)))
            #     print(tacts)
            #     print_pic(w, h, on_grid & cristmas_tree3(w, h))
            # file.write(str(tacts) + '\n')
            # for i in range(h):
            #     for j in range(w):
            #         if (j, i) in on_grid:
            #             file.write('@')
            #         else:
            #             file.write('.')
            #     file.write('\n')
            if pattern(on_grid):
                print(tacts)
                print_pic(w, h, on_grid)
            if tacts % 10000 == 0:
                break


# print_pic(101, 103, cristmas_tree3(101, 103))
part2()
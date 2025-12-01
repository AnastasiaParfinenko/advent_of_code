def get_date():
    with open('input01_1.txt', 'r', encoding='utf-8') as file:
        actions = [(1 - 2 * (line[0] == 'L')) * int(line[1:]) for line in file]
    return actions


def part1():
    actions = get_date()
    arrow = 50

    count = 0
    for action in actions:
        arrow = (arrow + action) % 100
        if arrow == 0:
            count += 1

    print(count)


def sign(number):
    return (number > 0) - (number < 0)


def part2():
    actions = get_date()
    arrow = 50

    count = 0
    for action in actions:
        for _ in range(abs(action)):
            arrow = (arrow + sign(action)) % 100
            if arrow == 0:
                count += 1

    print(count)


part1()
# 1007
part2()
# 5820
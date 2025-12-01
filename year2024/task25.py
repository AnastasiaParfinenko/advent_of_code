def get_data():
    with open('input25.txt', 'r') as file:
        keys = []
        locks = []
        while True:
            line1 = file.readline()
            if not line1:
                break

            detail = [0] * 5

            for _ in range(5):
                for i, c in enumerate(file.readline().strip()):
                    if c == '#':
                        detail[i] += 1

            line7 = file.readline().strip()
            if line7 == '.....':
                locks.append(detail)
            elif line7 == '#####':
                keys.append(detail)
            else:
                assert False, 'Alarmstufe rot!'

            file.readline()

        return locks, keys


def part1():
    locks, keys = get_data()
    res = 0
    for key in keys:
        for lock in locks:
            if all(key[i] + lock[i] <= 5 for i in range(5)):
                res += 1

    print(res)


part1()


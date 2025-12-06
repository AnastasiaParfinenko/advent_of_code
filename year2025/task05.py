def get_data(name):
    with open(name, 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file]

    sep = lines.index('')
    fresh_products = [list(map(int, s.split('-'))) for s in lines[:sep]]
    given_products = [int(s) for s in lines[sep + 1:]]

    return fresh_products, given_products


def part1():
    fresh_products, given_products = get_data('input05_1.txt')

    res = 0
    for product in given_products:
        for a, b in fresh_products:
            if a <= product <= b:
                res += 1
                break

    return res


def sort_and_merge(intervals_list):
    intervals_list.sort()
    new_list = [intervals_list[0]]

    for a, b in intervals_list[1:]:
        if a <= new_list[-1][1] + 1:
            new_list[-1][1] = max(b, new_list[-1][1])
        else:
            new_list.append([a, b])

    return new_list


def part2():
    fresh_products, given_products = get_data('input05_1.txt')
    fresh_products = sort_and_merge(fresh_products)
    return sum(b - a + 1 for (a, b) in fresh_products)


a1 = part1()
print(a1)
assert a1 == 720, a1

a2 = part2()
print(a2)
assert a2 == 357608232770687, a2

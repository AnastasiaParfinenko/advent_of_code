def get_data():
    with open('input5.txt', 'r') as file:
        rules = []
        for line in file:
            if line == '\n':
                break
            else:
                rules.append([int(n) for n in line.split('|')])
        updates = []
        for line in file:
            update = list(map(int, line.split(',')))
            updates.append(update)

    return rules, updates


def check(rules, update):
    for i in range(len(update)):
        for rule in rules:
            if rule[1] == update[i] and rule[0] in update[i + 1:]:
                return False

    return True


def part1():
    res = 0
    rules, updates = get_data()
    for update in updates:
        if check(rules, update):
            res += update[len(update) // 2]
    print(res)


def change_update(rules, update):
    l = len(update)
    i = 0
    while i < l:
        for j in range(i + 1, l):
            rule = [update[j],update[i]]
            if rule in rules:
                del update[j]
                update.insert(i, rule[0])
                break
        else:
            i += 1

    return update


def part2():
    res = 0
    rules, updates = get_data()

    for update in updates:
        if not check(rules, update):
            res += change_update(rules, update)[len(update) // 2]

    print(res)


part1()
part2()

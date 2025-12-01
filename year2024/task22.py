from functools import lru_cache
import cProfile

def mix(value, number):
    return value ^ number


def prune(number):
    return number % 16777216


@lru_cache(maxsize=None)
def it(number):
    step1 = prune(mix(number * 64, number))
    step2 = prune(mix(step1 // 32, step1))
    step3 = prune(mix(step2 * 2048, step2))

    return step3


def it2000(number):
    for _ in range(2000):
        number = it(number)
    return number


def get_data(number):
    changes = []
    rest = number % 10
    prices = [rest]
    for _ in range(2000):
        number = it(number)
        changes.append(number % 10 - rest)
        rest = number % 10
        prices.append(rest)

    return prices, changes


def get_patterns(new_data):
    patterns = set()
    for data in new_data:
        patterns.update(data.keys())
    return patterns


def change_data(data):
    prices, changes = data
    new_data = {}
    for i in range(len(changes) - 4):
        if prices[i + 4] != 0:
            pattern = tuple(changes[i: i + 4])
            if pattern not in new_data:
                new_data[pattern] = prices[i + 4]

    return new_data


def part1():
    with open('input22.txt', 'r') as file:
        res1 = sum(it2000(int(line)) for line in file)
        print(res1)


def part2():
    with open('input22.txt', 'r') as file:
        all_data = [get_data(int(line)) for line in file]
    new_data = [change_data(data) for data in all_data]
    patterns = get_patterns(new_data)

    max_sum = 0
    for pattern in patterns:
        new_sum = sum(data[pattern] for data in new_data if pattern in data)
        max_sum = max(max_sum, new_sum)
    print(max_sum)


# part1()
# part2()
cProfile.run('part2()')
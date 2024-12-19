from functools import lru_cache


def get_data():
    with open('input.txt', 'r') as file:
        towels = tuple(file.readline().strip().split(', '))
        file.readline()
        designs = [line.strip() for line in file]

    return towels, designs


@lru_cache(None)
def check(towels, design: str):
    if not design:
        return True

    for t in towels:
        if design.startswith(t):
            if check(towels, design[len(t):]):
                return True

    return False

@lru_cache(None)
def count_ways(towels, design: str):
    if not design:
        return 1

    different_ways = 0

    for t in towels:
        if design.startswith(t):
            different_ways += count_ways(towels, design[len(t):])

    return different_ways


def part12():
    towels, designs = get_data()
    ans1 = sum(check(towels, design) for design in designs)
    ans2 = sum(count_ways(towels, design) for design in designs)
    print(ans1, ans2, sep='\n')


part12()
from functools import lru_cache


def get_data():
    with open('input.txt', 'r') as file:
        towels = tuple(file.readline().strip('\n').split(', '))
        file.readline()
        designs = [line.strip('\n') for line in file]

    return towels, designs


@lru_cache(None)
def check(towels, design: str):
    if not design:
        return 1

    different_ways = 0

    for t in towels:
        if design.startswith(t):
            different_ways += check(towels, design[len(t):])

    return different_ways


def part12():
    towels, designs = get_data()
    ans1 = sum(1 for design in designs if check(towels, design))
    ans2 = sum(check(towels, design) for design in designs)
    print(ans1, ans2, sep='\n')


part12()
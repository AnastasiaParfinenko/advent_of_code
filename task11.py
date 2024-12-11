from functools import lru_cache


def get_stones():
    with open('input.txt', 'r') as file:
        stones = file.read().split()
        return stones


def one_blink(stones: list):
    new_stones = []
    for stone in stones:
        if len(stone) % 2 == 0:
            middle = len(stone) // 2
            new_stones.append(stone[:middle])
            new_stones.append(str(int(stone[middle:])))
        elif stone == '0':
            new_stones.append('1')
        else:
            new_stones.append(str(int(stone) * 2024))

    return  new_stones

@lru_cache(None)
def count_stones(stone, time, cur_time):
    if not stone:
        return 0

    if cur_time == time:
        return 1

    if len(stone) % 2 == 0:
        middle = len(stone) // 2
        stone1 = stone[:middle]
        stone2 = str(int(stone[middle:]))
    elif stone == '0':
        stone1 = '1'
        stone2 = None
    else:
        stone1 = str(int(stone) * 2024)
        stone2 = None

    return count_stones(stone1, time, cur_time + 1) + count_stones(stone2, time, cur_time + 1)


def part1():
    stones = get_stones()
    times = 25
    for time in range(times):
        stones = one_blink(stones)
    print(len(stones))


def part2():
    stones = get_stones()
    res = 0
    for stone in stones:
        res += count_stones(stone,75,0)
    print(res)


part1()
part2()
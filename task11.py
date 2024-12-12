from functools import lru_cache


def get_stones():
    with open('input11.txt', 'r') as file:
        return file.read().split()


@lru_cache(None)
def count_stones(stone, total_blink, cur_blink):
    if not stone:
        return 0

    if cur_blink == total_blink:
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

    return count_stones(stone1, total_blink, cur_blink + 1) + count_stones(stone2, total_blink, cur_blink + 1)


def part12():
    stones = get_stones()
    for total_blink in [25, 75]:
        print(sum(count_stones(stone, total_blink,0) for stone in stones))


part12()

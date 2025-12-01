import itertools
from functools import lru_cache


def check_path(pad, s, path):
    ban = (0, 0) if '0' in pad else (0, 1)
    x, y = pad[s]
    dx = {'^': 0, '>': 1, 'v': 0, '<': -1}
    dy = {'^': 1, '>': 0, 'v': -1, '<': 0}
    for a in path:
        x += dx[a]
        y += dy[a]
        if (x, y) == ban:
            return False

    return True


def make_path(pad, s, e):
    dx, dy = pad[e][0] - pad[s][0], pad[e][1] - pad[s][1]
    l = abs(dx) + abs(dy)
    combinations = itertools.combinations(range(l), abs(dx))
    paths = []
    for combo in combinations:
        path = ['^'] * l if dy > 0 else ['v'] * l
        for p in combo:
            path[p] = '<' if dx < 0 else '>'
        if check_path(pad, s, path):
            paths.append(''.join(path) + 'A')

    return tuple(paths)


# '029A' -> (('<A',), ('^A',), ('>^^A', '^>^A', '^^>A'), ('vvvA',))
def num_step(code):
    code = 'A' + code
    sequences = []
    for i in range(len(code) - 1):
        sequences.append(make_path(NUMERIC_PAD, code[i], code[i + 1]))

    return tuple(sequences)


# 'A^<A' -> (('<A',), ('v<A',), ('>>^A', '>^>A'))
@lru_cache(None)
def dir_step(seq):
    seq = 'A' + seq
    sequences = []
    for i in range(len(seq) - 1):
        sequences.append(make_path(DIR_PAD, seq[i], seq[i + 1]))

    return tuple(sequences)


NUMERIC_PAD = {
    '0': (1, 0),
    'A': (2, 0),
    '1': (0, 1),
    '2': (1, 1),
    '3': (2, 1),
    '4': (0, 2),
    '5': (1, 2),
    '6': (2, 2),
    '7': (0, 3),
    '8': (1, 3),
    '9': (2, 3),
}

DIR_PAD = {
    '<': (0, 0),
    'v': (1, 0),
    '>': (2, 0),
    '^': (1, 1),
    'A': (2, 1),
}


@lru_cache(None)
def it(seq: str, pads: int):
    if pads == 0:
        return len(seq)

    next_sequences = dir_step(seq)
    pads -= 1

    res = 0
    for sequences in next_sequences:
        etwas = min(it(seq, pads) for seq in sequences)
        res += etwas

    return res


def part12(name, pads):
    with open(name, 'r') as file:
        codes = [line.strip() for line in file]

    res = 0
    for code in codes:
        etwas = 0
        step1 = num_step(code)
        for sequences in step1:
            noch_etwas = min(it(seq, pads) for seq in sequences)
            etwas += noch_etwas
        res += etwas * int(code[:-1])

    print(res)


part12('input21.txt', 2)
# 213536
part12('input21.txt', 25)
# 258369757013802
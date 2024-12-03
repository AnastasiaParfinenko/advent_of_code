from os import write
import re


def check(line, cur_index):
    c1, c2 = False, False
    k = line.find(',', cur_index)
    if k == -1:
        return None
    if k - cur_index <= 7 and line[cur_index + 4: k].isdigit():
        num1 = int(line[cur_index + 4: k])
        c1 = True
    s = line.find(')', cur_index)
    if s == -1:
        return None
    if s - k <= 4 and line[k + 1: s].isdigit():
        num2 = int(line[k + 1: s])
        c2 = True

    if c1 and c2:
        return num1 * num2
    else:
        return None

def part1():
    res = 0

    with open('new_input.txt', 'r', encoding='utf-8') as file:
        for line in file:
            cur_index = -4
            while True:
                cur_index = line.find('mul(', cur_index + 4)
                if cur_index == -1:
                    break
                if check(line, cur_index):
                    res += check(line, cur_index)

    return res


def part2():
    with open('input.txt', 'r', encoding='utf-8') as file:
        s = file.read()
        new_s = ''
        work = True
        for i in range(len(s)):
            if work:
                new_s += s[i]
                if s.startswith("don't()", i):
                    work = False
            else:
                if s.startswith('do()', i):
                    work = True

    with open('new_input.txt', 'w', encoding='utf-8') as file:
        file.write(new_s)



new_part1()

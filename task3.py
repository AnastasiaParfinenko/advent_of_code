import re


def  part1():
    with open('new_input.txt', 'r', encoding='utf-8') as file:
        s = file.read()
        pattern = r"mul\(([0-9]{1,3}),([0-9]{1,3})\)"
        all_mul = re.findall(pattern, s)
        print(sum(int(mul[0]) * int(mul[1]) for mul in all_mul))


def part2():
    with open('input3.txt', 'r', encoding='utf-8') as file:
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


part2()
part1()

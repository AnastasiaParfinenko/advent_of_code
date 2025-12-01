list1 = []
list2 = []

with open('input.txt', 'r', encoding='utf-8') as file:
    for line in file:
        a, b = line.split()
        list1.append(int(a))
        list2.append(int(b))

def part1():
    list1.sort()
    list2.sort()

    return sum(abs(list1[i] - list2[i]) for i in range(len(list1)))

def part2():
    return sum(list1[i]*list2.count(list1[i]) for i in range(len(list1)))

print(part2())
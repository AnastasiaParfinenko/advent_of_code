from numpy import sign

task_list = []

with open('input2.txt', 'r', encoding='utf-8') as file:
    for line in file:
        task_list.append([int(i) for i in line.split()])


def check(report):
    s = sign(report[1] - report[0])
    if s == 0:
        return False
    elif s > 0:
        for i in range(1, len(report)):
            if (report[i] - report[i - 1]) > 3 or (report[i] - report[i - 1]) < 1:
                return False
        else:
            return True
    elif s < 0:
        for i in range(1, len(report)):
            if (report[i - 1] - report[i]) > 3 or (report[i - 1] - report[i]) < 1:
                return False
        else:
            return True


def part1():
    count = 0
    for report in task_list:
        if check(report):
            count += 1

    return count

def part2():
    count = 0
    for report in task_list:
        if check(report):
            count += 1
            continue
        else:
            for i in range(len(report)):
                copy_report = report[:]
                del copy_report[i]
                assert copy_report != report
                if check(copy_report):
                    count += 1
                    break

    return count


print(part2())
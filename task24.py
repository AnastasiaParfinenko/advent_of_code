def get_data():
    with open('input24.txt', 'r') as file:
        xy = {}
        for line in file:
            if line == '\n':
                break
            xy[line[:3]] = int(line[-2])
        new_variables = {}
        for line in file:
            line = line.strip().split()
            new_variables[line[4]] = (line[2], line[0], line[1])

    return xy, new_variables


def get_z(known_values, unknown_variables, var):
    if var in known_values:
        return known_values[var]

    term = unknown_variables[var]
    a = get_z(known_values, unknown_variables, term[0])
    b = get_z(known_values, unknown_variables, term[1])
    op = term [2]

    if op == 'AND':
        new_value = a and b
    elif op == 'OR':
        new_value = a or b
    else:
        new_value = a ^ b

    known_values[var] = new_value
    return new_value


def part1():
    xy, new_variables = get_data()
    for var in new_variables:
        get_z(xy, new_variables, var)

    z = {}
    for var in xy:
        if var.startswith('z'):
            z[var] = xy[var]

    res_z = ''.join(str(z[key]) for key in sorted(z.keys(), reverse=True))

    print(int(res_z, 2))


def part2():
    xy, new_variables = get_data()

    x, y = {}, {}
    for var in xy:
        if var.startswith('x'):
            x[var] = xy[var]
        if var.startswith('y'):
            y[var] = xy[var]

    res_x = ''.join(str(x[key]) for key in sorted(x.keys(), reverse=True))
    res_y = ''.join(str(y[key]) for key in sorted(y.keys(), reverse=True))


    new_variables['z05'], new_variables['bpf'] = new_variables['bpf'], new_variables['z05']
    new_variables['z11'], new_variables['hcc'] = new_variables['hcc'], new_variables['z11']
    new_variables['z35'], new_variables['fdw'] = new_variables['fdw'], new_variables['z35']
    new_variables['hqc'], new_variables['qcw'] = new_variables['qcw'], new_variables['hqc']

    task_list = ['hqc', 'qcw', 'z05', 'z11', 'z35', 'bpf', 'hcc', 'fdw']
    print(','.join(sorted(task_list)))

    for var in new_variables:
        get_z(xy, new_variables, var)

    z = {}
    for var in xy:
        if var.startswith('z'):
            z[var] = xy[var]

    res_z = ''.join(str(z[key]) for key in sorted(z.keys(), reverse=True))
    print(int(res_z, 2) == int(res_x, 2) + int(res_y, 2))
    print()

    for i in range(0, len(z)):
        if i < 10:
            var = 'z0' + str(i)
        else:
            var = 'z' + str(i)
        print(var)
        print(new_variables[var])
        var1, var2, _ = new_variables[var]
        print(new_variables[var1] if var1 in new_variables else xy[var1])
        print(new_variables[var2] if var2 in new_variables else xy[var2])
        print()

part1()
part2()
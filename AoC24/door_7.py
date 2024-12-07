import itertools

def part1(ergs, values):
    count = 0
    for erg, vals in zip(ergs, values):
        #print(vals)
        print(erg)
        num_ops = len(vals) - 1
        for op in itertools.product(["+", "*", "||"], repeat=num_ops):
            s = 0
            for i in range(len(vals)):
                if i + 1 == len(vals):
                    continue

                if i == 0:
                    s += int(eval(str(vals[i]) + op[i] + str(vals[i + 1])))
                else:
                    s = int(eval(str(s) + op[i] + str(vals[i + 1])))
            if erg == s:
                count += s
                break
    return count

def part2(puzzle):
    pass

with open("../inputs.txt") as f:
    puzzle = f.read().splitlines()
    erg = [int(line.split(":")[0]) for line in puzzle]

    values = []
    for line in puzzle:
        #print(line.split(":")[1])
        _values = []
        for val in line.split(":")[1].lstrip().split(" "):
            #print(val)
            _values.append(int(val))
        values.append(_values)
#print(values)
print("Part 1: ", part1(erg, values))
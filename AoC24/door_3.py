import re
import copy

def part1(puzzle, sum):
    # find all matches of mul(X,Y)
    m = re.findall(r"mul\((\d+),(\d+)\)", puzzle)
    #print(m)
    for mul in m:
        sum += int(mul[0]) * int(mul[1])
    return sum

def part2(puzzle):
    # find all do() matches
    # Find all matches and their positions
    dos = [(match.start(), match.group()) for match in re.finditer("do\(\)", puzzle)]
    donts = [(match.start(), match.group()) for match in re.finditer("don't\(\)", puzzle)]

    # sort by their starting char position
    merged = sorted(dos + donts, key=lambda x: x[0])

    # iterate over the indexes
    modified_puzzle = re.sub(r"(do\(\)|don't\(\))", r"\n", puzzle)

    # depending on the beginning I can/can't multiply each mul() in the current line
    multiply_first = True
    sum = 0
    for i, line in enumerate(modified_puzzle.split("\n"), -1):
        if multiply_first:
            # first line -> can multiply
            sum = part1(line, sum)
            multiply_first = False
            continue
        instr = merged[i][1]
        if instr == "do()":
            sum = part1(line, sum)
        elif instr == "don't()":
            continue
    return sum

with open("../inputs.txt") as f:
    puzzle = f.read().replace("\n", "")
    print(puzzle)

sum = 0
sum = part1(puzzle, sum)
print(sum)

sum = part2(puzzle)
print(sum)
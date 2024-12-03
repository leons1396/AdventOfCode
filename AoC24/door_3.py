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
    muls = re.findall(r"mul\((\d+),(\d+)\)", puzzle)
    # find all do() matches
    #dos = re.findall("do\(\)", puzzle)
    # Find all matches and their positions
    dos = [(match.start(), match.group()) for match in re.finditer("do\(\)", puzzle)]
    donts = [(match.start(), match.group()) for match in re.finditer("don't\(\)", puzzle)]
    print("Donts:", donts)
    print("Dos:", dos)

    # find all matches of mul(X,Y) and their indexes in the string
    #muls = [(mul, puzzle.index(f"mul({mul[0]},{mul[1]}")) for mul in muls]
    #print(muls)    # merge do() and dont() and sort them by their starting char index in the string

    print(dos + donts)
    merged = sorted(dos + donts, key=lambda x: x[0])
    print(merged)
    # iterate over the indexes
    modified_puzzle = re.sub(r"(do\(\)|don't\(\))", r"\n", puzzle)
    # save the new string in inputs2.txt
    with open("../inputs2.txt", "w") as f:
        f.write(modified_puzzle)
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
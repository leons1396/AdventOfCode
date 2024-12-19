from functools import lru_cache
import re

with open("../inputs.txt") as f:
    puzzle = f.read().splitlines()
    towels = puzzle[0].replace(" ", "").split(",")
    designs = puzzle[2:]
print(puzzle)
print(towels)
print(designs)


def part1(designs, towels):
    count = 0
    for design in designs:
        possible_towels = []
        for towel in towels:
            if towel in design:
                possible_towels.append(towel)

        # remove duplicates
        list(set(possible_towels))

        regex = re.compile(r"^(" + "|".join(possible_towels) + r")*$")
        if regex.fullmatch(design):  #
            count += 1
    return count

print(part1(designs, towels))


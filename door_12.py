# TODO Part 2
import itertools


def create_combinations(records, values):
    records = ["#." if c == "?" else c for c in records]
    return sum(
        count_matches(combination, values)
        for combination in itertools.product(*records)
    )


def count_matches(combi, nums):
    return nums == [
        sum(1 for _ in grouper)
        for key, grouper in itertools.groupby(combi)
        if key == "#"
    ]


with open("puzzle.txt") as file:
    puzzle = file.readlines()

print(puzzle)
arrangements = 0
for line in puzzle:
    records, values = line.split(" ")
    # print(records)
    # print(values)

    extend_records = (records + "?") * 3
    extend_records = extend_records[:-1]

    values = [int(x) for _ in range(3) for x in values.split(",")]
    print(values)
    print(extend_records)
    arrangements += create_combinations(extend_records, values)
    break

print("arrangements: ", arrangements)

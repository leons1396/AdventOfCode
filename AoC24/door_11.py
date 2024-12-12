import copy

def part1(puzzle):
    for i in range(1, 26):
        temp = []
        print(f"Blink {i}")
        for stone in puzzle:
            if stone == "0":
                temp.append("1")
            # even number of digits
            elif len(stone) % 2 == 0:
                left_digits = stone[:(len(stone) // 2)]
                right_digits = str(int(stone[(len(stone) // 2):]))
                temp.append(left_digits)
                temp.append(right_digits)
            else:
                temp.append(str(int(stone) * 2024))
        puzzle = copy.deepcopy(temp)
    return len(puzzle)

# recursive solution
# help from https://www.youtube.com/watch?v=EOAFa8j-GVQ
cache = {}
def part2(stone, steps):
    if steps == 0:
        return 1
    if (stone, steps) not in cache:
        if stone == "0":
            cache[(stone, steps)] = part2("1", steps - 1)
            result = part2("1", steps - 1)
        elif len(stone) % 2 == 0:
            result = 0
            left_digits = stone[:(len(stone) // 2)]
            right_digits = str(int(stone[(len(stone) // 2):]))
            result += part2(left_digits, steps - 1)
            result += part2(right_digits, steps - 1)
        else:
            result = part2(str(int(stone) * 2024), steps - 1)
        cache[(stone, steps)] = result
    return cache[(stone, steps)]


with open("../inputs.txt") as f:
    puzzle = f.read().split(" ")

#print("erg: ", part1(puzzle))

erg = 0
for stone in puzzle:
    print("####### init stone: ", stone)
    erg += part2(stone, 5)
print("erg: ", erg)
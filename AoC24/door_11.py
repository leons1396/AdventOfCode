import copy

with open("../inputs.txt") as f:
    puzzle = f.read().split(" ")

print(puzzle)
for i in range(1, 76):
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
    #print(f"Blink {i}: {puzzle}")
print("erg: ", len(puzzle))
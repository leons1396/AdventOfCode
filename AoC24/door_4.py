import re

def match(line, count):
    # find XMAS and SAMX in horizontal lines
    m1 = re.findall(r"XMAS", line)
    m2 = re.findall(r"SAMX", line)
    count += len(m1 + m2)
    return count

def part1(puzzle):
    count = 0
    for i, line in enumerate(lines, 1):
        count = match(line, count)
    print("Count horizontal: ", count)
    # find in vertical lines
    # iterate over each character in one line
    for c in range(len(puzzle[0])):
        # iterate over lines
        new_line = "".join([puzzle[l][c] for l in range(len(puzzle))])
        count = match(new_line, count)
    #print("Count vertical: ", count)

    # find in diagonal lines upper right triangle from right to left
    # for second iteration just reverse the charachter in each line
    print("UPPER TRIANGLE WITH MAIN DIAGONAL\n")
    for _ in range(2):
        # find in diagonal lines upper right triangle from left to right
        if _ == 1:
            print("######## REVERSED PUZZLE ########")
            puzzle = ["".join(list(reversed(line))) for line in puzzle]

        for c in range(len(puzzle[0])):
            temp_line = []
            for l in range(len(puzzle)):
                if c+l < len(puzzle[0]):
                    temp_line.append(puzzle[l][c+l])
            new_line = "".join(temp_line)
            print(new_line)
            count = match(new_line, count)

        print("")
        print("LOWER TRIANGLE WITHOUT MAIN DIAGONAL\n")
        # find in diagonal lines lower triangle from left to right
        for c in range(len(puzzle[0]) - 1):
            temp_line = []
            for char, l in enumerate(range(1+c, len(puzzle))):
                temp_line.append(puzzle[l][char])
            new_line = "".join(temp_line)
            print(new_line)
            count = match(new_line, count)

    return count

def apply_mask(l1, l2, l3) -> bool:
    word_left_diagonal = l1[0] + l2[1] + l3[2]
    word_right_diagonal = l1[2] + l2[1] + l3[0]
    if word_left_diagonal in ["SAM", "MAS"] and word_right_diagonal in ["SAM", "MAS"]:
        return True
    return False

def part2(puzzle):
    count = 0
    # create a 3x3 mask
    # iterate over lines
    for end_line, start_line in enumerate(range(len(puzzle)), 3):
        if end_line == len(puzzle)+1:
            break
        slice = puzzle[start_line:end_line]

        # iterate over each character in one line
        for end_c, start_c in enumerate(range(len(puzzle[0])), 3):
            if end_c == len(puzzle[0])+1:
                break
            l1 = slice[0][start_c:end_c]
            l2 = slice[1][start_c:end_c]
            l3 = slice[2][start_c:end_c]
            if apply_mask(l1, l2, l3):
                count += 1
    return count

with open("../inputs.txt") as f:
    lines = f.read().splitlines()
    print(lines)

#print("length", len(lines))
#count = part1(lines)
#print("Count: ", count)

count = part2(lines)
print(count)
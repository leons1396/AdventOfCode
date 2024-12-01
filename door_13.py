def vertical_sym(len_line, size_puzzle, pattern_map):
    all_vertical_lines = {}
    idxs_vert_line = []
    for i, col in enumerate(range(1, len_line + 1), 1):
        # reached end of line
        if col == len_line:
            all_vertical_lines[col] = vert_line_next
            break

        vert_line = []
        vert_line_next = []
        for row in range(1, size_puzzle + 1):
            vert_line.append(pattern_map[col + (row - 1) * len_line])
            vert_line_next.append(pattern_map[(col + 1) + (row - 1) * len_line])

        # print("vert_line", vert_line)
        # print("vert_line_next", vert_line_next)
        all_vertical_lines[col] = vert_line
        # print("all_vertical_lines", all_vertical_lines)
        if vert_line == vert_line_next:
            print("vertical symmetry found")
            # print("col", col)
            idxs_vert_line.append(col)

    # sym line is at the border
    sum_block = 0
    for i_vert_line in idxs_vert_line:
        is_mirror = True
        if i_vert_line == 1 or i_vert_line == len_line:
            sum_block += i_vert_line
            continue

        # print("all_vertical_lines", all_vertical_lines)
        # only if there is a vertical sym line
        if i_vert_line > 0:  # TODO I think this if is not necessary any more
            # check if it is a real mirror
            print("i_vert_line", i_vert_line)
            for i, _ in enumerate(range(len_line - (i_vert_line + 1)), 1):
                if i_vert_line - i < 1:
                    continue

                if (
                    all_vertical_lines[i_vert_line - i]
                    != all_vertical_lines[i_vert_line + i + 1]
                ):
                    print("#### not a mirror")
                    sum_block += 0
                    is_mirror = False
                    break

            print("return i_vert_line", i_vert_line)
            if is_mirror:
                sum_block += i_vert_line
        else:
            sum_block += 0
    return sum_block


def horizontal_sym(len_line, size_puzzle, pattern_map):
    all_hor_lines = {}
    idxs_hor_line = []
    for i, row in enumerate(range(1, size_puzzle + 1), 1):
        # reached end of line
        if row == size_puzzle:
            all_hor_lines[row] = hor_line_next
            break

        hor_line = []
        hor_line_next = []
        for col in range(1, len_line + 1):
            hor_line.append(pattern_map[col + (row - 1) * len_line])
            hor_line_next.append(pattern_map[col + row * len_line])

        # print("hor_line", hor_line)
        # print("hor_line_next", hor_line_next)
        all_hor_lines[row] = hor_line
        # print("all_hor_lines", all_hor_lines)
        if hor_line == hor_line_next:
            # BUG It is possible there are more than one horizontal symmetry
            print("horizontal symmetry found")
            # print("row", row)
            idxs_hor_line.append(row)
    # print("all_hor_lines", all_hor_lines)

    # sym line is at the border
    sum_block = 0
    for i_hor_line in idxs_hor_line:
        is_mirror = True
        if i_hor_line == 1 or i_hor_line == size_puzzle:
            sum_block += i_hor_line * 100
            continue

        # only if there is a horizontal sym line
        if i_hor_line > 0:
            # check if it is a real mirror
            for i, _ in enumerate(range(size_puzzle - (i_hor_line + 1)), 1):
                if i_hor_line - i < 1:
                    continue

                if all_hor_lines[i_hor_line - i] != all_hor_lines[i_hor_line + i + 1]:
                    print("#### not a mirror")
                    sum_block += 0
                    is_mirror = False
                    break
            if is_mirror:
                sum_block += i_hor_line * 100
        else:
            sum_block += 0

    return sum_block


with open("puzzle.txt") as file:
    puzzle = file.read().splitlines()

# print(puzzle)

s = 0
ash_rocks = []
sublist = []
for line in puzzle:
    if line == "":
        ash_rocks.append(sublist)
        sublist = []
    else:
        sublist.append(line)

if sublist:
    ash_rocks.append(sublist)
print(ash_rocks)

for block in ash_rocks:
    len_line = len(block[0])
    # print("len_line", len_line)
    pattern_map = {idx: tile for idx, tile in enumerate("".join(block), 1)}
    # print("pattern map", pattern_map)

    s += vertical_sym(len_line, len(block), pattern_map)
    s += horizontal_sym(len_line, len(block), pattern_map)

print("Sum :", s)

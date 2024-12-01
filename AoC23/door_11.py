# number of possilbe pairs: (n^2 - n) / 2

with open('../puzzle_inputs/puzzle_input.txt') as f:
    puzzle = f.read().splitlines()

#print(puzzle)
factor = 1000
puzzle_exp_rows = []
count_galaxy = 0
galaxy_at_col = [i for i in range(1, len(puzzle[0])+1)]
#print(galaxy_at_col)
matches_col = []
for line in puzzle:
    if '#' in line:
        puzzle_exp_rows.append(line)
        count_galaxy += line.count('#')
        for pos, char in enumerate(line, 1):
            if char == '#':
                matches_col.append(pos)
    else:
        # add 10 rows only containing '.'
        for _ in range(factor):
            puzzle_exp_rows.append(line)

#print(puzzle_exp_rows)
print("count galaxy: ", count_galaxy)
print("matches_col: ", matches_col)

# find the columns with no galaxy. Starting Index=1
empty_cols = [i for i in range(1, len(puzzle[0]) + 1) if i not in matches_col]
print("empty_cols: ", empty_cols)
print("lenght expand rows", len(puzzle_exp_rows))
#expand the columns
puzzle_exp_cols = []
for line in puzzle_exp_rows:
    for i, empty_col in enumerate(empty_cols):
        line = line[:empty_col+(i*(factor-1))-1] + ('.' * factor) + line[empty_col+(i*(factor-1)):]
    puzzle_exp_cols.append(line)
print("expand done")
#print("expanded cols: ", puzzle_exp_cols)
#print("len index 0: ", len(puzzle_exp_cols[0]))
#print("len index 0: ", len(puzzle_exp_cols[3]))
# determine the position of the galaxy
len_line = len(puzzle_exp_cols[0])
grid = []
for idx, line in enumerate(puzzle_exp_cols, 1):
    if '#' in line:
        for i, obersavtion in enumerate(line, 1):
            if obersavtion == '.':
                continue
            elif obersavtion == '#':
                row, col = divmod(i, len_line)
                if col == 0:
                    grid.append((idx, len_line))
                else:
                    grid.append((idx, col))
print(grid)
print("lenght grid", len(grid))
# vector calculation for each pair of galxies
# filter method and then sum(list from filter)
number_of_pairs = (count_galaxy**2 - count_galaxy) / 2
d = 0
while len(grid) > 0:
    for i in range(1, count_galaxy):
        x = abs(grid[0][0] - grid[i][0])
        y = abs(grid[0][1] - grid[i][1])
        d += x + y
    _ = grid.pop(0)
    count_galaxy -= 1
print("distance", d)
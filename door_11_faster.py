# number of possilbe pairs: (n^2 - n) / 2

with open('puzzle_inputs/puzzle_input.txt') as f:
    puzzle = f.read().splitlines()

print(puzzle)
# get index of the galaxies
galaxies = {}
empty_rows = []
cols_with_galaxies = []
galaxy_nr = 1
for rownumber, row in enumerate(puzzle, 1):
    if '#' in row:
        for colnumber, char in enumerate(row, 1):
            coordinates = {'row': 0, 'col': 0}
            if char == '#':
                coordinates['row'], coordinates['col'] = rownumber, colnumber
                galaxies[galaxy_nr] = coordinates
                cols_with_galaxies.append(colnumber)
                galaxy_nr += 1
    else:
        empty_rows.append(rownumber)
print("galaxies: ", galaxies)
print("empty rows: ", empty_rows)

# get the empty cols
cols_without_galaxies = [i for i in range(1, len(puzzle[0]) + 1) if i not in cols_with_galaxies]
print("cols without galax: ", cols_without_galaxies)

# recalculate the index positions of the galaxies with the expanded grid
# empty rows and cols are sorted in ascending order
factor = 1000000
shifted_galaxies = []
for coordinates in galaxies.values():
    temp_empty_row = list(filter(lambda z: z < coordinates['row'], empty_rows))
    temp_empty_cols = list(filter(lambda z: z < coordinates['col'], cols_without_galaxies))

    new_row = coordinates['row']
    new_col = coordinates['col']
    # if not empty
    if temp_empty_row:
        new_row = coordinates['row'] + len(temp_empty_row) * (factor - 1)
    if temp_empty_cols:
        new_col = coordinates['col'] + len(temp_empty_cols) * (factor - 1)
    shifted_galaxies.append((new_row, new_col))

print("shifted galaxies: ", shifted_galaxies)

d = 0
count_galaxy = len(shifted_galaxies)
while len(shifted_galaxies) > 0:
    for i in range(1, count_galaxy):
        x = abs(shifted_galaxies[0][1] - shifted_galaxies[i][1])
        y = abs(shifted_galaxies[0][0] - shifted_galaxies[i][0])
        d += x + y
    _ = shifted_galaxies.pop(0)
    count_galaxy -= 1
print("distance", d)
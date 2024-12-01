import numpy as np

with open("../inputs.txt") as f:
    puzzle = f.read().splitlines()
    puzzle = [line.split(" ") for line in puzzle]
    ids_left = np.array(sorted([int(line[0]) for line in puzzle]))  # first char
    ids_right = np.array(sorted([int(line[-1]) for line in puzzle]))  # last char

# solution first part
#print(np.sum(np.abs(ids_left - ids_right)))
unique, counts = np.unique(ids_right, return_counts=True)
lookup = dict(zip(unique, counts))
sum = 0
for id in ids_left:
    if id in lookup:
        occ = lookup[id]
        sum += occ * id
    else:
        continue
print(sum)
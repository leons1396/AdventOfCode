import numpy as np

# 7 6 4 ->diff -> -1 -2 decreasing order
# 4 6 7 ->diff -> 2 1  increasing order
# cases:
#  - all diffs have to <0
#  - all diffs have to >0
#  - max abs = 3

with open("../inputs.txt") as f:
    inputs = f.read().splitlines()
    inputs = [list(map(int, i.split(" "))) for i in inputs]
    print(inputs)

count = 0
for level in inputs:
    diff = np.diff(level)
    if not np.all(np.abs(diff) <= 3):
        # unsafe, max diff is 3
        continue

    if np.all(diff < 0):
        # safe, decreasing order of values
        count += 1
    elif np.all(diff > 0):
        # safe, increasing order of values
        count += 1
    else:
        print("mixed order")
print(count)
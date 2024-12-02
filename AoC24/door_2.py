import numpy as np

# cases
# - increasing order, all diffs > 0 & max diff <=3 -> safe
# - decreasing order, all diffs < 0 & max diff <=3 -> safe
# - if there are 2 equal adjacent values -> unsafe

def is_safe(lvl):
    inc = np.diff(lvl)
    # check values are in decreasing or increasing order
    if np.all(inc > 0) or np.all(inc < 0):
        # check if there is no bigger diff than 3
        if np.all(np.abs(inc) <= 3):
            return True
    return False

with open("../inputs.txt") as f:
    inputs = f.read().splitlines()
    inputs = [list(map(int, i.split(" "))) for i in inputs]
    print(inputs)

count = 0
for level in inputs:
    if is_safe(level):
        print("safe")
        count += 1
        continue
    else:
        for i in range(len(level)):
            lvl_copy = level.copy()
            del lvl_copy[i]
            if is_safe(lvl_copy):
                print("safe after deleting one value")
                count += 1
                break
        # if any diff bigger than 3 -> unsafe -> remove value -> safe? check again
        # if an diff is 0 -> unsafe -> remove value -> safe? check again

print(count)

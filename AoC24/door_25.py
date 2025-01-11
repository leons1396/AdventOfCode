def get_heights(schema):
    """    heights = []
    for col in range(0, len(schema[0])):
        s = 0
        for row in range(1, len(schema) - 1):
            if schema[row][col] == '#':
                s += 1
        heights.append(s)"""
    return [sum(1 for row in range(1, len(schema) - 1) if schema[row][col] == '#') for col in range(len(schema[0]))]

def part1(schemantics):
    # locks = top row filled with #
    # keys = top row filled with .
    locks = [get_heights(schema) for schema in schemantics if '#' in schema[0]]
    keys = [get_heights(schema) for schema in schemantics if '.' in schema[0]]

    """    for lock in locks:
        for key in keys:
            is_pair = False
            for l, k in zip(lock, key):
                if (k + l) > 5:
                    #print("No match")
                    is_pair = False
                    break
                else:
                    is_pair = True
                    #print("Match")
            if is_pair:
                count += 1"""
    return sum(all((k + l) <= 5 for l, k in zip(lock, key)) for lock in locks for key in keys)

def part2():
    return

if __name__ == "__main__":
    with open("../inputs.txt") as f:
        puzzle = f.read().split('\n\n')

        schemantics = []
        for line in puzzle:
            schemantics.append(line.split())

    print(schemantics)

    print("Erg part1: ", part1(schemantics))
    print("Erg part2: ", part2())

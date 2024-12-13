import copy

with open("../inputs.txt") as f:
    chars = set(f.read())
    chars.remove("\n")

with open("../inputs.txt") as f:
    puzzle = f.read().splitlines()
print(chars)
print(puzzle)

def calculate_perimeter(fields):
    # Directions representing the 4 possible neighbors (up, down, left, right)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    perimeters = []
    for field in fields:
        perimeter = 0
        # iterate through the points
        for x, y in field:
            for dx, dy in directions:
                neighbor = (x + dx, y + dy)
                # If the neighbor is not in the set, this edge contributes to the perimeter
                if neighbor not in field:
                    perimeter += 1
        perimeters.append(perimeter)
    return perimeters

def add_neighbor_poitns(field, cur_point, filtered_grid):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    x, y = cur_point
    for dx, dy in directions:
        neighbor = (x + dx, y + dy)
        if neighbor in filtered_grid and neighbor not in field:
            field.append(neighbor)
    return field

def check_for_neighbors(field, cur_point):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    x, y = cur_point
    for dx, dy in directions:
        neighbor = (x + dx, y + dy)
        if neighbor in field:
            return True
    return False

def calc_price(fields, perimeters):
    p = 0
    for field, perimeter in zip(fields, perimeters):
        p += len(field) * perimeter
    return p

def check_connecting_fields(fields):
    """if any point from a field is a neighbor from any another point from antoher field then
    those fields are connected"""
    fields_copy = copy.deepcopy(fields)

    while True:
        concatenate = False
        for i, field in enumerate(fields_copy, 1):
            if len(fields_copy) == 1:
                return fields_copy
            # iterated over each field
            if i == len(fields_copy):
                return fields_copy
            #temp = []
            for point in field:
                if i == len(fields_copy):
                    break
                slice_fields = fields_copy[i:]
                for j, f in enumerate(slice_fields, 0):
                    # check the next field in the list
                    if check_for_neighbors(f, point):
                        # concatenate
                        temp = fields_copy[i-1] + f
                        fields_copy.pop(i+j)
                        fields_copy.pop(i-1)
                        fields_copy.insert(0, list(set(temp)))
                        concatenate = True
                        break
                if concatenate:
                    # start new loop
                    break
            if concatenate:
                break

def part1(puzzle, chars):
    # {(x, y): char}
    grid = {(col, row): puzzle[row][col] for row in range(len(puzzle)) for col in range(len(puzzle[row]))}
    price = 0
    for c in chars:
        # filter grid by each char
        filtered_grid = dict(filter(lambda x: x[1] == c, grid.items()))
        # sort filtered grid by x
        filtered_grid = dict(sorted(filtered_grid.items(), key=lambda item: (item[0][1], item[0][0])))
        #print(filtered_grid)
        # find the connected fields
        fields = []
        #seen = []
        #while len(seen) == filtered_grid:
        field = []
        print("Char: ", c)

        for i, (point, char) in enumerate(filtered_grid.items()):
            # there are no neighbors for the current point
            if len(field) != 0 and not check_for_neighbors(field, point):
                fields.append(field.copy())
                field.clear()
                field.append(point)
                field = add_neighbor_poitns(field, point, filtered_grid)
                continue

            if len(field) == 0:
                field.append(point)
                # add neighbor points
                field = add_neighbor_poitns(field, point, filtered_grid)
                continue
            else:
                # only add neighbor points to the current field if the current point
                # has any neighbors in that field
                field = add_neighbor_poitns(field, point, filtered_grid)
        fields.append(field.copy())
        field.clear()
        #print(fields)
        fields = check_connecting_fields(fields)
        perimeters = calculate_perimeter(fields)
        #print(f"For Char {c} the perimeters are {perimeters}. Area of first field {len(fields[0])}")
        price += calc_price(fields, perimeters)
        #print(f"Char {c}: {calc_price(fields, perimeters)}")
    return price

def part2(puzzle):
    return

erg = part1(puzzle, chars)
print("Part 1:", erg)

def init_move(start_pos, tile, len_line, direction):
    # move up
    if direction == 'up':
        if tile in ['F', '7', '|']:
            return start_pos - len_line
    # move right
    if direction == 'right':
        if tile in ['J', '7', '-']:
            return start_pos + 1
    # move down
    if direction == 'down':
        if tile in ['L', 'J', '|']:
            return start_pos + len_line
    # move left
    if direction == 'left':
        if tile in ['F', '-', 'L']:
            return start_pos - 1
    return None


with open('puzzle_inputs/puzzle_input.txt') as f:
    puzzle = f.read().splitlines()

len_line = len(puzzle[0])
print("len_line", len_line)
# create mapping of position and corresponding symbol
tile_map = {idx: tile for idx, tile in enumerate(''.join(puzzle), 1)}

# find S in tile_map
start_pos = None
for i, v in enumerate(tile_map.values(), 1):
    if v == "S":
        start_pos = i
        break

print("start_pos", start_pos)

found_s = False
for i in range(0, 4):
    if found_s:
        break
    cur_pos = None
    visited = []
    prev_move = []
    # init with right step
    if i == 0:
        # check if I can step to the right
        if start_pos % len_line != 0:
            cur_pos = init_move(start_pos, tile_map[start_pos + 1], len_line, 'right')
            # check if the returned position is a valid position. it must be within the map and if the new pos is on
            # a border then it is a invalid move too.
            if isinstance(cur_pos, int):
                visited.append(cur_pos)
                prev_move.append('right')
            else:
                # calc pos is invalid
                continue
        else:
            # cur_pos is at right border
            continue
    if i == 1:
        # check if I can step to the left
        if start_pos % len_line != 1:
            cur_pos = init_move(start_pos, tile_map[start_pos - 1], len_line, 'left')
            if isinstance(cur_pos, int):
                visited.append(cur_pos)
                prev_move.append('left')
            else:
                continue
        else:
            # cur_pos is at left border
            continue
    if i == 2:
        # check if I can step down
        if start_pos < len(tile_map) - len_line:
            cur_pos = init_move(start_pos, tile_map[start_pos + len_line], len_line, 'down')
            if isinstance(cur_pos, int):
                visited.append(cur_pos)
                prev_move.append('down')
            else:
                continue
        else:
            # cur_pos is at top border
            continue
    if i == 3:
        # check if I can step up
        if start_pos > len_line:
            cur_pos = init_move(start_pos, tile_map[start_pos - len_line], len_line, 'up')
            if isinstance(cur_pos, int):
                visited.append(cur_pos)
                prev_move.append('up')
            else:
                continue
        else:
            # cur_pos is at bottom border
            continue
    # start walking
    while True:
        # get tile
        tile = tile_map[cur_pos]
        if prev_move[-1] == 'left':
            # step down
            if tile == 'F':
                cur_pos = cur_pos + len_line
                prev_move.append('down')
            # step left
            elif tile == '-':
                cur_pos = cur_pos - 1
                prev_move.append('left')
            # step up
            elif tile == 'L':
                cur_pos = cur_pos - len_line
                prev_move.append('up')
            else:
                print("Start from beginning")
                print("current pos when starting new: ", cur_pos)
                break
        elif prev_move[-1] == 'right':
            # step up
            if tile == 'J':
                cur_pos = cur_pos - len_line
                prev_move.append('up')
            # step down
            elif tile == '7':
                cur_pos = cur_pos + len_line
                prev_move.append('down')
            # step right
            elif tile == '-':
                cur_pos = cur_pos + 1
                prev_move.append('right')
            else:
                print("Start from beginning")
                print("current pos when starting new: ", cur_pos)
                break
        elif prev_move[-1] == 'up':
            # step right
            if tile == 'F':
                cur_pos = cur_pos + 1
                prev_move.append('right')
            # step up
            elif tile == '|':
                cur_pos = cur_pos - len_line
                prev_move.append('up')
            # step left
            elif tile == '7':
                cur_pos = cur_pos - 1
                prev_move.append('left')
            else:
                print("Start from beginning")
                print("current pos when starting new: ", cur_pos)
                break
        elif prev_move[-1] == 'down':
            # step right
            if tile == 'L':
                cur_pos = cur_pos + 1
                prev_move.append('right')
            # step down
            elif tile == '|':
                cur_pos = cur_pos + len_line
                prev_move.append('down')
            # step left
            elif tile == 'J':
                cur_pos = cur_pos - 1
                prev_move.append('left')
            else:
                print("Start from beginning")
                print("current pos when starting new: ", cur_pos)
                break
        # do we reach start of cycle start_pos == cur
        if cur_pos == start_pos:
            # exit condition - found S
            print("found Start position")
            found_s = True
            break
        if cur_pos in visited:
            print("found wrong cycle")
            break

        # validate
        prev_pos = visited[-1]
        # if cur_pos is at left border and want to step left
        if prev_pos % len_line == 1 and prev_move[-1] == 'left':
            print("left border")
            break
        # if cur pos is at right border and want to step right
        if prev_pos % len_line == 0 and prev_move[-1] == 'right':
            print("right border")
            break
        # if cur pos is at top border and want to step up
        if cur_pos < 1:
            # use cur_pos instead of prev_pos
            print("top border")
            break
        if cur_pos > len(tile_map):
            print("bottom border")
            break
        # add to visited
        visited.append(cur_pos)

print(len(visited))
print("farthest = ", (len(visited) // 2) + 1)
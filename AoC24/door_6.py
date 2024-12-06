# if . is free, move
# if #, turn right
# if end of puzzle, stop
history_moves = []

def is_free(puzzle, cur_pos, next_move):
    if next_move == "up":
        if puzzle[cur_pos[0]-1][cur_pos[1]] == "#":
            # turn right
            #print(history_moves)
            return "right", cur_pos
        elif cur_pos[0] - 1 == 0:
            return "end", (cur_pos[0] - 1, cur_pos[1])
        else:
            # step further
            #history_moves.append(next_move)
            return "up", (cur_pos[0] - 1, cur_pos[1])
    elif next_move == "down":
        if puzzle[cur_pos[0]+1][cur_pos[1]] == "#":
            #print(history_moves)
            return "left", cur_pos
        elif cur_pos[0] + 1 == len(puzzle) - 1:
            return "end", (cur_pos[0] + 1, cur_pos[1])
        else:
            # step further
            #history_moves.append(next_move)
            return "down", (cur_pos[0] + 1, cur_pos[1])
    elif next_move == "left":
        if puzzle[cur_pos[0]][cur_pos[1]-1] == "#":
            #print(history_moves)
            return "up", cur_pos
        elif cur_pos[1] - 1 == 0:
            return "end", (cur_pos[0], cur_pos[1] - 1)
        else:
            # step further
            #history_moves.append(next_move)
            return "left", (cur_pos[0], cur_pos[1] - 1)
    elif next_move == "right":
        if puzzle[cur_pos[0]][cur_pos[1]+1] == "#":
            #print(history_moves)
            return "down", cur_pos
        elif cur_pos[1] + 1 == len(puzzle[0]) - 1:

            return "end", (cur_pos[0], cur_pos[1] + 1)
        else:
            # step further
            #history_moves.append(next_move)
            return "right", (cur_pos[0], cur_pos[1] + 1)

def part1(puzzle):
    count = 0
    for i, row in enumerate(puzzle):
        for j, col in enumerate(row):
            if puzzle[i][j] != "." and puzzle[i][j] != "#":
                cur_pos = (i, j)
                break

    next_move = {"<": "left", "^": "up", ">": "right", "v": "down"}[puzzle[cur_pos[0]][cur_pos[1]]]
    puzzle[cur_pos[0]] = puzzle[cur_pos[0]].replace(puzzle[cur_pos[0]][cur_pos[1]], ".")
    print(next_move)
    print(puzzle)
    history_moves.append(cur_pos)
    break_counter = 0
    while True:
        next_move, cur_pos = is_free(puzzle, cur_pos, next_move)
        if cur_pos not in history_moves:
            history_moves.append(cur_pos)
        #print(history_moves)
        if next_move == "end":
            print(history_moves)
            return len(history_moves)


        break_counter += 1
        if break_counter == 10000:
            return "BREAK COUNTER REACHED"

def part2(puzzle):
    return count

with open('../inputs.txt', 'r') as f:
    puzzle = f.read().splitlines()

print("NUMBER MOVES: ", part1(puzzle))
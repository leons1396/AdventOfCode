def wasteland(inputs):
    pass


with open("puzzle_inputs/wasteland_puzzle.txt") as f:
    inputs = f.readlines()
    inputs = [line.replace("\n", "").strip().split(" = ") for line in inputs]
    print(inputs)

instructions = inputs.pop(0)
_ = inputs.pop(0)

print(instructions[0][0], len(instructions[0]))
current_node = None
for node in inputs:
    if node[0] == 'AAA':
        current_node = node
        break

i = 0  # only for L and R
node_idx = 0
steps = 0
while True:
    if len(instructions[0]) == i:
        i = 0  # start from beginning

    current_instruction = instructions[0][i]

    if current_instruction == "L":
        go_to = current_node[1][1:4]
    else:
        go_to = current_node[1][6:9]

    for j, node in enumerate(inputs):
        if go_to == node[0]:
            node_idx = j
            steps += 1
            break

    current_node = inputs[node_idx]

    i += 1

    if current_node[0] == 'ZZZ':
        print("Reach Final Node")
        break

    if steps == 100000:
        print("BREAK")
        break

print(f"Total Steps {steps}")
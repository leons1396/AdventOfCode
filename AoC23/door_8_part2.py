from math import gcd

with open("puzzle_inputs/wasteland_puzzle.txt") as f:
    inputs = f.readlines()
    inputs = [line.replace("\n", "").strip().split(" = ") for line in inputs]
    print(inputs)

instructions = inputs.pop(0)
_ = inputs.pop(0)

print(instructions[0][0], len(instructions[0]))

nec_nodes = {}
for idx, node in enumerate(inputs):
    if node[0][-1] == 'A':
        nec_nodes[node[0]] = idx

node_mapping = {node[0]:idx for idx, node in enumerate(inputs)}

print(nec_nodes)
print(node_mapping)

# https://github.com/hyper-neutrino/advent-of-code/blob/main/2023/day08p2.py
# needed help to get the idea just walk from nodes that end with Z to Z and then solving with lcm
cycles = []
for current, value in nec_nodes.items():
    cycle = []

    to_node = value
    current_steps = instructions[0]
    step_count = 0
    first_z = None
    while True:
        while step_count == 0 or not current.endswith("Z"):
            step_count += 1

            if current_steps[0] == "L":
                current = inputs[to_node][1][1:4]  # Where to jump next
            else:
                current = inputs[to_node][1][6:9]

            current_steps = current_steps[1:] + current_steps[0]
            to_node = node_mapping[current]

        cycle.append(step_count)

        if first_z is None:
            first_z = current
            step_count = 0
        elif current == first_z:
            break

    cycles.append(cycle)

total_steps = 0
steps = [c[0] for c in cycles]

lcm = steps.pop(0)
for step in steps:
    lcm = (lcm * step) // gcd(lcm, step)

print(lcm)

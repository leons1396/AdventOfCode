with open('puzzle_inputs/puzzle_input.txt') as f:
    puzzle = f.read().splitlines()
    sequences = [list(map(int, line.split(" "))) for line in puzzle]

print(sequences)

interpolated_values = []
for seq in sequences:
    history = []  # one history for each sequence
    history.append(seq)
    while True:
        diffs = []
        for i in range(len(seq) - 1):
            diffs.append(seq[i+1] - seq[i])
        history.insert(0, diffs)
        seq = list(diffs)

        if all(diff == 0 for diff in diffs):
            # Reach the zero line in sequence
            break

    interpolate = 0
    for h in range(len(history)-1):
        interpolate = interpolate + history[h+1][-1]
    interpolated_values.append(interpolate)

print(interpolated_values)
print(sum(interpolated_values))

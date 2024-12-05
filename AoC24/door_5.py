def check(rules: list, update_seq: list) -> bool:
    for i in range(len(update_seq)):
        val_to_check = update_seq[i]
        subset_rules = list(filter(lambda x: x[0] == val_to_check, rules))
        for val in update_seq[i+1:]:
            if (val_to_check, val) in subset_rules:
            # check the rules for the next value
                continue
            else:
                return False
    # every rule is passed
    return True

def part1(rules, updates):
    count = 0
    for update in updates:
        if check(rules, update_seq=update):
            count += update[((len(update) - 1) // 2)]
    return count

def part2(puzzle):
    pass

with open("../inputs.txt") as f:
    lines = f.read().split("\n\n")
    rules = [line for line in lines[0].split("\n")]
    rules = [(int(rule.split("|")[0]), int(rule.split("|")[1])) for rule in rules]
    _updates = [line for line in lines[1].split("\n")]

    updates = []
    for update in _updates:
        temp = [int(val) for val in update.split(",")]
        updates.append(temp)

for update in updates:
    if len(update) % 2 == 0:
        print("Error: update sequence must have an odd number of elements")

#print(rules)
#print(updates)

count = part1(rules, updates)
print(count)
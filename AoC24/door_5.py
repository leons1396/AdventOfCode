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

def reorder(rules: list, update_seq: list) -> list:
    break_counter = 0
    stop = True
    while stop:
        for i, cur in enumerate(update_seq, 1):
            if i == len(update_seq):
                stop = False
                break
            subset_rules = list(filter(lambda x: x[0] == cur, rules))
            # if empty than there is no rule -> swap
            if len(subset_rules) == 0:
                update_seq[i - 1], update_seq[i] = update_seq[i], update_seq[i - 1]
                break
            if (cur, update_seq[i]) not in subset_rules:
                update_seq[i - 1], update_seq[i] = update_seq[i], update_seq[i - 1]
                break
        break_counter += 1
        if break_counter == 5000:
            print("Break counter reached")
            break
    return update_seq

def part1(rules, updates):
    count = 0
    for update in updates:
        if check(rules, update_seq=update):
            count += update[((len(update) - 1) // 2)]
    return count

def part2(rules, updates):
    count = 0
    for update in updates:
        # only focus on the incorrect ones
        if not check(rules, update_seq=update):
            new_update = reorder(rules, update)
            count += new_update[((len(new_update) - 1) // 2)]
    return count

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
count = part2(rules, updates)
print(count)
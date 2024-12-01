def trebuchet(calib_doc):
    encoded = list()
    L = list()
    spelled_values = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    for line in calib_doc:
        # get single values

        temp_numbers = {f"{char}_{idx}": idx for idx, char in enumerate(line) if char.isdigit()}

        for key, val in spelled_values.items():
            find_first = line.find(key)
            find_last = line.rfind(key)
            if find_first == -1 or find_last == -1:
                # given substring is not in calib_doc line
                continue

            if find_first != find_last:
                temp_numbers[f"{val}_{find_first}"] = find_first
                temp_numbers[f"{val}_{find_last}"] = find_last
            else:
                temp_numbers[val] = find_first

        sorted_temp_numbers = dict(sorted(temp_numbers.items(), key=lambda x: x[1]))

        L = [int(key.split("_")[0]) for key in sorted_temp_numbers.keys()]

        if len(L) == 1:
            encoded.append((L[0] * 10) + L[0])

        elif len(L) >= 2:
            first_last = L[0], L[-1]
            encoded.append(int(''.join(map(str, first_last))))

    print(encoded)
    return sum(encoded)


if __name__ == '__main__':
    with open('../puzzle_inputs/puzzle_input.txt') as f:
        lines = f.readlines()
        lines = [code.replace("\n", "") for code in lines]

    print(lines)
    #debug = ['twokdkcbhtqxfc87rkgctwo']
    total = trebuchet(lines)
    print("Total: ", total)

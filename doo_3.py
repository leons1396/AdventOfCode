def encode_part_numbers(lines):
    sum_part_numbers = 0
    prev_tup_values_pos = list()
    prev_tup_values_pos_2 = list()
    prev_symbols_pos = list()
    prev_symbols_pos_2 = list()
    current_tup_values_pos = list()
    current_symbols_pos = list()
    i = 0
    for line in lines:
        i += 1
        digit_pos = list()
        digit = ""

        prev_symbols_pos_2 = list(prev_symbols_pos)
        prev_symbols_pos = list(current_symbols_pos)
        current_symbols_pos.clear()

        prev_tup_values_pos_2 = list(prev_tup_values_pos)
        prev_tup_values_pos = list(current_tup_values_pos)
        current_tup_values_pos.clear()
        for i, char in enumerate(line):
            if char.isdigit():
                digit_pos.append(i)  # type str
                digit += char

            elif char != '.':
                current_symbols_pos.append(i)
                digit = ""
                digit_pos.clear()
            else:
                # Char is a dot
                if digit:  # digit is not empty
                    number_pos = (digit_pos[0], digit_pos[-1], int(digit))  #start ind, end index, number
                    print("NUmber ps: ", number_pos)
                    current_tup_values_pos.append(number_pos)

                    digit = ""
                    digit_pos.clear()

            #print(digit)
            #print(digit_pos)
        symbols = prev_symbols_pos_2 + prev_symbols_pos + current_symbols_pos
        values = prev_tup_values_pos_2 + prev_tup_values_pos + current_tup_values_pos
        print("Symbols: ", symbols)
        print("Tuple Values: ", values)
        print("PREV Tuple: ", prev_tup_values_pos)
        print("PREV 2 Tuple: ", prev_tup_values_pos_2)
        if len(current_symbols_pos) > 0:
            for pos in symbols:
                for tup_val in values:
                    if pos in range(tup_val[0]-1, tup_val[1]+2):  #end is exclusive
                        sum_part_numbers += tup_val[2]

        print("Sum: ", sum_part_numbers)

        if i == 3:
            break


if __name__ == '__main__':
    with open('puzzle_inputs/part_numbers.txt') as f:
        engine_schematic = f.readlines()
        engine_schematic = [code.replace("\n", "") for code in engine_schematic]

    print(engine_schematic)
    #engine_schematic = ["..............................569..............-.....&.82..512..............................................+............913..&888..695.%..."]
    total = encode_part_numbers(engine_schematic)
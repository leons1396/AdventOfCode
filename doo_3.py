def encode_part_numbers(lines):

    #prev_tup_values_pos = list()
    #prev_tup_values_pos_2 = list()
    #prev_symbols_pos = list()
    #prev_symbols_pos_2 = list()
    current_tup_values_pos = list()
    current_symbols_pos = list()

    for line_number, line in enumerate(lines):
        digit_pos = list()
        digit = ""

        for i, char in enumerate(line):
            if char.isdigit():
                digit_pos.append(i)  # type str
                digit += char

            elif char != '.':
                current_symbols_pos.append((i, line_number))
                if digit:
                    if i == digit_pos[-1] + 1:
                        number_pos = (digit_pos[0], digit_pos[-1], int(digit), line_number)  #start ind, end index, number
                        print("NUmber ps: ", number_pos)
                        current_tup_values_pos.append(number_pos)

                digit = ""
                digit_pos.clear()
            else:
                # Char is a dot
                if digit:  # digit is not empty
                    number_pos = (digit_pos[0], digit_pos[-1], int(digit), line_number)  #start ind, end index, number
                    print("NUmber ps: ", number_pos)
                    current_tup_values_pos.append(number_pos)

                    digit = ""
                    digit_pos.clear()

            if i == len(line)-1:
                if digit:  # digit is not empty
                    number_pos = (digit_pos[0], digit_pos[-1], int(digit), line_number)  #start ind, end index, number
                    print("NUmber ps: ", number_pos)
                    current_tup_values_pos.append(number_pos)

                    digit = ""
                    digit_pos.clear()


    sum_part_numbers = 0
    if len(current_symbols_pos) > 0:
        for tup_symbol in current_symbols_pos:
            pos = tup_symbol[0]
            line_sym = tup_symbol[1]
            for i, tup_val in enumerate(current_tup_values_pos):
                if tup_val[3] == line_sym - 1 or line_sym == tup_val[3] or line_sym + 1 == tup_val[3]:
                    if pos in range(tup_val[0]-1, tup_val[1]+2):  #end is exclusive
                        sum_part_numbers += tup_val[2]

        return sum_part_numbers


if __name__ == '__main__':
    with open('puzzle_inputs/part_numbers.txt') as f:
        engine = f.readlines()
        engine = [code.replace("\n", "") for code in engine]

    total = encode_part_numbers(engine)
    print("Toal Sum: ", total)  #507214

def card_game(cards):
    total_points = 0
    for round in cards:
        oponent_cards, my_cards = round
        oponent_cards_str = oponent_cards.split(" ")
        my_cards_str = my_cards.split(" ")

        oponent_cards_int = [int(number) for number in oponent_cards_str if number]
        my_cards_int = [int(number) for number in my_cards_str if number]

        # Now iterate through oponent_cards and my_cards. Take one value from oponent and proof if it is in my_cards_int
        # for every hit increase a counter and double it
        # Problem if there is a number twice ???
        match = 0
        for win_number in oponent_cards_int:
            if win_number in my_cards_int:
                match += 1

        if match > 0:
            total_points = total_points + 2**(match-1)

    return total_points


def card_game_part_2(cards):
    table = {f"card_{i}": 1 for i in range(1, len(cards) + 1)}
    for card_num, round in enumerate(cards):
        card_num += 1

        oponent_cards, my_cards = round
        oponent_cards_str = oponent_cards.split(" ")
        my_cards_str = my_cards.split(" ")

        oponent_cards_int = [int(number) for number in oponent_cards_str if number]
        my_cards_int = [int(number) for number in my_cards_str if number]

        # Now iterate through oponent_cards and my_cards. Take one value from oponent and proof if it is in my_cards_int
        # for every hit increase a counter and double it
        # Problem if there is a number twice ???
        match = 0
        for win_number in oponent_cards_int:
            if win_number in my_cards_int:
                match += 1

        if match > 0:
            for copy in range(1, table[f"card_{card_num}"]+1):
                for num in range(card_num+1, card_num+match+1):
                    table[f"card_{num}"] += 1

    return sum(table.values())


if __name__ == '__main__':
    with open('puzzle_inputs/cards.txt') as f:
        scratchcards = f.readlines()
        scratchcards = [puzzle[10:].replace("\n", "").split(' | ') for puzzle in scratchcards]
    print(scratchcards)
    total_sum = card_game(scratchcards)
    total_sum_2 = card_game_part_2(scratchcards)
    print("Sum: ", total_sum_2)

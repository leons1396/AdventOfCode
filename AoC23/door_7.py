def my_f(cards):
    trans_to_values = {'A':14, 'K':13, 'Q':12, 'J':11, 'T':10}
    five_of_kind = []
    four_of_kind = []
    full_house = []
    three_of_kind = []
    two_pair = []
    pair = []
    high_card = []

    for j, card in enumerate(cards):
        deck_, _ = card
        deck, bit = deck_.split(" ")
        print(deck, bit)

        hand = []
        for char in deck:
            if not char.isdigit():
                hand.append(trans_to_values[char])
            else:
                hand.append(int(char))
        print(hand)


        num_three_of_kind = 0
        num_pair = 0
        is_high_card = True
        for i in range(2,15):
            occ = hand.count(i)
            if occ == 5:
                five_of_kind.append((hand, bit))
                is_high_card = False
                break
            elif occ == 4:
                four_of_kind.append((hand, bit))
                is_high_card = False
                break
            elif occ == 3:
                num_three_of_kind += 1
            elif occ == 2:
                num_pair += 1
            else:
                continue

        if num_three_of_kind == 1 and num_pair == 1:
            full_house.append((hand, int(bit)))
        elif num_pair > 1:
            two_pair.append((hand, int(bit)))
        elif num_pair == 1:
            pair.append((hand, int(bit)))
        elif num_three_of_kind == 0 and num_pair == 0 and is_high_card:
            high_card.append((hand, int(bit)))

        print(high_card)
        print(four_of_kind)
        print(pair)
        if j == 3:
            break
       
        # Now sort every cards list by his sum

        # concatenate all cards list -> rank * bit

if __name__ == '__main__':
    with open('puzzle_inputs/camel_cards.txt') as f:
        cards = f.readlines()
        cards = [c.split('\n') for c in cards]
    print(cards)
    my_f(cards)
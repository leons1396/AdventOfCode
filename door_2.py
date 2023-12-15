def cube_game(puzzle_input, matching_cubes):
    sum_game = 0
    power_sum = 0
    for round, game in enumerate(puzzle_input):
        game_set = game[1].split("; ")
        draws = [draw.split(", ") for draw in game_set]
        print("Draws", draws)

        cubes_list = list()
        for cube in draws:
            cubes = dict(green=-1, red=-1, blue=-1)
            for idx in range(len(cube)):
                amount, color = cube[idx].split(' ')
                cubes[color] = int(amount)

            cubes_list.append(cubes)

        impossible = False
        for cube_set in cubes_list:
            for key, value in cube_set.items():
                if value == -1:
                    continue

                if key in matching_cubes:
                    if value > matching_cubes[key]:
                        impossible = True

        print("List: ", cubes_list)

        max_blue = max(cub['blue'] for cub in cubes_list)
        max_green = max(cub['green'] for cub in cubes_list)
        max_red = max(cub['red'] for cub in cubes_list)

        power_sum += max_blue * max_green * max_red

        if not impossible:
            sum_game += round + 1

    return sum_game, power_sum

if __name__ == '__main__':
    with open('cube_game.txt') as f:
        lines = f.readlines()
        lines = [code.replace("\n", "").split(": ") for code in lines]

    print(lines)

    cubes_in_bag = dict(red=12, green=13, blue=14)
    total_game, total_power = cube_game(lines, cubes_in_bag)
    print("Total: ", total_game)
    print("Total Power: ", total_power)



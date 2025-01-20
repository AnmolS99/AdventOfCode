limits = {"red": 12, "green": 13, "blue": 14}


def check_over_limits(round: str):
    colors = round.split(",")
    for color in colors:

        for k, v in limits.items():

            if k in color:
                num_cubes = color.replace(k, "")
                num_cubes = int(num_cubes.strip())

                if num_cubes > v:
                    return True
    return False


def part_one_solution():
    id_sum = 0
    for line in open("./2/input.txt").readlines():
        game_id_string, rounds_string = line.split(":")
        game_id = int(game_id_string[5:])

        rounds = rounds_string.split(";")

        possible = True
        for round in rounds:

            if check_over_limits(round):
                possible = False

        if possible:
            id_sum += game_id

    print(id_sum)


def get_game_power(rounds):
    color_highest = {"red": 0, "green": 0, "blue": 0}

    for round in rounds:

        colors = round.split(",")

        for color in colors:

            for k, v in color_highest.items():

                if k in color:

                    num_cubes = color.replace(k, "")
                    num_cubes = int(num_cubes.strip())

                    if num_cubes > v:
                        color_highest[k] = num_cubes
    return color_highest["red"] * color_highest["green"] * color_highest["blue"]


def part_two_solution():
    sum = 0
    for line in open("./2/input.txt").readlines():
        game_id_string, rounds_string = line.split(":")
        rounds = rounds_string.split(";")
        power = get_game_power(rounds)
        sum += power
    print(sum)


part_two_solution()

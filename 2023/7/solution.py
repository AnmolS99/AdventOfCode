values = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2
}


def get_type(game):
    cards = list(game)
    num_same = 0
    for card in cards:
        same = cards.count(card)
        if same > num_same:
            num_same = same
    if num_same == 5:
        return 6
    elif num_same == 4:
        return 5
    elif num_same == 3:
        if len(set(cards)) == 2:
            return 4
        else:
            return 3
    elif num_same == 2:
        if len(set(cards)) == 3:
            return 2
        else:
            return 1
    else:
        return 0


def hand1_smaller(hand1, hand2):
    for i in range(len(hand1)):
        if values[hand1[i]] < values[hand2[i]]:
            return True
        elif values[hand1[i]] > values[hand2[i]]:
            return False
    Exception("Hands exactly the same")


def sort_same_types(indices_list, games_list):
    change = True
    count = 0
    while change == True:
        count += 1
        change = False

        for i in range(len(indices_list) - 1):
            idx = indices_list[i]
            idx_2 = indices_list[i + 1]
            if not hand1_smaller(games_list[idx], games_list[idx_2]):
                tmp = idx
                indices_list[i] = indices_list[i + 1]
                indices_list[i + 1] = tmp
                change = True
    return indices_list


def sort_games(games):
    sorted_indices = []
    types = []
    for k, v in games.items():
        types.append(get_type(k))

    for type in range(len(types)):
        print("Type: " + str(type))
        indices = [i for i in range(len(types)) if types[i] == type]
        print("\t- Sorting " + str(len(indices)) + " games")
        if len(indices) > 0:
            sorted = sort_same_types(indices, list(games.keys()))
            for idx in sorted:
                sorted_indices.append(idx)
    return sorted_indices


def task_one_solution():
    games = {}
    sum = 0
    lines = open("./7/input.txt").read().split("\n")
    for line in lines:
        games[line.split(" ")[0]] = int(line.split(" ")[1])
    sorted_indices = sort_games(games)

    rank = 1
    for i in sorted_indices:
        bid = int(list(games.values())[i])
        sum += rank * bid
        rank += 1
        print("Rank: " + str(rank))
    print(sum)


task_one_solution()
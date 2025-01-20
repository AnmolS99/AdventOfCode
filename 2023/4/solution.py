def task_one_solution():
    sum = 0
    for line in open("./4/input.txt").readlines():
        cards_string = line.split(":")[1]
        winning_nums_string, scratch_num_string = cards_string.split("|")

        winning_nums = winning_nums_string.strip().split(" ")
        winning_nums = list(filter(('').__ne__, winning_nums))
        scratch_num = scratch_num_string.strip().split(" ")
        scratch_num = list(filter(('').__ne__, scratch_num))

        wins = len([i for i in scratch_num if i in winning_nums])

        if wins > 0:
            sum += (2**(wins - 1))

    print(sum)


def task_two_solution():
    with open("./4/input.txt", "r") as f:
        num_games = len(f.readlines())

    scratchcard_list = [0] * num_games

    idx = -1
    for line in open("./4/input.txt").readlines():
        idx += 1

        scratchcard_list[idx] += 1

        cards_string = line.split(":")[1]
        winning_nums_string, scratch_num_string = cards_string.split("|")

        winning_nums = winning_nums_string.strip().split(" ")
        winning_nums = list(filter(('').__ne__, winning_nums))
        scratch_num = scratch_num_string.strip().split(" ")
        scratch_num = list(filter(('').__ne__, scratch_num))

        wins = len([i for i in scratch_num if i in winning_nums])

        if wins > 0:
            for i in range(1, wins + 1):
                scratchcard_list[idx + i] += scratchcard_list[idx]

    print(sum(scratchcard_list))


task_two_solution()
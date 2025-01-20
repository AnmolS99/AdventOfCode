def task_one_solution():
    input_file = open("./6/input.txt").read()
    times_string, distance_string = input_file.split("\n")

    times = list(filter(('').__ne__, times_string.split(" ")))[1:]
    distances = list(filter(('').__ne__, distance_string.split(" ")))[1:]

    product = 1
    for i in range(len(times)):
        time = int(times[i])
        distance = int(distances[i])
        num_wins = 0
        for t in range(time + 1):
            dist = t * (time - t)
            if dist > distance:
                num_wins += 1
        product *= num_wins
    print(product)


def task_two_solution():
    input_file = open("./6/input.txt").read()
    times_string, distance_string = input_file.split("\n")

    times = list(filter(('').__ne__, times_string.split(" ")))[1:]
    distances = list(filter(('').__ne__, distance_string.split(" ")))[1:]

    product = 1

    time = int("".join(str(x) for x in times))
    distance = int("".join(str(x) for x in distances))
    num_wins = 0
    for t in range(time + 1):
        dist = t * (time - t)
        if dist > distance:
            num_wins += 1
    product *= num_wins
    print(product)


task_two_solution()
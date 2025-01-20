def task_one_solution():
    input_file = open("./5/input.txt").read()
    seeds_string = input_file.split("\n\n")[0]
    maps_string_list = input_file.split("\n\n")[1:]
    lowest_location_num = None

    for seed in seeds_string.split(":")[1].split(" ")[1:]:
        num = int(seed)

        for maps_string in maps_string_list:

            ranges = maps_string.split("\n")[1:]
            ranges = list(filter(('').__ne__, ranges))

            for range in ranges:
                dst, src, length = range.split(" ")
                dst, src, length = int(dst), int(src), int(length)

                if (num >= src) and (num <= src + length - 1):
                    num = dst + (num - src)
                    break

        if (lowest_location_num is None) or (num < lowest_location_num):
            lowest_location_num = num
    print(lowest_location_num)


def task_two_solution():
    input_file = open("./5/input.txt").read()
    seeds_string = input_file.split("\n\n")[0]
    maps_string_list = input_file.split("\n\n")[1:]

    lowest_location_num = None

    seeds_list = seeds_string.split(":")[1].split(" ")[1:]
    for i in range(len(seeds_list) // 2):
        start_seed = int(seeds_list[i * 2])
        seed_length = int(seeds_list[(i * 2) + 1])

        for seed in range(start_seed, start_seed + seed_length):
            print("Seed " + str(seed) + " (nr. " + str(i) + ")")

            num = int(seed)

            for maps_string in maps_string_list:

                ranges = maps_string.split("\n")[1:]
                ranges = list(filter(('').__ne__, ranges))

                for curr_range in ranges:
                    dst, src, length = curr_range.split(" ")
                    dst, src, length = int(dst), int(src), int(length)

                    if (num >= src) and (num <= src + length - 1):
                        num = dst + (num - src)
                        break

            if (lowest_location_num is None) or (num < lowest_location_num):
                lowest_location_num = num
    print(lowest_location_num)


task_two_solution()
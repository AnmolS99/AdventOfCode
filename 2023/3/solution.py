import numpy as np


def has_special_character(character_list):
    for character in character_list:
        if (not character.isdigit()) and (character != ".") and (character !=
                                                                 "\n"):
            return True
    return False


def has_adjecent_special_symbol(iy, ix_start, ix_end, matrix):
    adjecent_symbols = []
    if iy > 0:

        if ix_start > 0:  # Top left corner
            adjecent_symbols.append(matrix[iy - 1, ix_start - 1])

        for ix in range(ix_start, ix_end + 1):  # Row directly above
            adjecent_symbols.append(matrix[iy - 1, ix])

        if ix_end < (matrix.shape[1] - 2):  # Top right corner
            adjecent_symbols.append(matrix[iy - 1, ix_end + 1])

    if iy < (matrix.shape[0] - 2):

        if ix_start > 0:  # Bottom left corner
            adjecent_symbols.append(matrix[iy + 1, ix_start - 1])

        for ix in range(ix_start, ix_end + 1):  # Row directly below
            adjecent_symbols.append(matrix[iy + 1, ix])

        if ix_end < (matrix.shape[1] - 2):  # Bottom right corner
            adjecent_symbols.append(matrix[iy + 1, ix_end + 1])

    if ix_start > 0:  # Directly to the left
        adjecent_symbols.append(matrix[iy, ix_start - 1])

    if ix_end < (matrix.shape[1] - 2):  # Directly to the right
        adjecent_symbols.append(matrix[iy, ix_end + 1])

    return has_special_character(adjecent_symbols), adjecent_symbols


def part_one_solution():
    sum = 0
    matrix = []
    for line in open("./3/input.txt").readlines():
        matrix.append([*line])

    np_matrix = np.array(matrix)

    for iy in range(0, np_matrix.shape[0]):
        reading_num = False
        start_index = None
        end_index = None
        current_num = ""

        for ix in range(0, np_matrix.shape[1]):
            current_char = np_matrix[iy, ix]

            if current_char.isdigit():
                if not reading_num:
                    reading_num = True
                    start_index = ix
                current_num += current_char

            elif (not current_char.isdigit() and reading_num):
                end_index = ix - 1
                has_adjecent, adjecent_list = has_adjecent_special_symbol(
                    iy, start_index, end_index, np_matrix)
                if has_adjecent:
                    sum += int(current_num)
                else:
                    print(current_num)
                    print(adjecent_list)

                reading_num = False
                start_index = None
                end_index = None
                current_num = ""
    print(sum)


def remove_duplicate_indices(iy, ix, adjecent_nums_index: list):
    if (iy - 1, ix) in adjecent_nums_index:
        if (iy - 1, ix - 1) in adjecent_nums_index:
            adjecent_nums_index.remove((iy - 1, ix - 1))
        if (iy - 1, ix + 1) in adjecent_nums_index:
            adjecent_nums_index.remove((iy - 1, ix + 1))
    if (iy + 1, ix) in adjecent_nums_index:
        if (iy + 1, ix - 1) in adjecent_nums_index:
            adjecent_nums_index.remove((iy + 1, ix - 1))
        if (iy + 1, ix + 1) in adjecent_nums_index:
            adjecent_nums_index.remove((iy + 1, ix + 1))
    return adjecent_nums_index


def get_adjecent_nums_product(indices, matrix):
    product = 1
    for index in indices:
        num = str(matrix[index])

        iy = index[0]
        original_ix = index[1]

        ix = original_ix
        # Check nums to the left
        while ix > 0:
            ix -= 1

            if matrix[iy, ix].isdigit():
                num = matrix[iy, ix] + num
            else:
                break

        ix = original_ix
        while ix < (matrix.shape[1] - 1):
            ix += 1

            if matrix[iy, ix].isdigit():
                num += matrix[iy, ix]
            else:
                break
        product *= int(num)
    return product


def get_adjecent_nums_index(iy, ix, matrix):
    adjecent_nums_index = []
    if iy > 0:

        if ix > 0:  # Top left corner

            if matrix[iy - 1, ix - 1].isdigit():
                adjecent_nums_index.append((iy - 1, ix - 1))

        # Directly above
        if matrix[iy - 1, ix].isdigit():
            adjecent_nums_index.append((iy - 1, ix))

        if ix < (matrix.shape[1] - 2):  # Top right corner
            if matrix[iy - 1, ix + 1].isdigit():
                adjecent_nums_index.append((iy - 1, ix + 1))

    if iy < (matrix.shape[0] - 1):

        if ix > 0:  # Bottom left corner
            if matrix[iy + 1, ix - 1].isdigit():
                adjecent_nums_index.append((iy + 1, ix - 1))

        # Directly below
        if matrix[iy + 1, ix].isdigit():
            adjecent_nums_index.append((iy + 1, ix))

        if ix < (matrix.shape[1] - 1):  # Bottom right corner
            if matrix[iy + 1, ix + 1].isdigit():
                adjecent_nums_index.append((iy + 1, ix + 1))

    if ix > 0:  # Directly to the left
        if matrix[iy, ix - 1].isdigit():
            adjecent_nums_index.append((iy, ix - 1))

    if ix < (matrix.shape[1] - 1):  # Directly to the right
        if matrix[iy, ix + 1].isdigit():
            adjecent_nums_index.append((iy, ix + 1))

    adjecent_nums_index = remove_duplicate_indices(iy, ix, adjecent_nums_index)

    return len(adjecent_nums_index) == 2, adjecent_nums_index


def part_two_solution():
    sum = 0
    matrix = []
    for line in open("./3/input.txt").readlines():
        matrix.append([*line])

    np_matrix = np.array(matrix)

    for iy in range(0, np_matrix.shape[0]):

        for ix in range(0, np_matrix.shape[1]):
            current_char = np_matrix[iy, ix]

            if current_char == "*":

                has_exactly_two_num_neigbours, adjecent_nums_index = get_adjecent_nums_index(
                    iy, ix, np_matrix)
                if has_exactly_two_num_neigbours:
                    gear_ratio = get_adjecent_nums_product(
                        adjecent_nums_index, np_matrix)
                    sum += gear_ratio

    print(sum)


part_two_solution()
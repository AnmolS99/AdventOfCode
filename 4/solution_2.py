import numpy as np


def count_all_xmas(char_array):
    
    count = 0

    rows, cols = char_array.shape

    for i in range(rows - 2):

        for j in range(cols - 2):

            diag = ''.join(char for char in char_array[[i, i + 1, i + 2], [j, j + 1, j + 2]])
            anti_diag = ''.join(char for char in char_array[[i, i + 1, i + 2], [j + 2, j + 1, j]])

            if (diag == "MAS" or diag == "SAM") and (anti_diag == "MAS" or anti_diag == "SAM"):
                count += 1

    return count


content = np.loadtxt("4/input.txt", dtype=str)

char_array = np.char.asarray(content).view("U1").reshape(len(content), -1)

print(count_all_xmas(char_array))
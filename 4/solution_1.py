import numpy as np


def count_all_xmas(char_array):
    return count_xmas_horizontal(char_array) + count_xmas_vertically(char_array) + count_xmas_diagonally(char_array)

def count_xmas_horizontal(char_array):
    
    count = 0

    for line in char_array:

        for i in range(len(line)):

            if i > 2 and (''.join(char for char in line[i-3 : i+1]) == "XMAS" or ''.join(char for char in line[i-3 : i+1]) == "SAMX"):
                count += 1

    return count

def count_xmas_vertically(char_array):

    char_array = np.rot90(char_array)

    count = 0

    for line in char_array:

        for i in range(len(line)):

            if i > 2 and (''.join(char for char in line[i-3 : i+1]) == "XMAS" or ''.join(char for char in line[i-3 : i+1]) == "SAMX"):
                count += 1


    return count

def count_xmas_diagonally(char_array):

    count = 0
    
    for _ in range(4):
            
        char_array = np.rot90(char_array)
        
        for d in range(-char_array.shape[0] + 1, char_array.shape[0]): 

            diag_char_array = np.diagonal(char_array, offset=d)

            for i in range(len(diag_char_array)):

                if i > 2 and ''.join(char for char in diag_char_array[i-3 : i+1]) == "XMAS":
                    count += 1

    return count


content = np.loadtxt("4/input.txt", dtype=str)

char_array = np.char.asarray(content).view("U1").reshape(len(content), -1)

print(count_all_xmas(char_array))
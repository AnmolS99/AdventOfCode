import numpy as np

content = np.loadtxt("6/input.txt", comments='$', dtype=str)

char_array = np.char.asarray(content).view("U1").reshape(len(content), -1)

guard_x, guard_y = np.where((char_array == '^') | (char_array == '>') | (char_array == 'v') | (char_array == '<'))

guard_pos = (guard_x[0], guard_y[0])

map_num_rows, map_num_cols = char_array.shape

def rotate_guard_direction(guard_sign):
    match guard_sign:
        case '^':
            return '>'
        case 'v':
            return '<'
        case '<':
            return '^'
        case '>':
            return 'v'

def get_next_pos(guard_pos, guard_sign):
    match guard_sign:
        case '^':
            return guard_pos[0] - 1, guard_pos[1]
        case 'v':
            return guard_pos[0] + 1, guard_pos[1]
        case '<':
            return guard_pos[0], guard_pos[1] - 1
        case '>':
            return guard_pos[0], guard_pos[1] + 1


def is_guard_route_loop(char_array, guard_pos, guard_sign):

    prev_states = set()
    
    while True: 

        next_pos = get_next_pos(guard_pos, char_array[guard_pos])

        if next_pos[0] < 0 or next_pos[0] >= map_num_rows or next_pos[1] < 0 or next_pos[1] >= map_num_cols:
            char_array[guard_pos] = 'X'
            return False

        if char_array[next_pos] == '#':
            char_array[guard_pos] = rotate_guard_direction(char_array[guard_pos])
            
            if (next_pos, char_array[guard_pos]) in prev_states:
                return True
            
            prev_states.add((guard_pos, guard_sign))
            continue

        guard_sign = char_array[guard_pos]

        char_array[guard_pos] = 'X'

        char_array[next_pos] = guard_sign

        guard_pos = next_pos

        if (guard_pos, guard_sign) in prev_states:
            return True

        prev_states.add((guard_pos, guard_sign))

count_loops = 0

for i in range(char_array.shape[0]):
    print(f"Row {i}/{map_num_rows}")
    for j in range(char_array.shape[1]):

        if char_array[i][j] == '.':
            
            arr_copy = char_array.copy()
            arr_copy[i][j] = '#'

            if is_guard_route_loop(arr_copy, guard_pos, char_array[guard_pos]):
                count_loops += 1

print(f"Number of ways to get loops: {count_loops}")
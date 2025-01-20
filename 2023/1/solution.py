int_words = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}


def convert_string_num_to_int(input_string: str):
    for k, v in int_words.items():
        input_string = input_string.replace(k, str(v))
    return input_string


def solution1():

    sum = 0
    for line in open("./1/input.txt").readlines():
        line = convert_string_num_to_int(line)
        first_digit = None
        last_digit = None
        for character in line:
            if character.isdigit():
                first_digit = character
                break
        for character in reversed(line):
            if character.isdigit():
                last_digit = character
                break
        full_num = int(first_digit + last_digit)
        sum += full_num

    print(sum)


def get_first_digit(line, reverse: bool = False):
    if reverse:
        line = line[::-1]

    for i in range(len(line)):
        if line[i].isdigit():
            return line[i]

        for k, v in int_words.items():

            if reverse:
                k = k[::-1]

            if k in line[:i + 1]:
                return str(v)


def solution2():

    sum = 0
    for line in open("./1/input.txt").readlines():
        first_digit = None
        last_digit = None

        first_digit = get_first_digit(line)
        last_digit = get_first_digit(line, True)

        full_num = int(first_digit + last_digit)
        sum += full_num

    print(sum)


solution2()
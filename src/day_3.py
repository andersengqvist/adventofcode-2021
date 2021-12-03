
from lib.files import read_lines


def part1():
    the_input = read_lines("res/day_3_1.txt")
    res = get_gamma_and_epsilon(the_input)
    print("Day 2.1: {}".format(res[0] * res[1]))


def part2():
    the_input = read_lines("res/day_3_1.txt")
    oxygen = oxygen_generator_rating(the_input)
    co2 = co2_scrubber_rating(the_input)
    print("Day 2.2: {}".format(oxygen * co2))


def get_binaries_at_index(the_list, idx):
    ones = 0
    for w in the_list:
        if w[idx] == "1":
            ones += 1
    if ones >= len(the_list) / 2:
        return "1", "0"
    else:
        return "0", "1"


def get_gamma_and_epsilon(the_list):
    gamma = ""
    epsilon = ""
    digits = len(the_list[0])
    for i in range(digits):
        ge = get_binaries_at_index(the_list, i)
        gamma += ge[0]
        epsilon += ge[1]
    return int(gamma, 2), int(epsilon, 2)


def filter_list(the_list, the_char, idx):
    return [item for item in the_list if item[idx] == the_char]


def oxygen_generator_rating(the_list):
    digits = len(the_list[0])
    idx = 0
    my_list = the_list
    while len(my_list) > 1 and idx < digits:
        ge = get_binaries_at_index(my_list, idx)
        my_list = filter_list(my_list, ge[0], idx)
        idx += 1
    return int(my_list[0], 2)


def co2_scrubber_rating(the_list):
    digits = len(the_list[0])
    idx = 0
    my_list = the_list
    while len(my_list) > 1 and idx < digits:
        ge = get_binaries_at_index(my_list, idx)
        my_list = filter_list(my_list, ge[1], idx)
        idx += 1
    return int(my_list[0], 2)


if __name__ == "__main__":
    part1()
    part2()

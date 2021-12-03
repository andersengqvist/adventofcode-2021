from lib.files import read_lines


def part1():
    the_input = [int(line) for line in read_lines("res/day_1_1.txt")]
    res = count_number_of_times_a_depth_measurement_increases(the_input)
    print("Day 1.1: {}".format(res))


def part2():
    the_input = [int(line) for line in read_lines("res/day_1_1.txt")]
    res = count_number_of_times_a_depth_measurement_increases_with_sliding_window(the_input)
    print("Day 1.2: {}".format(res))


def count_number_of_times_a_depth_measurement_increases_with_sliding_window(the_list):
    res = []
    for i in range(len(the_list) - 2):
        res.append(the_list[i] + the_list[i+1] + the_list[i+2])
    return count_number_of_times_a_depth_measurement_increases(res)


def count_number_of_times_a_depth_measurement_increases(the_list):
    curr = the_list[0]
    res = 0
    for val in the_list:
        if val > curr:
            res += 1
        curr = val
    return res


if __name__ == "__main__":
    part1()
    part2()

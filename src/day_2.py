import functools

from lib.files import read_lines


def part1():
    the_input = read_lines("res/day_2_1.txt")
    res = get_position_part_1(the_input)
    print("Day 2.1: {}".format(res[0] * res[1]))


def part2():
    the_input = read_lines("res/day_2_1.txt")
    res = get_position_part_2(the_input)
    print("Day 2.2: {}".format(res[0] * res[1]))


# return the instruction in a tuple (horizontal movement, vertical movement)
# Or, for part 2: (horizontal movement, aim movement)
def parse_instruction(line):
    splitted = line.split()
    direction = splitted[0]
    value = int(splitted[1])
    if direction == "forward":
        return value, 0
    if direction == "down":
        return 0, value
    if direction == "up":
        return 0, -value


def get_position_part_1(the_list):
    instructions = (parse_instruction(line) for line in the_list)
    return functools.reduce(lambda t1, t2: (t1[0] + t2[0], t1[1] + t2[1]), instructions)


def get_position_part_2(the_list):
    instructions = (parse_instruction(line) for line in the_list)
    aim = 0
    horizontal_pos = 0
    vertical_pos = 0
    for instruction in instructions:
        aim += instruction[1]
        horizontal_pos += instruction[0]
        vertical_pos += aim * instruction[0]
    return horizontal_pos, vertical_pos


if __name__ == "__main__":
    part1()
    part2()

from lib.files import read_lines
from collections import Counter


def part1():
    the_input = read_lines("res/day_9_1.txt")
    the_map = parse_map(the_input)
    res = sum_risk_levels(the_map)
    print("Day 9.1: {}".format(res))


def part2():
    the_input = read_lines("res/day_9_1.txt")
    the_map = parse_map(the_input)
    color_map = create_color_map(the_map)
    res = get_three_largest_basins_product(color_map)
    print("Day 9.2: {}".format(res))


def parse_map(the_input):
    return [parse_row(line) for line in the_input]


def parse_row(line):
    return [int(c.strip()) for c in line if c.strip()]


def sum_risk_levels(the_map):
    res = 0
    for row in range(len(the_map)):
        for col in range(len(the_map[row])):
            if is_low_point_at(the_map, row, col):
                res += the_map[row][col] + 1
    return res


def is_low_point_at(the_map, row, col):
    if row > 0 and the_map[row][col] >= the_map[row - 1][col]:
        return False
    if row < len(the_map) - 1 and the_map[row][col] >= the_map[row + 1][col]:
        return False
    if col > 0 and the_map[row][col] >= the_map[row][col - 1]:
        return False
    if col < len(the_map[row]) - 1 and the_map[row][col] >= the_map[row][col + 1]:
        return False
    return True


def create_color_map(the_map):
    color_map = [None] * len(the_map)
    color = 1
    for row in range(len(the_map)):
        color_map[row] = [None] * len(the_map[row])
        for col in range(len(the_map[row])):
            if is_low_point_at(the_map, row, col):
                color_map[row][col] = color
                color += 1
            if the_map[row][col] == 9:
                color_map[row][col] = -1
    while not is_colored(color_map):
        for row in range(len(the_map)):
            for col in range(len(the_map[row])):
                if color_map[row][col] is None:
                    color = get_color_at(color_map, row, col)
                    if color is not None:
                        color_map[row][col] = color
    return color_map


def is_colored(color_map):
    for row in range(len(color_map)):
        for col in range(len(color_map[row])):
            if color_map[row][col] is None:
                return False
    return True


def get_color_at(color_map, row, col):
    if row > 0 and color_map[row - 1][col] is not None and color_map[row - 1][col] > 0:
        return color_map[row - 1][col]
    if row < len(color_map) - 1 and color_map[row + 1][col] is not None and color_map[row + 1][col] > 0:
        return color_map[row + 1][col]
    if col > 0 and color_map[row][col - 1] is not None and color_map[row][col - 1] > 0:
        return color_map[row][col - 1]
    if col < len(color_map[row]) - 1 and color_map[row][col + 1] is not None and color_map[row][col + 1] > 0:
        return color_map[row][col + 1]
    return None


def get_three_largest_basins_product(color_map):
    counter = Counter()
    for row in range(len(color_map)):
        for col in range(len(color_map[row])):
            if color_map[row][col] is not None and color_map[row][col] > 0:
                val = color_map[row][col]
                counter[val] += 1
    biggest = counter.most_common(3)
    return biggest[0][1] * biggest[1][1] * biggest[2][1]


if __name__ == "__main__":
    part1()
    part2()

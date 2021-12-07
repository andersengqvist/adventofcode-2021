from lib.files import read_file


def part1():
    the_input = [int(crab) for crab in read_file("res/day_7_1.txt").split(",")]
    res = get_min_fuel_consumption_part_1(the_input)
    print("Day 1.1: {}".format(res))


def part2():
    the_input = [int(crab) for crab in read_file("res/day_7_1.txt").split(",")]
    res = get_min_fuel_consumption_part_2(the_input)
    print("Day 1.2: {}".format(res))


def get_min_fuel_consumption_part_1(crab_fleet):
    return get_min_fuel_consumption(crab_fleet, calculate_linear_fuel_consumption_for_crab)


def get_min_fuel_consumption_part_2(crab_fleet):
    return get_min_fuel_consumption(crab_fleet, calculate_increasing_fuel_consumption_for_crab)


def get_min_fuel_consumption(crab_fleet, consumption_for_crab_function):
    return min(gen_fuel_consumption(crab_fleet, consumption_for_crab_function))


def gen_fuel_consumption(crab_fleet, consumption_for_crab_function):
    (min_d, max_d) = get_stats(crab_fleet)
    for i in range(min_d, max_d + 1):
        yield calculate_fuel_consumption_for_fleet(crab_fleet, i, consumption_for_crab_function)


def get_stats(crab_fleet):
    return min(crab_fleet), max(crab_fleet)


def calculate_fuel_consumption_for_fleet(crab_fleet, depth, consumption_for_crab_function):
    res = 0
    for crab in crab_fleet:
        res += consumption_for_crab_function(crab, depth)
    return res


def calculate_linear_fuel_consumption_for_crab(the_crab, depth):
    return abs(the_crab - depth)


def calculate_increasing_fuel_consumption_for_crab(the_crab, depth):
    n = abs(the_crab - depth)
    return int(((n + 1) * n) / 2)


if __name__ == "__main__":
    part1()
    part2()

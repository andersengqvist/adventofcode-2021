from functools import reduce

from lib.files import read_lines
from collections import Counter


def part1():
    the_input = [line for line in read_lines("res/day_5_1.txt")]
    res = get_overlap_part_1(the_input)
    print("Day 5.1: {}".format(res))


def part2():
    the_input = [line for line in read_lines("res/day_5_1.txt")]
    res = get_overlap_part_2(the_input)
    print("Day 5.2: {}".format(res))


class Point:

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def x(self):
        return self._x

    def y(self):
        return self._y

    def __eq__(self, other):
        if isinstance(other, Point):
            return self._x == other.x() and self._y == other.y()
        return False

    def __hash__(self):
        return 7 * hash(self._x) + 17 * hash(self._y)

    def __repr__(self):
        return "Point({}, {})".format(self._x, self._y)

    def __str__(self):
        return "[{}, {}]".format(self._x, self._y)


def parse_points(line):
    points = line.split(" -> ")
    first = points[0].split(",")
    second = points[1].split(",")
    return int(first[0]), int(first[1]), int(second[0]), int(second[1])


def gen(n1, n2):
    num = n1
    if n1 < n2:
        while num <= n2:
            yield num
            num += 1
    else:
        if n1 > n2:
            while num >= n2:
                yield num
                num -= 1
        else:
            while True:
                yield num


def build_line(x1, y1, x2, y2):
    res = []
    for dx, dy in zip(gen(x1, x2), gen(y1, y2)):
        res.append(Point(dx, dy))
    return res


def count_overlapping(lines):
    flattened = [point for line in lines for point in line]
    counter = Counter(flattened)
    return reduce(lambda acc, value: acc + 1 if value > 1 else acc, counter.values(), 0)


def get_overlap_part_1(lines):
    parsed_coordinates = [parse_points(line) for line in lines if line.strip()]
    lines = [build_line(tup[0], tup[1], tup[2], tup[3]) for tup in parsed_coordinates if tup[0] == tup[2] or tup[1] == tup[3] ]
    return count_overlapping(lines)


def get_overlap_part_2(lines):
    parsed_coordinates = [parse_points(line) for line in lines if line.strip()]
    lines = [build_line(tup[0], tup[1], tup[2], tup[3]) for tup in parsed_coordinates]
    return count_overlapping(lines)


if __name__ == "__main__":
    part1()
    part2()

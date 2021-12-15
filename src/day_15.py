from lib.files import read_lines
from lib.queue import PriorityQueue
from collections import namedtuple

Point = namedtuple('Point', 'x y')


def part1():
    the_input = read_lines("res/day_15_1.txt")
    the_map = build_map(the_input)
    res = find_least_cost(the_map, Point(0, 0), Point(len(the_map[0]) - 1, len(the_map) - 1))
    print("Day 15.1: {}".format(res.f()))


def part2():
    the_input = read_lines("res/day_15_1.txt")
    the_map = build_mega_map(the_input)
    res = find_least_cost(the_map, Point(0, 0), Point(len(the_map[0]) - 1, len(the_map) - 1))
    print("Day 15.2: {}".format(res.f()))


def build_map(the_input):
    return [build_line(line.strip()) for line in the_input if line.strip()]


def build_line(the_line):
    return [int(char) for char in the_line]


def build_mega_map(the_input):
    the_map = build_map(the_input)
    mega_map = [[0 for _x in range(len(the_map[0]) * 5)] for _y in range(len(the_map) * 5)]

    for mega_y in range(5):
        for mega_x in range(5):
            for y in range(len(the_map)):
                for x in range(len(the_map[y])):
                    val = the_map[y][x] + mega_y + mega_x
                    if val >= 10:
                        val = val - 9
                    mega_map[mega_y * len(the_map) + y][mega_x * len(the_map[y]) + x] = val
    return mega_map


def print_map(the_map):
    for y in range(len(the_map)):
        for x in range(len(the_map[y])):
            print(str(the_map[y][x]), end="")
        print("")


# point = tuple (x, y)
# g = movement cost to the pos
# h = estimated cost to goal
# f = total cost
class Pos:
    def __init__(self, point, g, h):
        self._point = point
        self._g = g
        self._h = h

    def point(self):
        return self._point

    def g(self):
        return self._g

    def h(self):
        return self._h

    def f(self):
        return self._g + self._h

    def __repr__(self):
        return "{}, g: {}, h: {}, f: {}".format(self.point(), self.g(), self.h(), self.f())

    def __eq__(self, other):
        if isinstance(other, Pos):
            return self._point == other.point()
        return False

    def __hash__(self):
        return hash(self._point.x) + 13 * hash(self._point.y)

    def __lt__(self, other):
        if isinstance(other, Pos):
            return self.f() < other.f()
        return False


def estimate_cost(p1, p2):
    return abs(p1.x - p2.x) + abs(p1.y - p2.y)


def find_neighbours(the_map, point):
    res = []
    if point.y > 0:
        res.append(Point(point.x, point.y - 1))
    if point.y < len(the_map) - 1:
        res.append(Point(point.x, point.y + 1))
    if point.x > 0:
        res.append(Point(point.x - 1, point.y))
    if point.x < len(the_map[point.y]) - 1:
        res.append(Point(point.x + 1, point.y))
    return res


def find_least_cost(the_map, begin, end):
    inspect = PriorityQueue()
    finished = dict()
    init_pos = Pos(begin, 0, estimate_cost(begin, end))
    inspect.push(init_pos.f(), init_pos)
    while inspect:
        pos = inspect.pop()
        if pos.point() == end:
            return pos
        finished[pos.point()] = pos
        neighbours = find_neighbours(the_map, pos.point())
        for neighbour in neighbours:
            npos = Pos(neighbour, pos.g() + the_map[neighbour.y][neighbour.x], estimate_cost(neighbour, end))
            add_neigh = True
            ins = inspect.get(npos)
            if ins is not None:
                add_neigh = False
                if npos.f() < ins.f():
                    inspect.update_priority(npos.f(), npos)
            ins = finished.get(neighbour, None)
            if ins is not None and ins.f() <= npos.f():
                add_neigh = False
            if add_neigh:
                inspect.push(npos.f(), npos)
    return None


if __name__ == "__main__":
    part1()
    part2()

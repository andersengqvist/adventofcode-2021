from lib.files import read_lines
from collections import namedtuple
import re


def part1():
    the_input = read_lines("res/day_22_1.txt")
    instructions = parse_input(the_input)
    reactor = run_reboot_steps(instructions)
    reactor.intersection(Cube(-50, 50, -50, 50, -50, 50))
    res = reactor.size()
    print("Day 22.1: {}".format(res))


def part2():
    the_input = read_lines("res/day_22_1.txt")
    instructions = parse_input(the_input)
    reactor = run_reboot_steps(instructions)
    res = reactor.size()
    print("Day 22.2: {}".format(res))


Coordinate = namedtuple('Coordinate', 'x y z')


class Cube:
    def __init__(self, x_min, x_max,  y_min, y_max, z_min, z_max):
        self._x_min = x_min
        self._x_max = x_max
        self._y_min = y_min
        self._y_max = y_max
        self._z_min = z_min
        self._z_max = z_max

    def x_min(self):
        return self._x_min

    def x_max(self):
        return self._x_max

    def y_min(self):
        return self._y_min

    def y_max(self):
        return self._y_max

    def z_min(self):
        return self._z_min

    def z_max(self):
        return self._z_max

    def len_x(self):
        return self._x_max - self._x_min + 1

    def len_y(self):
        return self._y_max - self._y_min + 1

    def len_z(self):
        return self._z_max - self._z_min + 1

    def size(self):
        return self.len_x() * self.len_y() * self.len_z()

    def overlaps(self, cube):
        return self._x_min <= cube.x_max() and self._x_max >= cube.x_min()\
               and self._y_min <= cube.y_max() and self._y_max >= cube.y_min()\
               and self._z_min <= cube.z_max() and self._z_max >= cube.z_min()

    def encloses(self, cube):
        return self._x_min <= cube.x_min() and self._x_max >= cube.x_max()\
               and self._y_min <= cube.y_min() and self._y_max >= cube.y_max()\
               and self._z_min <= cube.z_min() and self._z_max >= cube.z_max()

    def intersection(self, cube):
        if not self.overlaps(cube):
            return []
        return [Cube(
            max(self._x_min, cube.x_min()),
            min(self._x_max, cube.x_max()),
            max(self._y_min, cube.y_min()),
            min(self._y_max, cube.y_max()),
            max(self._z_min, cube.z_min()),
            min(self._z_max, cube.z_max()))]

    def remove(self, cube):
        if not self.overlaps(cube):
            return [self]
        elif cube.encloses(self):
            return []
        else:
            return self._split(cube)

    def _split(self, cube):
        (x_min, x_max, y_min, y_max, z_min, z_max) =\
            self._x_min, self._x_max, self._y_min, self._y_max, self._z_min, self._z_max
        res = []
        if x_min < cube.x_min():
            res.append(Cube(x_min, cube.x_min() - 1, y_min, y_max, z_min, z_max))
            x_min = cube.x_min()
        if x_max > cube.x_max():
            res.append(Cube(cube.x_max() + 1, x_max, y_min, y_max, z_min, z_max))
            x_max = cube.x_max()
        if y_min < cube.y_min():
            res.append(Cube(x_min, x_max, y_min, cube.y_min() - 1, z_min, z_max))
            y_min = cube.y_min()
        if y_max > cube.y_max():
            res.append(Cube(x_min, x_max, cube.y_max() + 1, y_max, z_min, z_max))
            y_max = cube.y_max()
        if z_min < cube.z_min():
            res.append(Cube(x_min, x_max, y_min, y_max, z_min, cube.z_min() - 1))
        if z_max > cube.z_max():
            res.append(Cube(x_min, x_max, y_min, y_max, cube.z_max() + 1, z_max))
        return res

    def __repr__(self):
        return "[x: {}, {} y: {}, {} z: {}, {}]".format(
            self._x_min, self._x_max, self._y_min, self._y_max, self._z_min, self._z_max)


class Reactor:
    def __init__(self):
        self._cubes = []

    def on(self, cube):
        cubes = []
        for coob in self._cubes:
            cubes.extend(coob.remove(cube))
        cubes.append(cube)
        self._cubes = cubes

    def off(self, cube):
        cubes = []
        for coob in self._cubes:
            cubes.extend(coob.remove(cube))
        self._cubes = cubes

    def intersection(self, cube):
        cubes = []
        for coob in self._cubes:
            cubes.extend(coob.intersection(cube))
        self._cubes = cubes

    def size(self):
        res = 0
        for coob in self._cubes:
            res += coob.size()
        return res

    def __repr__(self):
        return str(self._cubes)


RebootStep = namedtuple('RebootStep', 'op x_min x_max  y_min y_max z_min z_max')


def parse_input(the_input):
    pattern = "([a-z]+)\\s*x=(-?\\d+)\\.\\.(-?\\d+),y=(-?\\d+)\\.\\.(-?\\d+),z=(-?\\d+)\\.\\.(-?\\d+)"
    prog = re.compile(pattern)
    result = []
    for line in the_input:
        match = prog.match(line.strip())
        if match:
            rs = RebootStep(
                match.group(1),
                int(match.group(2)),
                int(match.group(3)),
                int(match.group(4)),
                int(match.group(5)),
                int(match.group(6)),
                int(match.group(7))
            )
            result.append(rs)
        else:
            raise AssertionError("Failed to parse line: {}".format(line))
    return result


def run_reboot_steps(steps):
    reactor = Reactor()
    for step in steps:
        run_reboot_step(reactor, step)
    return reactor


def run_reboot_step(reactor, step):
    if step.op == "on":
        reactor.on(Cube(step.x_min, step.x_max, step.y_min, step.y_max, step.z_min, step.z_max))
    else:
        reactor.off(Cube(step.x_min, step.x_max, step.y_min, step.y_max, step.z_min, step.z_max))


if __name__ == "__main__":
    part1()
    part2()

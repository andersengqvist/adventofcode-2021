
def part1():
    target = Target(85, 145, -163, -108)
    res = find_highest_y(target)
    print("Day 17.1: {}".format(res))


def part2():
    target = Target(85, 145, -163, -108)
    res = count_hits(target)
    print("Day 17.2: {}".format(res))


class Target:
    def __init__(self, x_1, x_2, y_1, y_2):
        self._x_min = min(x_1, x_2)
        self._x_max = max(x_1, x_2)
        self._y_min = min(y_1, y_2)
        self._y_max = max(y_1, y_2)

    def x_max(self):
        return self._x_max

    def x_min(self):
        return self._x_min

    def y_min(self):
        return self._y_min

    def is_hit(self, x, y):
        return self._x_min <= x <= self._x_max and self._y_min <= y <= self._y_max

    def is_miss(self, x, y):
        return x > self._x_max or y <= self._y_min


def sum_ints(n):
    return int(((n + 1) * n) / 2)


def max_x_velocity(target):
    return target.x_max()


def min_x_velocity(target):
    n = 0
    while sum_ints(n) < target.x_min():
        n += 1
    return n


def max_y_velocity(target):
    return - 1 - target.y_min()


def min_y_velocity(target):
    return target.y_min()


def find_highest_y(target):
    n = max_y_velocity(target)
    return sum_ints(n)


def hits_target(target, x_velocity, y_velocity):
    dx = x_velocity
    dy = y_velocity
    x = 0
    y = 0
    while True:
        x += dx
        y += dy
        if dx > 0:
            dx -= 1
        dy -= 1
        if target.is_hit(x, y):
            return True
        elif target.is_miss(x, y):
            return False


def count_hits(target):
    xmin = min_x_velocity(target)
    xmax = max_x_velocity(target)
    ymin = min_y_velocity(target)
    ymax = max_y_velocity(target)
    hits = 0
    for x in range(xmin, xmax + 1):
        for y in range(ymin, ymax + 1):
            if hits_target(target, x, y):
                hits += 1
    return hits


if __name__ == "__main__":
    part1()
    part2()

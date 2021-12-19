import math
import functools
import copy

from lib.files import read_lines


def part1():
    the_input = read_lines("res/day_18_1.txt")
    sfs = parse_snailfish_numbers(the_input)
    sf = add_snailfish_number_list(sfs)
    print("Day 18.1: {}".format(sf.magnitude()))


def part2():
    the_input = read_lines("res/day_18_1.txt")
    sfs = parse_snailfish_numbers(the_input)
    res = find_max_magnitude(sfs)
    print("Day 18.2: {}".format(res))


class SnailfishNumber:
    def __init__(self, left, right, the_parent=None):
        self._left = left
        self._right = right
        self._parent = the_parent
        if isinstance(self._left, SnailfishNumber):
            self._left.parent(self)
        if isinstance(self._right, SnailfishNumber):
            self._right.parent(self)

    def parent(self, the_parent):
        self._parent = the_parent

    def left(self):
        return self._left

    def right(self):
        return self._right

    def __repr__(self):
        return "[{},{}]".format(self._left, self._right)

    def __add__(self, other):
        return SnailfishNumber(copy.deepcopy(self), copy.deepcopy(other))

    def __deepcopy__(self, memo=None):
        if memo is None:
            memo = {}
        id_self = id(self)
        _copy = memo.get(id_self)
        if _copy is None:
            _copy = SnailfishNumber(copy.deepcopy(self._left, memo), copy.deepcopy(self._right, memo))
            memo[id_self] = _copy
        return _copy

    def magnitude(self):
        ln = self._left if isinstance(self._left, int) else self._left.magnitude()
        rn = self._right if isinstance(self._right, int) else self._right.magnitude()
        return 3 * ln + 2 * rn

    def reduce(self):
        while True:
            while True:
                (result, p) = self.do_explode(0)
                if result == 0:
                    break
            if not self.do_split():
                return

    def do_explode(self, level):
        is_leaf = True
        if isinstance(self._left, SnailfishNumber):
            is_leaf = False
            (result, p) = self._left.do_explode(level + 1)
            if result == 2:
                self._left = 0
                self._move_right(p[1])
                return 3, (p[0], 0)
            elif result == 3:
                self._move_right(p[1])
                return 3, (p[0], 0)
        if isinstance(self._right, SnailfishNumber):
            is_leaf = False
            (result, p) = self._right.do_explode(level + 1)
            if result == 2:
                self._right = 0
                self._move_left(p[0])
                return 3, (0, p[1])
            elif result == 3:
                self._move_left(p[0])
                return 3, (0, p[1])
        if is_leaf and level >= 4:
            return 2, (self._left, self._right)
        return 0, None

    def do_split(self):
        if isinstance(self._left, int) and self._left >= 10:
            self._left = self._split(self._left)
            return True
        elif isinstance(self._left, SnailfishNumber) and self._left.do_split():
            return True
        if isinstance(self._right, int) and self._right >= 10:
            self._right = self._split(self._right)
            return True
        elif isinstance(self._right, SnailfishNumber) and self._right.do_split():
            return True
        return False

    def _split(self, number):
        half = number / 2
        return SnailfishNumber(math.floor(half), math.ceil(half), self)

    def _move_right(self, number):
        if number != 0:
            if isinstance(self._right, SnailfishNumber):
                self._right.add_left(number)
            else:
                self._right += number

    def _move_left(self, number):
        if number != 0:
            if isinstance(self._left, SnailfishNumber):
                self._left.add_right(number)
            else:
                self._left += number

    def add_left(self, number):
        if isinstance(self._left, SnailfishNumber):
            self._left.add_left(number)
        else:
            self._left += number

    def add_right(self, number):
        if isinstance(self._right, SnailfishNumber):
            self._right.add_right(number)
        else:
            self._right += number


def parse_half_pair(the_str, the_idx):
    idx = the_idx
    if the_str[idx] == "[":
        return parse_snailfish_number(the_str, idx)
    elif the_str[idx].isnumeric():
        idx2 = idx + 1
        while the_str[idx2].isnumeric():
            idx2 += 1
        number = int(the_str[idx:idx2])
        idx = idx2
        return number, idx
    else:
        raise AssertionError


def parse_snailfish_number(the_str, the_idx):
    idx = the_idx + 1
    (left, idx) = parse_half_pair(the_str, idx)
    idx += 1
    (right, idx) = parse_half_pair(the_str, idx)
    return SnailfishNumber(left, right), idx + 1


def parse_snailfish_numbers(the_input):
    return [parse_snailfish_number(line.strip(), 0)[0] for line in the_input if line.strip()]


def add_snailfish_numbers(left, right):
    sf = left + right
    sf.reduce()
    return sf


def add_snailfish_number_list(the_list):
    return functools.reduce(add_snailfish_numbers, the_list)


def find_max_magnitude(the_list):
    max_mag = 0
    for i in range(len(the_list) - 1):
        for j in range(i + 1, len(the_list)):
            sf = add_snailfish_numbers(the_list[i], the_list[j])
            m = sf.magnitude()
            if m > max_mag:
                max_mag = m
            sf = add_snailfish_numbers(the_list[j], the_list[i])
            m = sf.magnitude()
            if m > max_mag:
                max_mag = m
    return max_mag


if __name__ == "__main__":
    part1()
    part2()

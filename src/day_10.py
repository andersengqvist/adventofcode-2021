from lib.files import read_lines
from collections import deque


def part1():
    the_input = read_lines("res/day_10_1.txt")
    res = get_total_syntax_error(the_input)
    print("Day 10.1: {}".format(res))


def part2():
    the_input = read_lines("res/day_10_1.txt")
    res = get_middle_score(the_input)
    print("Day 10.2: {}".format(res))


class Line:

    def __init__(self, input):
        self._input = input
        self._first_invalid = None
        self._to_complete = None
        self._parse()

    def _parse(self):
        stack = deque()
        for ch in self._input:
            if is_opening(ch):
                stack.append(ch)
            elif is_closing(ch):
                op = stack.pop()
                if not is_valid_chunk(op, ch):
                    self._first_invalid = ch
                    return
            else:
                raise Exception("Unexpected character in line: {}".format(ch))
        self._to_complete = [find_closing(ch) for ch in reversed(stack)]

    def is_corrupted(self):
        return self._first_invalid is not None

    def is_incomplete(self):
        return self._to_complete is not None and len(self._to_complete) != 0

    def get_points(self):
        if self.is_corrupted():
            if self._first_invalid == ')':
                return 3
            elif self._first_invalid == ']':
                return 57
            elif self._first_invalid == '}':
                return 1197
            elif self._first_invalid == '>':
                return 25137
            else:
                raise Exception("Unexpected invalid: {}".format(self._first_invalid))
        elif self.is_incomplete():
            score = 0
            for ch in self._to_complete:
                score *= 5
                if ch == ')':
                    score += 1
                elif ch == ']':
                    score += 2
                elif ch == '}':
                    score += 3
                elif ch == '>':
                    score += 4
                else:
                    raise Exception("Unexpected ch: {}".format(ch))
            return score
        return 0


def is_opening(ch):
    return ch == '(' or ch == '[' or ch == '{' or ch == '<'


def is_closing(ch):
    return ch == ')' or ch == ']' or ch == '}' or ch == '>'


def is_valid_chunk(right, left):
    return right == '(' and left == ')'\
           or right == '[' and left == ']'\
           or right == '{' and left == '}'\
           or right == '<' and left == '>'


def find_closing(ch):
    if ch == '(':
        return ')'
    if ch == '[':
        return ']'
    if ch == '{':
        return '}'
    if ch == '<':
        return '>'
    raise Exception("No closing for: {}".format(ch))


def get_total_syntax_error(the_input):
    lines = (Line(line) for line in the_input)
    return sum(line.get_points() for line in lines if line.is_corrupted())


def get_middle_score(the_input):
    lines = (Line(line) for line in the_input)
    sorted_points = sorted(line.get_points() for line in lines if line.is_incomplete())
    size = len(sorted_points)
    return sorted_points[int(size/2)]


if __name__ == "__main__":
    part1()
    part2()

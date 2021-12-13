from lib.files import read_file
import os


def part1():
    the_input = read_file("res/day_13_1.txt")
    res = run_part_1(the_input)
    print("Day 13.1: {}".format(res))


def part2():
    the_input = read_file("res/day_13_1.txt")
    res = run_part_2(the_input)
    print("Day 13.2:")
    res.print()


class Paper:
    def __init__(self, paper):
        self._paper = paper
        self._height = len(paper)
        self._width = len(paper[0])

    def fold_horizontal(self, at_y):
        for y in range(at_y + 1, self._height):
            for x in range(self._width):
                val = self._paper[y][x]
                if val == 1:
                    new_y = 2 * at_y - y
                    self._paper[new_y][x] = 1
                    self._paper[y][x] = 0
        self._height = at_y

    def fold_vertical(self, at_x):
        for y in range(self._height):
            for x in range(at_x + 1, self._width):
                val = self._paper[y][x]
                if val == 1:
                    new_x = 2 * at_x - x
                    self._paper[y][new_x] = 1
                    self._paper[y][x] = 0
        self._width = at_x

    def count_dots(self):
        res = 0
        for y in range(self._height):
            for x in range(self._width):
                val = self._paper[y][x]
                if val == 1:
                    res += 1
        return res

    def print(self):
        for y in range(self._height):
            for x in range(self._width):
                val = self._paper[y][x]
                if val == 0:
                    print(".", end="")
                else:
                    print("#", end="")
            print("")


def parse_input(the_input):
    chunks = the_input.split(os.linesep + os.linesep)
    paper = build_paper(chunks[0])
    instructions = build_instructions(chunks[1])
    return paper, instructions


def build_paper(the_string):
    lines = the_string.split(os.linesep)
    points = get_points(lines)
    width = max(p[0] for p in points)
    height = max(p[1] for p in points)
    paper = [[0 for _x in range(width+1)] for _y in range(height+1)]
    for point in points:
        x = point[0]
        y = point[1]
        paper[y][x] = 1
    return Paper(paper)


def get_points(lines):
    return [get_point(line) for line in lines]


def get_point(line):
    sp = line.split(",")
    return int(sp[0].strip()), int(sp[1].strip())


def build_instructions(the_string):
    lines = the_string.split(os.linesep)
    return [build_instruction(line) for line in lines if line.strip()]


def build_instruction(line):
    sp = line[11:].split("=")
    return sp[0].strip(), int(sp[1].strip())


def run_instruction(instruction, paper):
    if instruction[0] == "y":
        paper.fold_horizontal(instruction[1])
    else:
        paper.fold_vertical(instruction[1])


def run_part_1(the_input):
    (paper, instructions) = parse_input(the_input)
    run_instruction(instructions[0], paper)
    return paper.count_dots()


def run_part_2(the_input):
    (paper, instructions) = parse_input(the_input)
    for instruction in instructions:
        run_instruction(instruction, paper)
    return paper


if __name__ == "__main__":
    part1()
    part2()

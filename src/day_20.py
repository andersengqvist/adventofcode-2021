from lib.files import read_file
import os


def part1():
    the_input = read_file("res/day_20_1.txt")
    (algorithm, image) = parse_input(the_input)
    image = run_image_enhancement_algorithm(algorithm, image)
    image = run_image_enhancement_algorithm(algorithm, image)
    res = image.pixels()
    print("Day 20.1: {}".format(res))


def part2():
    the_input = read_file("res/day_20_1.txt")
    (algorithm, image) = parse_input(the_input)
    image = iterate_enhancement_algorithm(algorithm, image, 50)
    res = image.pixels()
    print("Day 20.2: {}".format(res))


class Image:
    def __init__(self, rows, cols, default_value):
        self._default = default_value
        self._img = [[default_value for _col in range(cols)] for _row in range(rows)]

    def rows(self):
        return len(self._img)

    def cols(self):
        return len(self._img[0])

    def default_value(self):
        return self._default

    def set(self, row, col, val):
        self._img[row][col] = val if val == 1 else 0

    def get(self, row, col):
        if 0 <= row < len(self._img) and 0 <= col < len(self._img[0]):
            return self._img[row][col]
        else:
            return self._default

    def pixels(self):
        res = 0
        for row in range(len(self._img)):
            for col in range(len(self._img[0])):
                res += self._img[row][col]
        return res


def parse_input(the_input):
    chunks = the_input.split(os.linesep + os.linesep)
    algorithm = build_algorithm(chunks[0])
    image = build_image(chunks[1], 0)
    return algorithm, image


def build_algorithm(the_input):
    return [1 if c == "#" else 0 for c in the_input.strip()]


def build_image(the_input, default_value):
    lines = the_input.strip().split(os.linesep)
    image = Image(len(lines), len(lines[0].strip()), default_value)
    for row in range(image.rows()):
        for col in range(image.cols()):
            if lines[row][col] == "#":
                image.set(row, col, 1)
    return image


def print_image(image):
    print("Image:")
    for row in range(image.rows()):
        for col in range(image.cols()):
            if image.get(row, col) == 1:
                print("#", end="")
            else:
                print(".", end="")
        print("")
    print("")


def iterate_enhancement_algorithm(algorithm, image, times):
    for time in range(times):
        image = run_image_enhancement_algorithm(algorithm, image)
    return image


def run_image_enhancement_algorithm(algorithm, image):
    default = image.default_value()
    if algorithm[0] == 1 and image.default_value() == 0:
        default = 1
    if algorithm[-1] == 0 and image.default_value() == 1:
        default = 0
    result = Image(image.rows() + 2, image.cols() + 2, default)
    for row in range(-1, image.rows() + 1):
        for col in range(-1, image.cols() + 1):
            val = calculate_pixel(algorithm, image, row, col)
            result.set(row + 1, col + 1, val)
    return result


def calculate_pixel(algorithm, image, the_row, the_col):
    idx = 0
    for row in range(the_row - 1, the_row + 2):
        for col in range(the_col - 1, the_col + 2):
            idx *= 2
            idx += image.get(row, col)
    return algorithm[idx]


if __name__ == "__main__":
    part1()
    part2()

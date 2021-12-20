import unittest

from src.day_20 import parse_input, print_image, run_image_enhancement_algorithm, iterate_enhancement_algorithm

the_input = """..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###
"""


class MyTestCase(unittest.TestCase):
    def test_1(self):
        (algorithm, image) = parse_input(the_input)
        print_image(image)
        self.assertEqual(10, image.pixels())
        image = run_image_enhancement_algorithm(algorithm, image)
        print_image(image)
        self.assertEqual(24, image.pixels())
        image = run_image_enhancement_algorithm(algorithm, image)
        print_image(image)
        self.assertEqual(35, image.pixels())

    def test_2(self):
        (algorithm, image) = parse_input(the_input)
        image = iterate_enhancement_algorithm(algorithm, image, 50)
        self.assertEqual(3351, image.pixels())


if __name__ == '__main__':
    unittest.main()

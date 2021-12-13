import unittest

from src.day_13 import parse_input, run_part_1

the_input = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
"""


class MyTestCase(unittest.TestCase):
    def test_parse_input(self):
        (paper, instructions) = parse_input(the_input)
        paper.fold_horizontal(7)
        self.assertEqual(17, paper.count_dots())
        paper.fold_vertical(5)
        self.assertEqual(16, paper.count_dots())

    def test_run_part_1(self):
        self.assertEqual(17, run_part_1(the_input))


if __name__ == '__main__':
    unittest.main()

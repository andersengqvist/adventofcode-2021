import unittest
import os
from src.day_5 import Point, build_line, get_overlap_part_1, get_overlap_part_2

lines = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
"""


class MyTestCase(unittest.TestCase):
    def test_build_line(self):
        self.assertEqual(
            [Point(0, 9), Point(1, 9), Point(2, 9), Point(3, 9), Point(4, 9), Point(5, 9)],
            build_line(0, 9, 5, 9)
        )
        self.assertEqual(
            [Point(8, 0), Point(7, 1), Point(6, 2), Point(5, 3), Point(4, 4), Point(3, 5), Point(2, 6), Point(1, 7), Point(0, 8)],
            build_line(8, 0, 0, 8)
        )
        self.assertEqual(
            [Point(9, 4), Point(8, 4), Point(7, 4), Point(6, 4), Point(5, 4), Point(4, 4), Point(3, 4)],
            build_line(9, 4, 3, 4)
        )
        self.assertEqual(
            [Point(2, 2), Point(2, 1)],
            build_line(2, 2, 2, 1)
        )
        self.assertEqual(
            [Point(7, 0), Point(7, 1), Point(7, 2), Point(7, 3), Point(7, 4)],
            build_line(7, 0, 7, 4)
        )

    def test_get_overlap_part_1(self):
        self.assertEqual(5, get_overlap_part_1(lines.split(os.linesep)))

    def test_get_overlap_part_2(self):
        self.assertEqual(12, get_overlap_part_2(lines.split(os.linesep)))


if __name__ == '__main__':
    unittest.main()

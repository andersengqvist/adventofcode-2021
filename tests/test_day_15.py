import unittest

from src.day_15 import Point, build_map, build_mega_map, find_least_cost

the_input = [
    "1163751742",
    "1381373672",
    "2136511328",
    "3694931569",
    "7463417111",
    "1319128137",
    "1359912421",
    "3125421639",
    "1293138521",
    "2311944581"
]


class MyTestCase(unittest.TestCase):

    def test_map(self):
        the_map = build_map(the_input)
        res = find_least_cost(the_map, Point(0, 0), Point(len(the_map[0]) - 1, len(the_map) - 1))
        self.assertEqual(40, res.f())

    def test_mega_map(self):
        the_map = build_mega_map(the_input)
        res = find_least_cost(the_map, Point(0, 0), Point(len(the_map[0]) - 1, len(the_map) - 1))
        self.assertEqual(315, res.f())


if __name__ == '__main__':
    unittest.main()

import unittest

from src.day_9 import parse_map, sum_risk_levels, create_color_map, get_three_largest_basins_product


the_input = [
    "2199943210",
    "3987894921",
    "9856789892",
    "8767896789",
    "9899965678"
]


class MyTestCase(unittest.TestCase):
    def test_part_1(self):
        the_map = parse_map(the_input)
        self.assertEqual(15, sum_risk_levels(the_map))

    def test_part_2(self):
        the_map = parse_map(the_input)
        color_map = create_color_map(the_map)
        self.assertEqual(1134, get_three_largest_basins_product(color_map))


if __name__ == '__main__':
    unittest.main()

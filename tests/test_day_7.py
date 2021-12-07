import unittest

from src.day_7 import get_min_fuel_consumption_part_1, get_min_fuel_consumption_part_2


class MyTestCase(unittest.TestCase):
    def test_get_min_fuel_consumption_part_1(self):
        self.assertEqual(37, get_min_fuel_consumption_part_1([16, 1, 2, 0, 4, 2, 7, 1, 2, 14]))

    def test_get_min_fuel_consumption_part_2(self):
        self.assertEqual(168, get_min_fuel_consumption_part_2([16, 1, 2, 0, 4, 2, 7, 1, 2, 14]))


if __name__ == '__main__':
    unittest.main()

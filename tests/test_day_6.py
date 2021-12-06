import unittest

from src.day_6 import calculate_population


class MyTestCase(unittest.TestCase):

    def test_calculate_population_at_day_18(self):
        self.assertEqual(26, calculate_population(6, [3, 4, 3, 1, 2], 18))

    def test_calculate_population_at_day_80(self):
        self.assertEqual(5934, calculate_population(6, [3, 4, 3, 1, 2], 80))

    def test_calculate_population_at_day_256(self):
        self.assertEqual(26984457539, calculate_population(6, [3, 4, 3, 1, 2], 256))


if __name__ == '__main__':
    unittest.main()

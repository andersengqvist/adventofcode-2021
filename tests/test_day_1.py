import unittest

from src.day_1 import count_number_of_times_a_depth_measurement_increases, count_number_of_times_a_depth_measurement_increases_with_sliding_window


class MyTestCase(unittest.TestCase):
    def test_count_number(self):
        self.assertEqual(7, count_number_of_times_a_depth_measurement_increases([199, 200, 208, 210, 200, 207, 240, 269, 260, 263]))

    def test_count_number_sliding(self):
        self.assertEqual(5, count_number_of_times_a_depth_measurement_increases_with_sliding_window([199, 200, 208, 210, 200, 207, 240, 269, 260, 263]))


if __name__ == '__main__':
    unittest.main()

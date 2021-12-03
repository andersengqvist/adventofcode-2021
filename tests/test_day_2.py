import unittest

from src.day_2 import get_position_part_1, get_position_part_2


class MyTestCase(unittest.TestCase):
    def test_get_position_part_1(self):
        self.assertEqual((15, 10), get_position_part_1(["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]))

    def test_get_position_part_2(self):
        self.assertEqual((15, 60), get_position_part_2(["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]))


if __name__ == '__main__':
    unittest.main()

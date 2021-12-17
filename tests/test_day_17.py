import unittest

from src.day_17 import Target, find_highest_y, hits_target, count_hits


class MyTestCase(unittest.TestCase):
    def test_find_highest_y(self):
        target = Target(20, 30, -10, -5)
        self.assertEqual(45, find_highest_y(target))

    def test_hits_target(self):
        target = Target(20, 30, -10, -5)
        self.assertTrue(hits_target(target, 7, 2))
        self.assertTrue(hits_target(target, 6, 3))
        self.assertTrue(hits_target(target, 9, 0))
        self.assertFalse(hits_target(target, 17, -4))
        self.assertTrue(hits_target(target, 6, 9))

    def test_count_hits(self):
        target = Target(20, 30, -10, -5)
        self.assertEqual(112, count_hits(target))


if __name__ == '__main__':
    unittest.main()

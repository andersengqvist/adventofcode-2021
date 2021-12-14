import unittest

from src.day_14 import solve_part


the_input = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
"""


class MyTestCase(unittest.TestCase):

    def test_run_part_1(self):
        self.assertEqual(1588, solve_part(the_input, 10))

    def test_run_part_2(self):
        self.assertEqual(2188189693529, solve_part(the_input, 40))


if __name__ == '__main__':
    unittest.main()

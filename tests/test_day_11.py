import unittest

from src.day_11 import create_octopuses, run_steps, count_flashes, calculate_sync_flashes

the_input_small = [
    "11111",
    "19991",
    "19191",
    "19991",
    "11111"
]

the_input = [
    "5483143223",
    "2745854711",
    "5264556173",
    "6141336146",
    "6357385478",
    "4167524645",
    "2176841721",
    "6882881134",
    "4846848554",
    "5283751526"
]


class MyTestCase(unittest.TestCase):
    def test_the_input_small(self):
        octopuses = create_octopuses(the_input_small)
        run_steps(octopuses, 2)
        self.assertEqual(4, octopuses[0][0].energy_level())

    def test_10_steps(self):
        octopuses = create_octopuses(the_input)
        run_steps(octopuses, 10)
        self.assertEqual(204, count_flashes(octopuses))

    def test_100_steps(self):
        octopuses = create_octopuses(the_input)
        run_steps(octopuses, 100)
        self.assertEqual(1656, count_flashes(octopuses))

    def test_calculate_sync_flashes(self):
        octopuses = create_octopuses(the_input)
        self.assertEqual(195, calculate_sync_flashes(octopuses))


if __name__ == '__main__':
    unittest.main()

import unittest
from src.day_25 import SeaFloor, parse_sea_floor, run_step, run_steps_until_stop

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
    def test_simple(self):
        the_input = ["...>>>>>..."]
        sea_floor = parse_sea_floor(the_input)
        self.assertEqual(SeaFloor.east, sea_floor.val_at(0, 7))
        self.assertEqual(SeaFloor.empty, sea_floor.val_at(0, 8))
        (sea_floor, moved) = run_step(sea_floor)
        self.assertTrue(moved)
        self.assertEqual(SeaFloor.empty, sea_floor.val_at(0, 7))
        self.assertEqual(SeaFloor.east, sea_floor.val_at(0, 8))
        (sea_floor, moved) = run_step(sea_floor)
        self.assertTrue(moved)
        self.assertEqual(SeaFloor.east, sea_floor.val_at(0, 7))
        self.assertEqual(SeaFloor.empty, sea_floor.val_at(0, 8))
        self.assertEqual(SeaFloor.east, sea_floor.val_at(0, 9))

    def test_little_bit_more_complex(self):
        the_input = [
            "..........",
            ".>v....v..",
            ".......>..",
            ".........."
        ]
        sea_floor = parse_sea_floor(the_input)
        self.assertEqual(SeaFloor.east, sea_floor.val_at(1, 1))
        self.assertEqual(SeaFloor.south, sea_floor.val_at(1, 2))
        self.assertEqual(SeaFloor.south, sea_floor.val_at(1, 7))
        self.assertEqual(SeaFloor.east, sea_floor.val_at(2, 7))
        (sea_floor, moved) = run_step(sea_floor)
        self.assertTrue(moved)
        self.assertEqual(SeaFloor.east, sea_floor.val_at(1, 1))
        self.assertEqual(SeaFloor.south, sea_floor.val_at(2, 2))
        self.assertEqual(SeaFloor.south, sea_floor.val_at(2, 7))
        self.assertEqual(SeaFloor.east, sea_floor.val_at(2, 8))

    def test_even_more_complex(self):
        the_input = [
            "...>...",
            ".......",
            "......>",
            "v.....>",
            "......>",
            ".......",
            "..vvv.."
        ]
        sea_floor = parse_sea_floor(the_input)
        (sea_floor, moved) = run_step(sea_floor)
        (sea_floor, moved) = run_step(sea_floor)
        (sea_floor, moved) = run_step(sea_floor)
        (sea_floor, moved) = run_step(sea_floor)
        res_input = [
            ">......",
            "..v....",
            "..>.v..",
            ".>.v...",
            "...>...",
            ".......",
            "v......"
        ]
        res_floor = parse_sea_floor(res_input)
        self.assertEqual(res_floor, sea_floor)

    def test_run_steps_until_stop(self):
        the_input = [
            "v...>>.vv>",
            ".vv>>.vv..",
            ">>.>v>...v",
            ">>v>>.>.v.",
            "v>v.vv.v..",
            ">.>>..v...",
            ".vv..>.>v.",
            "v.v..>>v.v",
            "....v..v.>",
        ]
        sea_floor = parse_sea_floor(the_input)
        (sea_floor, iterations) = run_steps_until_stop(sea_floor)
        self.assertEqual(58, iterations)
        res_input = [
            "..>>v>vv..",
            "..v.>>vv..",
            "..>>v>>vv.",
            "..>>>>>vv.",
            "v......>vv",
            "v>v....>>v",
            "vvv.....>>",
            ">vv......>",
            ".>v.vv.v..",
        ]
        res_floor = parse_sea_floor(res_input)
        self.assertEqual(res_floor, sea_floor)


if __name__ == '__main__':
    unittest.main()

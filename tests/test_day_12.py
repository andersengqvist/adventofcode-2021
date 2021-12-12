import unittest

from src.day_12 import build_cave_system, explore_paths


the_input_small = [
    "start-A",
    "start-b",
    "A-c",
    "A-b",
    "b-d",
    "A-end",
    "b-end"
]


the_input_larger = [
    "dc-end",
    "HN-start",
    "start-kj",
    "dc-start",
    "dc-HN",
    "LN-dc",
    "HN-end",
    "kj-sa",
    "kj-HN",
    "kj-dc"
]

the_input_largest = [
    "fs-end",
    "he-DX",
    "fs-he",
    "start-DX",
    "pj-DX",
    "end-zg",
    "zg-sl",
    "zg-pj",
    "pj-he",
    "RW-he",
    "fs-DX",
    "pj-RW",
    "zg-RW",
    "start-pj",
    "he-WI",
    "zg-he",
    "pj-fs",
    "start-RW"
]


class MyTestCase(unittest.TestCase):
    def test_explore_paths_small(self):
        cave_system = build_cave_system(the_input_small)
        paths = explore_paths(cave_system)
        # print_paths(paths)
        self.assertEqual(10, len(paths))

    def test_explore_paths_larger(self):
        cave_system = build_cave_system(the_input_larger)
        paths = explore_paths(cave_system)
        # print_paths(paths)
        self.assertEqual(19, len(paths))

    def test_explore_paths_largest(self):
        cave_system = build_cave_system(the_input_largest)
        paths = explore_paths(cave_system)
        # print_paths(paths)
        self.assertEqual(226, len(paths))

    def test_explore_paths_small_2_visits(self):
        cave_system = build_cave_system(the_input_small)
        paths = explore_paths(cave_system, 2)
        # print_paths(paths)
        self.assertEqual(36, len(paths))

    def test_explore_paths_larger_2_visits(self):
        cave_system = build_cave_system(the_input_larger)
        paths = explore_paths(cave_system, 2)
        # print_paths(paths)
        self.assertEqual(103, len(paths))

    def test_explore_paths_largest_2_visits(self):
        cave_system = build_cave_system(the_input_largest)
        paths = explore_paths(cave_system, 2)
        # print_paths(paths)
        self.assertEqual(3509, len(paths))


if __name__ == '__main__':
    unittest.main()

import unittest

from src.day_23 import Position, create_burrow, create_amphipods_map, PathFinder

the_input = [
    "#############",
    "#...........#",
    "###B#C#B#D###",
    "  #A#D#C#A#",
    "  #########"
]


class MyTestCase(unittest.TestCase):
    def test_create_burrow(self):
        burrow = create_burrow(the_input)
        location = burrow.location_at(Position(1, 3))
        self.assertEqual("hallway", location.type())
        self.assertEqual(Position(1, 3), location.position())
        self.assertTrue(location.is_movable())
        self.assertTrue(location.is_outside_room())
        self.assertEqual(3, location.neighbours())
        location = burrow.location_at(Position(2, 3))
        self.assertEqual("room", location.type())
        self.assertEqual(Position(2, 3), location.position())
        self.assertTrue(location.is_movable())
        self.assertEqual(2, location.neighbours())

    def test_create_amphipods_map(self):
        burrow = create_burrow(the_input)
        amphipods_map = create_amphipods_map(the_input)
        amphipod = amphipods_map[Position(2, 3)]
        self.assertEqual("B", amphipod.type())


    def test_find_shortest_path(self):
        burrow = create_burrow(the_input)
        amphipods_map = create_amphipods_map(the_input)
        pathfinder = PathFinder(burrow)
        result = pathfinder.find_min_cost(amphipods_map)
        self.assertEqual(12521, result.cost())


if __name__ == '__main__':
    unittest.main()

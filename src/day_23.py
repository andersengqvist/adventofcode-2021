from lib.files import read_lines_unstripped
from collections import namedtuple, deque
import heapq


def part1():
    the_input = read_lines_unstripped("res/day_23_1.txt")
    burrow = create_burrow(the_input)
    amphipods_map = create_amphipods_map(the_input)
    pathfinder = PathFinder(burrow)
    result = pathfinder.find_min_cost(amphipods_map)
    res = result.cost()
    print("Day 23.1: {}".format(res))


def part2():
    the_input = read_lines_unstripped("res/day_23_2.txt")
    burrow = create_burrow(the_input)
    amphipods_map = create_amphipods_map(the_input)
    pathfinder = PathFinder(burrow)
    result = pathfinder.find_min_cost(amphipods_map)
    res = result.cost()
    print("Day 23.2: {}".format(res))


Position = namedtuple('Position', 'row col')


class Location:
    def __init__(self, position, the_type, target_amphipod=None, neighbours=None):
        self._position = position
        # type: "room", "wall", "hallway" or "empty"
        self._type = the_type
        # only valid if type = "room"
        self._target_amphipod = target_amphipod
        if neighbours is None:
            neighbours = []
        self._neighbours = neighbours

    def position(self):
        return self._position

    def type(self):
        return self._type

    def is_room(self):
        return self._type == "room"

    def is_hallway(self):
        return self._type == "hallway"

    def is_movable(self):
        return self._type == "room" or self._type == "hallway"

    def target_amphipod(self):
        return self._target_amphipod

    def add_neighbour(self, location):
        self._neighbours.append(location)

    def neighbours(self):
        return self._neighbours

    def is_outside_room(self):
        if self._type == "hallway":
            for neighbour in self._neighbours:
                if neighbour.is_room():
                    return True
        return False

    def __lt__(self, other):
        return False


class Burrow:
    def __init__(self, locations):
        self._locations = locations

    def location_at(self, position):
        return self._locations[position.row][position.col]

    def all_are_home(self, amphipods):
        for (position, amphipod) in amphipods.population():
            location = self._locations[position.row][position.col]
            if not location.is_room() or location.target_amphipod() != amphipod.type():
                return False
        return True

    def rows(self):
        return len(self._locations)

    def cols(self, row):
        len(self._locations[row])

    def print(self, print_room_type=False, amphipods_map=None):
        if amphipods_map is None:
            amphipods_map = {}
        for row in range(len(self._locations)):
            for col in range(len(self._locations[row])):
                position = Position(row, col)
                if position in amphipods_map:
                    amphipod = amphipods_map[position]
                    print(amphipod.type(), end="")
                else:
                    location = self._locations[row][col]
                    # type: "room", "wall", "hallway" or "empty"
                    if location.type() == "room":
                        if print_room_type:
                            print(location.target_amphipod(), end="")
                        else:
                            print(".", end="")
                    elif location.type() == "wall":
                        print("#", end="")
                    elif location.type() == "hallway":
                        print(".", end="")
                    else:
                        print(" ", end="")
            print("")


def create_burrow(the_input):
    types = ["A", "B", "C", "D"]
    locations = []
    for row in range(len(the_input)):
        line = the_input[row]
        if line:
            type_idx = 0
            location_row = []
            locations.append(location_row)
            for col in range(len(the_input[row])):
                char = line[col]
                position = Position(row, col)
                if char == ".":
                    location_row.append(Location(position, "hallway"))
                elif char == "#":
                    location_row.append(Location(position, "wall"))
                elif char in types:
                    location_row.append(Location(position, "room", types[type_idx]))
                    type_idx += 1
                else:
                    location_row.append(Location(position, "empty"))
    for row in range(len(locations)):
        for col in range(len(locations[row])):
            loc = locations[row][col]
            if loc.is_movable():
                add_neighbours(row - 1, col, locations, loc)
                add_neighbours(row + 1, col, locations, loc)
                add_neighbours(row, col - 1, locations, loc)
                add_neighbours(row, col + 1, locations, loc)
    return Burrow(locations)


def add_neighbours(row, col, locations, location):
    if 0 <= row < len(locations) and 0 <= col < len(locations[row]):
        loc = locations[row][col]
        if loc.is_movable():
            location.add_neighbour(loc)


class Amphipod:
    def __init__(self, the_type):
        self._type = the_type

    def type(self):
        return self._type

    def move_cost(self):
        if self._type == "A":
            return 1
        elif self._type == "B":
            return 10
        elif self._type == "C":
            return 100
        else:
            return 1000

    def __eq__(self, other):
        if isinstance(other, Amphipod):
            return self._type == other.type()
        else:
            return False

    def __hash__(self):
        return hash(self._type)


class Amphipods:
    def __init__(self, cost, burrow, amphipods, prev):
        self._cost = cost
        self._estimated_cost = self.estimated_remaining_cost(burrow, amphipods)
        # a map Position -> Amphipod
        self._amphipods = amphipods
        self._prev = prev

    def estimated_remaining_cost(self, burrow, amphipods_map):
        occupied_positions = set()
        result = 0
        for (position, amphipod) in amphipods_map.items():
            result += self.estimated_walk_home(burrow, amphipod, position, occupied_positions)
        return result

    def estimated_walk_home(self, burrow, amphipod, from_position, occupied_positions):
        visited = set()
        queue = []
        from_location = burrow.location_at(from_position)
        heapq.heappush(queue, (0, from_location))
        while queue:
            (cost, location) = heapq.heappop(queue)
            position = location.position()
            visited.add(position)
            if location.target_amphipod() == amphipod.type() and position not in occupied_positions:
                occupied_positions.add(position)
                return cost
            else:
                for neighbour in location.neighbours():
                    if neighbour.position() not in visited:
                        heapq.heappush(queue, (cost + amphipod.move_cost(), neighbour))
        raise Exception("Could not find way home")

    def cost(self):
        return self._cost

    def remaining_cost(self):
        return self._estimated_cost

    def total_cost(self):
        return self._cost + self._estimated_cost

    def population(self):
        return self._amphipods.items()

    def occupied_at(self, position):
        return position in self._amphipods

    def amphipod_at(self, position):
        if position in self._amphipods:
            return self._amphipods[position]
        else:
            return None

    def copy_move(self, amphipod, from_position, to_position, cost, burrow):
        amphipods = self._amphipods.copy()
        del amphipods[from_position]
        amphipods[to_position] = amphipod
        return Amphipods(self._cost + cost, burrow, amphipods, self)

    def amphipods_map(self):
        return self._amphipods

    def previous(self):
        return self._prev

    def __eq__(self, other):
        if isinstance(other, Amphipods):
            return self._amphipods == other._amphipods
        else:
            return False

    def __hash__(self):
        result = 0
        for p in self._amphipods.keys():
            result += p.row * p.col
        return result

    def __lt__(self, other):
        return self.total_cost() < other.total_cost()


def create_amphipods_map(the_input):
    types = ["A", "B", "C", "D"]
    amphipods = {}
    for row in range(len(the_input)):
        line = the_input[row]
        if line:
            for col in range(len(the_input[row])):
                char = line[col]
                position = Position(row, col)
                if char in types:
                    amphipods[position] = Amphipod(char)
    return amphipods


class PathFinder:
    def __init__(self, burrow):
        self._burrow = burrow

    def find_min_cost(self, amphipods_map):
        visited = {}
        queue = []
        start_position = Amphipods(0, self._burrow, amphipods_map, None)
        heapq.heappush(queue, (start_position.total_cost(), start_position))
        while queue:
            (_c, amphipods) = heapq.heappop(queue)
            if amphipods not in visited:
                visited[amphipods] = amphipods
                if amphipods.remaining_cost() == 0:
                    return amphipods
                else:
                    for (position, amphipod) in amphipods.population():
                        self.inspect_movement(queue, visited, position, amphipod, amphipods)

    def inspect_movement(self, queue, visited, position, amphipod, amphipods):
        from_location = self._burrow.location_at(position)
        inspected = set()
        to_inspect = deque()
        for neighbour in from_location.neighbours():
            to_inspect.append((neighbour, amphipod.move_cost()))
        while to_inspect:
            (location, cost) = to_inspect.pop()
            inspected.add(location.position())
            move_score = self.move_score(from_location, location, amphipod, amphipods)
            if move_score > 0:
                # can move at least past
                if move_score == 2:
                    # can move to
                    from_position = from_location.position()
                    to_position = location.position()
                    new_amphipods = amphipods.copy_move(amphipod, from_position, to_position, cost, self._burrow)
                    if new_amphipods in visited:
                        v = visited[new_amphipods]
                        if new_amphipods.total_cost() < v.total_cost():
                            heapq.heappush(queue, (new_amphipods.total_cost(), new_amphipods))
                    else:
                        heapq.heappush(queue, (new_amphipods.total_cost(), new_amphipods))
                for neighbour in location.neighbours():
                    if neighbour.position() not in inspected:
                        to_inspect.append((neighbour, cost + amphipod.move_cost()))

    def move_score(self, from_location, to_location, amphipod, amphipods):
        if amphipods.occupied_at(to_location.position()):
            return -1
        if to_location.is_outside_room():
            return 1
        if to_location.is_room():
            if to_location.target_amphipod() != amphipod.type():
                return 1
            else:
                if self.is_possible_to_move_home(to_location, amphipod.type(), amphipods):
                    return 2
                else:
                    return 1
        else:
            if from_location.is_hallway():
                return 1
            else:
                return 2

    def is_possible_to_move_home(self, home_location, home_type, amphipods):
        inspected = set()
        to_inspect = deque()
        to_inspect.append(home_location)
        while to_inspect:
            location = to_inspect.pop()
            position = location.position()
            inspected.add(position)
            amphipod = amphipods.amphipod_at(position)
            if amphipod is not None and amphipod.type() != home_type:
                return False
            for neighbour in location.neighbours():
                if neighbour.position() not in inspected and neighbour.target_amphipod() == home_type:
                    to_inspect.append(neighbour)
        return True


if __name__ == "__main__":
    part1()
    part2()

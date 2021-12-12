from lib.files import read_lines
from collections import deque


def part1():
    the_input = read_lines("res/day_12_1.txt")
    cave_system = build_cave_system(the_input)
    paths = explore_paths(cave_system)
    res = len(paths)
    print("Day 12.1: {}".format(res))


def part2():
    the_input = read_lines("res/day_12_1.txt")
    cave_system = build_cave_system(the_input)
    paths = explore_paths(cave_system, 2)
    res = len(paths)
    print("Day 12.2: {}".format(res))


class Cave:
    def __init__(self, name):
        self._name = name
        self._neighbours = []

    def name(self):
        return self._name

    def is_small(self):
        return self._name.islower()

    def is_start(self):
        return self._name == "start"

    def is_end(self):
        return self._name == "end"

    def add_neighbour(self, n):
        self._neighbours.append(n)

    def neighbours(self):
        return self._neighbours

    def __eq__(self, other):
        if isinstance(other, Cave):
            return self._name == other.name()
        return False

    def __hash__(self):
        return hash(self._name)


class Path:
    def __init__(self, to_visit, max_visit=1, path=None, visited_small_caves=None):
        self._to_visit = to_visit
        self._max_visit = max_visit
        if path is None:
            path = list()
        self._path = path.copy()
        if visited_small_caves is None:
            visited_small_caves = {}
        self._visited = visited_small_caves.copy()

    def is_end(self):
        return self._to_visit is None

    def visit_next(self):
        if not self._can_visit(self._to_visit):
            return []
        self._path.append(self._to_visit)
        if self._to_visit.is_small():
            self._visited[self._to_visit.name()] = self._visited.get(self._to_visit.name(), 0) + 1
        if self._to_visit.is_end():
            self._to_visit = None
            return [self]
        neigh = self._to_visit.neighbours()
        res = []
        for n in neigh:
            if self._can_visit(n):
                if len(res) == 0:
                    self._to_visit = n
                    res.append(self)
                else:
                    res.append(Path(n, self._max_visit, self._path, self._visited))
        return res

    def _can_visit(self, cave):
        visits = self._visited.get(cave.name(), 0)
        if visits == 0:
            return True
        if visits < self._max_visit:
            if max(self._visited.values()) <= 1:
                return True
        return False

    def __str__(self):
        if self._to_visit is None:
            return ",".join(p.name() for p in self._path)
        return ",".join(p.name() for p in self._path) + " -> {}".format(self._to_visit.name())


def build_cave_system(the_input):
    caves = {}
    for line in the_input:
        names = line.split("-")
        cave1 = caves.setdefault(names[0], Cave(names[0]))
        cave2 = caves.setdefault(names[1], Cave(names[1]))
        if cave2.name() != "start" and cave1.name() != "end":
            cave1.add_neighbour(cave2)
        if cave1.name() != "start" and cave2.name() != "end":
            cave2.add_neighbour(cave1)
    return caves.get("start", Cave("start"))


def explore_paths(start_cave, max_visit=1):
    begin = Path(start_cave, max_visit)
    finished_paths = []
    exploring_paths = deque()
    exploring_paths.append(begin)
    while len(exploring_paths) != 0:
        path = exploring_paths.pop()
        new_paths = path.visit_next()
        for new_path in new_paths:
            if new_path.is_end():
                finished_paths.append(new_path)
            else:
                exploring_paths.append(new_path)
    return finished_paths


def print_paths(paths):
    for path in paths:
        print(path)


if __name__ == "__main__":
    part1()
    part2()

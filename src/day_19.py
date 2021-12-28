from lib.files import read_file
from lib.matrix import Vec3, Mat3
from collections import Counter, deque
import os
import copy
import heapq


def part1and2():
    the_input = read_file("res/day_19_1.txt")
    scanners = create_scanners(the_input)
    water = build_water(scanners, 12)
    print("Day 19.1: {}".format(water.beacons()))
    print("Day 19.2: {}".format(water.max_scanner_distance()))


class Beacon:
    def __init__(self, position: Vec3, neighbours=None, neighbour_distances=None):
        self._position = position
        if neighbours is None:
            neighbours = {}
        self._neighbours = neighbours
        if neighbour_distances is None:
            neighbour_distances = Counter()
        self._neighbour_distances = neighbour_distances

    def position(self):
        return self._position

    def neighbour_distances(self):
        return self._neighbour_distances

    def add_neighbour(self, neighbour_pos):
        v = self._position - neighbour_pos
        d = self._position.taxi_distance(neighbour_pos)
        self._neighbours.setdefault(d, []).append(v)
        self._neighbour_distances[d] += 1

    def max_distance(self):
        return max(self._neighbours.keys())

    def similarity_value(self, other):
        """ The higher the value the more similar"""
        if isinstance(other, Beacon):
            c = self._neighbour_distances & other._neighbour_distances
            return sum(c.values())
        return -1

    def find_transformation_matrices(self, other):
        if isinstance(other, Beacon):
            result = set()
            for (dist, vecs) in self._neighbours.items():
                for vec in vecs:
                    for other_vec in other._neighbours.get(dist, []):
                        m = find_rotation_matrix(vec, other_vec)
                        if m is not None:
                            result.add(m)
            return result
        return []

    def __lt__(self, other):
        return False

    def __copy__(self):
        return Beacon(self._position, self._neighbours.copy(), self._neighbour_distances.copy())


class Scanner:
    def __init__(self, name):
        self._name = name
        self._beacons = {}

    def name(self):
        return self._name

    def add_beacon(self, position: Vec3):
        if position not in self._beacons:
            new_beacon = Beacon(position)
            for beacon in self._beacons.values():
                beacon.add_neighbour(position)
                new_beacon.add_neighbour(beacon.position())
            self._beacons[position] = new_beacon

    def beacons(self):
        return self._beacons.values()

    def transform(self, matrix, movement):
        return [matrix * pos + movement for pos in self._beacons.keys()]

    def print(self):
        print(self._name)
        for beacon in self._beacons.values():
            print(beacon.position())


def create_scanners(the_input):
    return [create_scanner(inp.strip()) for inp in the_input.split(os.linesep + os.linesep) if inp.strip()]


def create_scanner(the_input):
    lines = the_input.split(os.linesep)
    name = lines[0].strip()
    scanner = Scanner(name)
    for line in lines[1:]:
        chs = line.split(",")
        v = Vec3(int(chs[0].strip()), int(chs[1].strip()), int(chs[2].strip()))
        scanner.add_beacon(v)
    return scanner


class Water:
    def __init__(self, init_scanner):
        self._beacons = {b.position(): copy.copy(b) for b in init_scanner.beacons()}
        self._beacon_pos = set(self._beacons.keys())
        self._scanners = [Vec3(0, 0, 0)]

    def add_beacon(self, position: Vec3):
        if position not in self._beacon_pos:
            self._beacon_pos.add(position)
            new_beacon = Beacon(position)
            for beacon in self._beacons.values():
                beacon.add_neighbour(position)
                new_beacon.add_neighbour(beacon.position())
            self._beacons[position] = new_beacon

    def add_scanner(self, position: Vec3):
        self._scanners.append(position)

    def beacons(self):
        return len(self._beacon_pos)

    def max_scanner_distance(self):
        res = 0
        for i in range(len(self._scanners)):
            for j in range(i + 1, len(self._scanners)):
                s1 = self._scanners[i]
                s2 = self._scanners[j]
                d = s1.taxi_distance(s2)
                res = max(d, res)
        return res

    def print(self):
        print("Water")
        for beacon in self._beacons.values():
            print("Beacon: {}".format(beacon.position()))
        for scanner in self._scanners:
            print("Scanner: {}".format(scanner))

    def find_scanner(self, scanner: Scanner, overlap):
        queue = []
        for beacon in self._beacons.values():
            for other_beacon in scanner.beacons():
                similarity = beacon.similarity_value(other_beacon)
                if similarity >= 2:
                    heapq.heappush(queue, (-similarity, (beacon, other_beacon)))
        while queue:
            (_sim, (beacon, other_beacon)) = heapq.heappop(queue)
            matrices = other_beacon.find_transformation_matrices(beacon)
            for m in matrices:
                new_vec = m * other_beacon.position()
                distance = beacon.position() - new_vec
                transformed_vecs = set(scanner.transform(m, distance))
                u = self._beacon_pos.intersection(transformed_vecs)
                if len(u) >= overlap:
                    self.add_scanner(distance)
                    for tv in transformed_vecs:
                        self.add_beacon(tv)
                    return True
        return False


def build_water(scanners, overlap):
    water = Water(scanners[0])
    to_inspect = deque()
    to_inspect.extend(scanners[1:])
    while to_inspect:
        scanner = to_inspect.pop()
        found = water.find_scanner(scanner, overlap)
        if not found:
            to_inspect.appendleft(scanner)
    return water


def rsin(angle):
    if angle == 90:
        return 1
    elif angle == 270:
        return -1
    else:
        return 0


def rcos(angle):
    if angle == 0:
        return 1
    elif angle == 180:
        return -1
    else:
        return 0


def rotx(angle):
    c = rcos(angle)
    s = rsin(angle)
    return Mat3([[1, 0, 0],
                 [0, c, -s],
                 [0, s, c]])


def roty(angle):
    c = rcos(angle)
    s = rsin(angle)
    return Mat3([[c, 0, s],
                 [0, 1, 0],
                 [-s, 0, c]])


def rotz(angle):
    c = rcos(angle)
    s = rsin(angle)
    return Mat3([[c, -s, 0],
                 [s, c, 0],
                 [0, 0, 1]])


rotx0 = rotx(0)
rotx90 = rotx(90)
rotx180 = rotx(180)
rotx270 = rotx(270)
rotz0 = rotz(0)
rotz90 = rotz(90)
rotz180 = rotz(180)
rotz270 = rotz(270)
roty0 = roty(0)
roty90 = roty(90)
roty180 = roty(1800)
roty270 = roty(270)

rot_matrices = [
    rotx0,
    rotx90,
    rotx180,
    rotx270,
    rotz90,
    rotz90 * rotx90,
    rotz90 * rotx180,
    rotz90 * rotx270,
    rotz180,
    rotz180 * rotx90,
    rotz180 * rotx180,
    rotz180 * rotx270,
    rotz270,
    rotz270 * rotx90,
    rotz270 * rotx180,
    rotz270 * rotx270,
    roty90,
    roty90 * rotx90,
    roty90 * rotx180,
    roty90 * rotx270,
    roty270,
    roty270 * rotx90,
    roty270 * rotx180,
    roty270 * rotx270,
]


def find_rotation_matrix(vec1, vec2):
    """finds the rotation matrix M, such that M * vec1 = vec2. Return None if no such matrix could be found"""
    for m in rot_matrices:
        v = m * vec1
        if v == vec2:
            return m
    return None


if __name__ == "__main__":
    part1and2()

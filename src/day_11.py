from lib.files import read_lines


def part1():
    the_input = read_lines("res/day_11_1.txt")
    octopuses = create_octopuses(the_input)
    run_steps(octopuses, 100)
    res = count_flashes(octopuses)
    print("Day 11.1: {}".format(res))


def part2():
    the_input = read_lines("res/day_11_1.txt")
    octopuses = create_octopuses(the_input)
    res = calculate_sync_flashes(octopuses)
    print("Day 11.2: {}".format(res))


class Octopus:
    def __init__(self, energy_level):
        self._energy_level = energy_level
        self._flashes = 0
        self._flashed = False

    def energy_level(self):
        return self._energy_level

    def flashes(self):
        return self._flashes

    def step_energy_level(self):
        self._energy_level += 1
        if self._energy_level > 9 and not self._flashed:
            self._flashed = True
            self._flashes += 1
            return True
        return False

    def reset(self):
        self._flashed = False
        if self._energy_level > 9:
            self._energy_level = 0


def create_octopuses(the_input):
    return [create_octopus_row(line) for line in the_input]


def create_octopus_row(line):
    return [Octopus(int(ch)) for ch in line]


def run_steps(octopuses, steps):
    for step in range(1, steps + 1):
        run_step(octopuses)


def calculate_sync_flashes(octopuses):
    step = 0
    while not is_synchronized(octopuses):
        run_step(octopuses)
        step += 1
    return step


def run_step(octopuses):
    for row in range(len(octopuses)):
        for col in range(len(octopuses[row])):
            if octopuses[row][col].step_energy_level():
                step_neighbours(octopuses, row, col)
    for row in range(len(octopuses)):
        for col in range(len(octopuses[row])):
            octopuses[row][col].reset()


def step_neighbours(octopuses, the_row, the_col):
    for row in range(max(the_row - 1, 0), min(the_row + 2, len(octopuses))):
        for col in range(max(the_col - 1, 0), min(the_col + 2, len(octopuses[row]))):
            if not (row == the_row and col == the_col):
                if octopuses[row][col].step_energy_level():
                    step_neighbours(octopuses, row, col)


def is_synchronized(octopuses):
    for row in range(len(octopuses)):
        for col in range(len(octopuses[row])):
            if octopuses[row][col].energy_level() != 0:
                return False
    return True


def count_flashes(octopuses):
    flashes = 0
    for row in range(len(octopuses)):
        for col in range(len(octopuses[row])):
            flashes += octopuses[row][col].flashes()
    return flashes


def print_octopuses(octopuses):
    print("Octopuses:")
    for row in range(len(octopuses)):
        for col in range(len(octopuses[row])):
            print('{:2d} '.format(octopuses[row][col].energy_level()), end='')
        print("")


if __name__ == "__main__":
    part1()
    part2()

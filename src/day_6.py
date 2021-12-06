from lib.files import read_file


def part1():
    the_input = [int(fish) for fish in read_file("res/day_6_1.txt").split(",")]
    res = calculate_population(6, the_input, 80)
    print("Day 6.1: {}".format(res))


def part2():
    the_input = [int(fish) for fish in read_file("res/day_6_1.txt").split(",")]
    res = calculate_population(6, the_input, 256)
    print("Day 6.2: {}".format(res))


class LanternFishes:

    def __init__(self, spawn_time, initial_flock):
        self._day = 0
        self._reset_idx = spawn_time
        self._flock = [0] * (spawn_time + 2 + 1)
        for i in initial_flock:
            self._flock[i] += 1

    def get_day(self):
        return self._day

    def step_day(self):
        breeding = self._flock[0]
        for i in range(len(self._flock) - 1):
            self._flock[i] = self._flock[i + 1]
        self._flock[-1] = breeding
        self._flock[self._reset_idx] += breeding
        self._day += 1

    def count(self):
        return sum(self._flock)

    def print(self):
        print("Day: {}, population: {}, flock: {}".format(self._day, self.count(), self._flock))


def calculate_population(spawn_time, initial_flock, days):
    flock = LanternFishes(spawn_time, initial_flock)
    while flock.get_day() != days:
        flock.step_day()
    return flock.count()


if __name__ == "__main__":
    part1()
    part2()

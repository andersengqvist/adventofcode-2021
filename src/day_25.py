from lib.files import read_lines


def part1():
    the_input = read_lines("res/day_25_1.txt")
    sea_floor = parse_sea_floor(the_input)
    (sea_floor, res) = run_steps_until_stop(sea_floor)
    print("Day 25.1: {}".format(res))


def part2():
    print("Day 25.2: {}".format("Wohoo!"))


class SeaFloor:
    empty = 0
    east = 1
    south = 2

    def __init__(self, rows, cols):
        self._floor = [[SeaFloor.empty for _c in range(cols)] for _r in range(rows)]

    def rows(self):
        return len(self._floor)

    def cols(self):
        return len(self._floor[0])

    def norm_row(self, row):
        if row >= self.rows():
            return row % self.rows()
        else:
            return row

    def norm_col(self, col):
        if col >= self.cols():
            return col % self.cols()
        else:
            return col

    def val_at(self, row, col):
        return self._floor[self.norm_row(row)][self.norm_col(col)]

    def set_at(self, row, col, val):
        self._floor[self.norm_row(row)][self.norm_col(col)] = val

    def __eq__(self, other):
        if isinstance(other, SeaFloor):
            return self._floor == other._floor
        return False

    def __hash__(self):
        return hash(self._floor)

    def print(self):
        for row in range(self.rows()):
            for col in range(self.cols()):
                val = self.val_at(row, col)
                if val == SeaFloor.empty:
                    print(".", end="")
                elif val == SeaFloor.east:
                    print(">", end="")
                else:
                    print("v", end="")
            print("")


def parse_sea_floor(the_input):
    rows = len(the_input)
    cols = len(the_input[0])
    result = SeaFloor(rows, cols)
    for row in range(rows):
        for col in range(cols):
            val = the_input[row][col]
            if val == ">":
                result.set_at(row, col, SeaFloor.east)
            elif val == "v":
                result.set_at(row, col, SeaFloor.south)
    return result


def run_steps_until_stop(sea_floor):
    runs = 0
    while True:
        (sea_floor, moved) = run_step(sea_floor)
        runs += 1
        if not moved:
            return sea_floor, runs


def run_step(sea_floor):
    result = SeaFloor(sea_floor.rows(), sea_floor.cols())
    moved = False
    # During a single step, the east-facing herd moves first, then the south-facing herd moves.
    for row in range(sea_floor.rows()):
        for col in range(sea_floor.cols()):
            val = sea_floor.val_at(row, col)
            if val == SeaFloor.east:
                n = sea_floor.val_at(row, col + 1)
                if n == SeaFloor.empty:
                    result.set_at(row, col + 1, val)
                    moved = True
                else:
                    result.set_at(row, col, val)
    for row in range(sea_floor.rows()):
        for col in range(sea_floor.cols()):
            val = sea_floor.val_at(row, col)
            if val == SeaFloor.south:
                n1 = sea_floor.val_at(row + 1, col)
                if n1 == SeaFloor.south:
                    result.set_at(row, col, val)
                else:
                    n2 = result.val_at(row + 1, col)
                    if n2 == SeaFloor.empty:
                        result.set_at(row + 1, col, val)
                        moved = True
                    else:
                        result.set_at(row, col, val)
    return result, moved


if __name__ == "__main__":
    part1()
    part2()

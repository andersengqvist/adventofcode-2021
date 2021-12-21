from collections import Counter


def part1():
    # Player 1 starting position: 2
    # Player 2 starting position: 1
    dice = DeterministicDice()
    board = Board(10)
    player1 = Player(2, board, dice)
    player2 = Player(1, board, dice)
    res = play_game_1(player1, player2, dice)
    print("Day 21.1: {}".format(res))


def part2():
    # Player 1 starting position: 2
    # Player 2 starting position: 1
    dice = DiracDice()
    board = Board(10)
    play = DimensionalPlay(2, 1, board, dice)
    res = play_game_2(play)
    print("Day 21.2: {}".format(res))


class DeterministicDice:
    def __init__(self):
        self._score = 1
        self._rolls = 0

    def roll(self):
        res = self._score
        self._score += 1
        self._rolls += 1
        if self._score > 100:
            self._score = 1
        return res

    def roll_times(self, times):
        res = 0
        for t in range(times):
            res += self.roll()
        return res

    def rolls(self):
        return self._rolls


class Board:
    def __init__(self, size):
        self._size = size

    def move(self, from_pos, steps):
        pos = from_pos + (steps % self._size)
        if pos > self._size:
            pos -= self._size
        return pos


class Player:
    def __init__(self, init_pos, board, dice):
        self._pos = init_pos
        self._board = board
        self._dice = dice
        self._score = 0

    def play_round(self):
        steps = self._dice.roll_times(3)
        self._pos = self._board.move(self._pos, steps)
        self._score += self._pos
        return self._score

    def score(self):
        return self._score


def play_game_1(player1, player2, dice):
    while True:
        res = player1.play_round()
        if res >= 1000:
            return player2.score() * dice.rolls()
        res = player2.play_round()
        if res >= 1000:
            return player1.score() * dice.rolls()


class DiracDice:
    def __init__(self):
        self._counter = Counter()
        for d1 in range(1, 4):
            for d2 in range(1, 4):
                for d3 in range(1, 4):
                    res = d1 + d2 + d3
                    self._counter[res] += 1

    def items(self):
        return self._counter.items()


class DimensionalPlayers:
    def __init__(self, p1_pos, p1_score, p2_pos, p2_score):
        self._p1_pos = p1_pos
        self._p1_score = p1_score
        self._p2_pos = p2_pos
        self._p2_score = p2_score

    def pos1(self):
        return self._p1_pos

    def score1(self):
        return self._p1_score

    def pos2(self):
        return self._p2_pos

    def score2(self):
        return self._p2_score

    def __eq__(self, other):
        return self._p1_pos == other.pos1()\
               and self._p1_score == other.score1()\
               and self._p2_pos == other.pos2()\
               and self._p2_score == other.score2()

    def __hash__(self):
        return self._p1_pos + self._p1_score + self._p2_pos + self._p2_score

    def __repr__(self):
        return "({} -> {}, {} -> {})".format(self._p1_pos, self._p1_score, self._p2_pos, self._p2_score)


class DimensionalPlay:
    def __init__(self, init_pos1, init_pos2, board, dice):
        self._board = board
        self._dice = dice
        self._dimensions = Counter()
        self._dimensions[DimensionalPlayers(init_pos1, 0, init_pos2, 0)] += 1
        self._wins1 = 0
        self._wins2 = 0

    def finished(self):
        return not bool(self._dimensions)

    def wins1(self):
        return self._wins1

    def wins2(self):
        return self._wins2

    def play_round(self):
        next_dimensions = Counter()
        # Play player 1
        for (steps, split_factor) in self._dice.items():
            for (play, dimensions) in self._dimensions.items():
                new_pos = self._board.move(play.pos1(), steps)
                new_score = play.score1() + new_pos
                new_dimensions = dimensions * split_factor
                if new_score >= 21:
                    self._wins1 += new_dimensions
                else:
                    next_dimensions[DimensionalPlayers(new_pos, new_score, play.pos2(), play.score2())] += new_dimensions
        self._dimensions = next_dimensions
        next_dimensions = Counter()
        # Play player 2
        for (steps, split_factor) in self._dice.items():
            for (play, dimensions) in self._dimensions.items():
                new_pos = self._board.move(play.pos2(), steps)
                new_score = play.score2() + new_pos
                new_dimensions = dimensions * split_factor
                if new_score >= 21:
                    self._wins2 += new_dimensions
                else:
                    next_dimensions[DimensionalPlayers(play.pos1(), play.score1(), new_pos, new_score)] += new_dimensions
        self._dimensions = next_dimensions


def play_game_2(play):
    while not play.finished():
        play.play_round()
    return max(play.wins1(), play.wins2())


if __name__ == "__main__":
    part1()
    part2()

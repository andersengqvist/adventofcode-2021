import os
from lib.files import read_file


def part1():
    the_input = read_file("res/day_4_1.txt")
    res = find_winning(the_input)
    print("Day 4.1: {}".format(res))


def part2():
    the_input = read_file("res/day_4_1.txt")
    res = find_losing(the_input)
    print("Day 4.2: {}".format(res))


class BoardCell:

    def __init__(self, num):
        self.num = num
        self.played = False


class BingoBoard:

    def __init__(self, board):
        # The game board. Matrix of BoardCells,
        self.board = board
        self.winning_number = -1  # Assuming all numbers are positive

    def play_number(self, num):
        if not self.is_won():
            for row in range(len(self.board)):
                for col in range(len(self.board[row])):
                    if self.board[row][col].num == num:
                        self.board[row][col].played = True
                        won = self._check_win(row, col)
                        if won:
                            self.winning_number = num
                        return won
        return False

    def _check_win(self, the_row, the_col):
        return self._check_vertical_win(the_col) or self._check_horizontal_win(the_row)

    def _check_horizontal_win(self, the_row):
        for col in range(len(self.board[the_row])):
            if not self.board[the_row][col].played:
                return False
        return True

    def _check_vertical_win(self, the_col):
        for row in range(len(self.board)):
            if not self.board[row][the_col].played:
                return False
        return True

    def is_won(self):
        return self.winning_number >= 0

    def get_score(self):
        if not self.is_won():
            return -1
        score = 0
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if not self.board[row][col].played:
                    score += self.board[row][col].num
        return score * self.winning_number

    def print(self):
        print("Board:")
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col].played:
                    print('{:2d}*'.format(self.board[row][col].num), end=' ')
                else:
                    print('{:2d} '.format(self.board[row][col].num), end=' ')
            print("")


def build_bingo_board(the_string):
    lines = the_string.split(os.linesep)
    board = []
    for line in lines:
        board.append([BoardCell(int(num.strip())) for num in line.strip().split()])
    return BingoBoard(board)


def build_game(the_string):
    chunks = the_string.split(os.linesep + os.linesep)
    numbers = [int(num.strip()) for num in chunks[0].split(",")]
    boards = [build_bingo_board(board) for board in chunks[1:]]
    return numbers, boards


def find_winning(the_string):
    p = build_game(the_string)
    numbers = p[0]
    boards = p[1]
    for num in numbers:
        for board in boards:
            if board.play_number(num):
                return board.get_score()
    return -1


def find_losing(the_string):
    p = build_game(the_string)
    numbers = p[0]
    boards = p[1]
    won_boards = 0
    for num in numbers:
        for board in boards:
            if not board.is_won():
                if board.play_number(num):
                    won_boards += 1
                    if won_boards == len(boards):
                        return board.get_score()
    return -1


if __name__ == "__main__":
    part1()
    part2()

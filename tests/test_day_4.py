import unittest

from src.day_4 import build_bingo_board, find_winning, find_losing

winning_board = """14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""

losing_board = """ 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6"""

game_string = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
"""


class MyTestCase(unittest.TestCase):

    def test_play_winning(self):
        # 7,4,9,5,11,17,23,2,0,14,21,24
        board = build_bingo_board(winning_board)
        self.assertFalse(board.play_number(7))
        self.assertFalse(board.play_number(4))
        self.assertFalse(board.play_number(9))
        self.assertFalse(board.play_number(5))
        self.assertFalse(board.play_number(11))
        self.assertFalse(board.play_number(17))
        self.assertFalse(board.play_number(23))
        self.assertFalse(board.play_number(2))
        self.assertFalse(board.play_number(0))
        self.assertFalse(board.play_number(14))
        self.assertFalse(board.play_number(21))
        self.assertTrue(board.play_number(24))
        self.assertEqual(4512, board.get_score())

    def test_play_winning_game(self):
        self.assertEqual(4512, find_winning(game_string))

    def test_play_losing(self):
        # 7,4,9,5,11,17,23,2,0,14,21,24,10,16,13
        board = build_bingo_board(losing_board)
        self.assertFalse(board.play_number(7))
        self.assertFalse(board.play_number(4))
        self.assertFalse(board.play_number(9))
        self.assertFalse(board.play_number(5))
        self.assertFalse(board.play_number(11))
        self.assertFalse(board.play_number(17))
        self.assertFalse(board.play_number(23))
        self.assertFalse(board.play_number(2))
        self.assertFalse(board.play_number(0))
        self.assertFalse(board.play_number(14))
        self.assertFalse(board.play_number(21))
        self.assertFalse(board.play_number(24))
        self.assertFalse(board.play_number(10))
        self.assertFalse(board.play_number(16))
        self.assertTrue(board.play_number(13))
        self.assertEqual(1924, board.get_score())

    def test_play_losing_game(self):
        self.assertEqual(1924, find_losing(game_string))


if __name__ == '__main__':
    unittest.main()

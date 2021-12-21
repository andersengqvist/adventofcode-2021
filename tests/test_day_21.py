import unittest

from src.day_21 import DeterministicDice, Board, Player, play_game_1, DiracDice, play_game_2, DimensionalPlay


class MyTestCase(unittest.TestCase):
    def test_play_game_1(self):
        dice = DeterministicDice()
        board = Board(10)
        player1 = Player(4, board, dice)
        player2 = Player(8, board, dice)
        res = play_game_1(player1, player2, dice)
        self.assertEqual(739785, res)

    def test_play_game_2(self):
        dice = DiracDice()
        board = Board(10)
        play = DimensionalPlay(4, 8, board, dice)
        res = play_game_2(play)
        self.assertEqual(444356092776315, res)


if __name__ == '__main__':
    unittest.main()

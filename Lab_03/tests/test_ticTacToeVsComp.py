from unittest import TestCase
from unittest.mock import patch

# from source import Player
# from source import TicTacToe
import source.TicTacToe as TicTacToe
import source.Player as Player


class TestTicTacToeVsComp(TestCase):
    def test_check_if_this_move_make_winner_should_return_false (self):
        player = Player.Player('test')
        tictactoe = TicTacToe.TicTacToeVsComp(2, player)
        x_coord = 0
        y_coord = 0
        tictactoe.board.board[x_coord][y_coord] = 1
        expected_return_statement = False
        self.assertEqual(tictactoe.check_if_this_move_make_winner(x_coord, y_coord), expected_return_statement)

    def test_move_should_return_false_if_coordinates_are_not_in_board (self):
        player = Player.Player('test')
        tictactoe = TicTacToe.TicTacToeVsComp(2, player)
        x_coord = 2
        y_coord = 0
        expected_return_statement = False
        self.assertEqual(tictactoe.move(1, x_coord, y_coord), expected_return_statement)

    @patch('source.TicTacToe.TicTacToeVsComp.get_coordinates', return_value = 0)
    def test_pair_of_moves_should_return_false (self, mock_get_coordinates):
        player = Player.Player('test')
        tictactoe = TicTacToe.TicTacToeVsComp(2, player)
        expected_return_statement = False
        self.assertEqual(tictactoe.pair_of_moves(), expected_return_statement)
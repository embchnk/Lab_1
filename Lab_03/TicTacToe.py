import Board
import Player
import random
from abc import ABCMeta, abstractmethod


class AbstractTicTacToe:
    __metaclass__=ABCMeta

    @abstractmethod
    def get_coordinates(self):
        pass

    @abstractmethod
    def move(self, which_player, x_coord, y_coord):
        pass

    @abstractmethod
    def start_game(self):
        pass


class TicTacToeVsComp(AbstractTicTacToe):
    def __init__(self, size, player):
        self.board = Board.Board(size)
        self.player = player
        self.sign = random.randint(1, 2)

    def get_coordinates(self):
        print("Choose x: ")
        try:
            get_val = input()
            x_coord = int(get_val)
        except ValueError:
            if get_val != 'q' and 'Q':
                return True
            return False
        print("Choose y: ")
        try:
            get_val = input()
            y_coord = int(get_val)
        except ValueError:
            if get_val != 'q' and 'Q':
                return True
            return False
        self.move(self.sign, x_coord, y_coord)
        return True

    def move(self, which_player, x_coord, y_coord):
        try:
            self.board.board[x_coord][y_coord] = which_player
        except IndexError:
            return

    def start_game(self):
        choice = True
        while choice:
            print("Game of player: ", self.player.name)
            print("Press Q to quit")
            self.board.show_board()
            choice = self.get_coordinates()
        self.board.save_board()



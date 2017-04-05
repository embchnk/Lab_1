import random
from abc import ABCMeta, abstractmethod

from source import Board


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
        self.sign = self.player.ret_sign()

    def check_if_this_move_make_winner(self, x_coord, y_coord):
        temp_counter = 0
        if x_coord == y_coord:
            for iterator in range(self.board.size):
                if self.board.board[x_coord][y_coord] == self.board.board[iterator][iterator]:
                    temp_counter += 1
                else:
                    break
            if temp_counter == self.board.size:
                return True
            temp_counter = 0
            for iterator in range(self.board.size):
                if self.board.board[x_coord][y_coord] == self.board.board[iterator][self.board.size - iterator - 1]:
                    temp_counter += 1
                else:
                    break
            if temp_counter == self.board.size:
                return True
            temp_counter = 0
        for iterator in range(self.board.size):
            if self.board.board[x_coord][y_coord] == self.board.board[iterator][y_coord]:
                temp_counter += 1
            else:
                break
        if temp_counter == self.board.size:
            return True
        temp_counter = 0
        for iterator in range(self.board.size):
            if self.board.board[x_coord][y_coord] == self.board.board[x_coord][iterator]:
                temp_counter += 1
            else:
                break
        if temp_counter == self.board.size:
            return True
        return False

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
        if not self.move(self.sign, x_coord, y_coord):
            print("Choose free/correct cell")
            self.get_coordinates()
        else:
            if self.check_if_this_move_make_winner(x_coord, y_coord):
                print("You won :)")
                self.board.counter = 0
        return True

    def move(self, which_player, x_coord, y_coord):
        try:
            if not self.board.board[x_coord][y_coord]:
                self.board.board[x_coord][y_coord] = which_player
                return 1
            else:
                return 0
        except IndexError:
            return 0

    def comp_move(self):
        x_coord = random.randrange(0, self.board.size)
        y_coord = random.randrange(0, self.board.size)
        if not self.move(3 - self.sign, x_coord, y_coord):
            self.comp_move()
        else:
            if self.check_if_this_move_make_winner(x_coord, y_coord):
                print("You lost")
                self.board.counter = 0

    def pair_of_moves(self):
        choice = self.get_coordinates()
        if not choice:
            return False
        self.board.counter -= 1
        if not self.board.counter <= 0:
            self.comp_move()
        self.board.counter -= 1
        return True

    def play_game(self):
        choice = True
        while choice and self.board.counter > 0:
            print("Game of player: ", self.player.name)
            print("Press Q to quit")
            self.board.show_board()
            choice = self.pair_of_moves()
        if self.board.counter <= 0:
            print("Game finished, thank you :)")
        else:
            self.board.save_board(self.player.name)
        self.board.show_board()

    def start_game(self):
        self.play_game()



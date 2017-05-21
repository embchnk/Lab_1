# from source import Player
# from source import TicTacToe
import Player
import TicTacToe
import server
import random
import datetime
import logging
from abc import ABCMeta, abstractmethod


class AbstractMenu:
    __metaclass__ = ABCMeta

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def get_choice(self):
        pass

    @abstractmethod
    def init_game(self, mode):
        pass

    @abstractmethod
    def do_proper_action(self):
        pass


class Menu(AbstractMenu):
    def __init__(self, server):
        self.menu = ["1 New game\n", "2 Load game\n", "3 Quit\n"]
        self.choice = 0
        self.server = server

    def change_choice(self, choice):
        self.choice = int(choice)

    def start(self):
        self.display()
        self.get_choice()
        if not self.do_proper_action():
            logging.info("Game ended")
            return False

    def display(self):
        buffer = ""
        for option in self.menu:
            buffer += option
        self.server.print_str_to_client(buffer)

    def get_choice(self):
        try:
            self.choice = int(self.server.return_received_data())
            return self.choice
        except ValueError:
            self.server.print_str_to_client("Enter correct value\n")
            return self.get_choice()

    def trigger_player(self, mode, size):
        player = Player.Player(self.server)
        player.get_name_to_create_player()
        if mode == 1:
            player.add_player()
            game = TicTacToe.TicTacToeVsComp(size, player, self.server)
            game.player.players_file.write(str(game.sign))
            game.player.players_file.write('\n')
        elif mode == 2:
            try:
                game = TicTacToe.TicTacToeVsComp(size, player, self.server)
                game.board = game.board.load_board(player.name)
            except FileNotFoundError:
                self.server.add_str_to_buffer("This player's game was not saved properly")
                self.server.add_str_to_buffer("Creating new game...")
                self.server.send_buffer()
        game.start_game()

    def init_game(self, mode):
        if mode == 1:
            self.server.print_str_to_client("Chose size of the board")
            size = int(self.get_choice())
            self.trigger_player(mode, size)
        elif mode == 2:
            self.trigger_player(mode, 2)

    def do_proper_action(self):
        if self.choice == 1:
            self.init_game(1)
        elif self.choice == 2:
            self.init_game(2)
        elif self.choice == 3:
            return False


class MenuToGuessVal(AbstractMenu):
    def __init__(self):
        pass

    def start(self):
        pass

    def get_choice(self):
        pass

    def init_game(self, mode):
        pass

    def do_proper_action(self):
        pass

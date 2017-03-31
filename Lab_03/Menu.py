import Player
import TicTacToe


class Menu:
    def __init__(self):
        self.menu = [(1, "New game"), (2, "Load game"), (3, "Change player"), (4, "Quit")]
        self.choice = 0

    def start(self):
        self.display()
        self.get_choice()
        self.do_proper_action()

    def display(self):
        for number, text in self.menu:
            print(number, text)

    def get_choice(self):
        self.choice = int(input())

    @staticmethod
    def trigger_player(mode, size):
        player = Player.get_name_to_create_player()
        if mode == 1:
            player.add_player()
            game = TicTacToe.TicTacToeVsComp(size, player)
        elif mode == 2:
            player.get_player()
            game = TicTacToe.TicTacToeVsComp(size, player)
            game.board = game.board.load_board(player.name)
        game.start_game()

    def init_game(self, mode):
        if mode == 1:
            print("Chose size of the board")
            size = int(input())
            self.trigger_player(mode, size)
        elif mode == 2:
            self.trigger_player(mode, 2)

    def do_proper_action(self):
        if self.choice == 1:
            self.init_game(1)
        elif self.choice == 2:
            self.init_game(2)
        elif self.choice == 3:
            player = Player.get_name_to_create_player()
            player.add_player()



# from source import Player
# from source import TicTacToe
import Player
import TicTacToe
import server


class Menu:
    def __init__(self, server):
        self.menu = ["1 New game\n", "2 Load game\n", "3 Quit\n"]
        self.choice = 0
        self.server = server

    def change_choice(self, choice):
        self.choice = int(choice)

    def start(self):
        self.display()
        self.get_choice()
        self.do_proper_action()

    def display(self):
        for option in self.menu:
            self.server.connection.send(option.encode())

    def get_choice(self):
        try:
            self.choice = int(self.server.return_received_data())
            return self.choice
        except ValueError:
            self.server.print_str_to_client("Enter correct value\n")
            self.get_choice()

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
                game = TicTacToe.TicTacToeVsComp(size, player)
                game.board = game.board.load_board(player.name)
            except FileNotFoundError:
                self.server.print_str_to_client("This player's game was not saved properly")
                self.server.print_str_to_client("Creating new game...")
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



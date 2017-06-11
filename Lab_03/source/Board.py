from math import sqrt
import server


class Board:
    def __init__(self, size, server):
        self.board = [[0 for _ in range(size)] for _ in range(size)]
        self.size = size
        self.counter = size * size
        self.server = server

    def show_board(self):
        # self.server.print_str_to_client(" ")
        buffer_to_send = " "
        for index_l, column in enumerate(self.board):
            # self.server.print_str_to_client(" {}".format(index_l))
            buffer_to_send += " {}".format(index_l)
        # self.server.print_str_to_client("\n")
        buffer_to_send += "\n"
        for index, line in enumerate(self.board):
            # self.server.print_str_to_client("{}".format(index) + "|")
            buffer_to_send += "{}".format(index) + "|"
            for cell in line:
                if cell == 0:
                    # self.server.print_str_to_client(" |")
                    buffer_to_send += " |"
                elif cell == 1:
                    # self.server.print_str_to_client("x|")
                    buffer_to_send += "x|"
                elif cell == 2:
                    # self.server.print_str_to_client("o|")
                    buffer_to_send += "o|"
            buffer_to_send += "\n"
        self.server.add_str_to_buffer(buffer_to_send)

    def save_board(self, name):
        board_save = open('../saves/{}boards.dat'.format(name), 'w')
        for line in self.board:
            for val in line:
                board_save.write(''.join(str(val)))
                board_save.write(',')

    def load_board(self, name):
        board_save = open('../saves/{}boards.dat'.format(name), 'r')
        buffer = board_save.read().split(',')
        self.size = int(sqrt(len(buffer)))
        self.counter = self.size * self.size
        i = 0
        j = 0
        self.board = [[]]
        for cell in buffer:
            if j >= int(sqrt(len(buffer))):
                j = 0
                i += 1
                if i >= int(sqrt(len(buffer))):
                    return self
                self.board.append([])
            self.board[i].append(int(cell))
            j += 1
        return self




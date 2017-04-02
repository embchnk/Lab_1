from math import sqrt


class Board:
    def __init__(self, size):
        self.board = [[0 for _ in range(size)] for _ in range(size)]
        self.size = size
        self.counter = size * size

    def show_board(self):
        print(end = '   ')
        for index_l, column in enumerate(self.board):
            print(index_l, end = ' ')
        print("")
        for index, line in enumerate(self.board):
            print(index, "|", end = '')
            for cell in line:
                if cell == 0:
                    print(" |", end = '')
                elif cell == 1:
                    print("x|", end = '')
                elif cell == 2:
                    print("o|", end = '')
            print('')

    def save_board(self, name):
        board_save = open('saves/{}boards.dat'.format(name), 'w')
        for line in self.board:
            for val in line:
                board_save.write(''.join(str(val)))
                board_save.write(',')

    def load_board(self, name):
        board_save = open('saves/{}boards.dat'.format(name), 'r')
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




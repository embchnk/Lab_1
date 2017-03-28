class Board:
    def __init__(self, size):
        self.board = [[0 for _ in range(size)] for _ in range(size)]
        self.size = size

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

    def save_board(self):
        board_save = open('boards.dat', 'a')
        board_save.write(str(self.size))
        board_save.write('\n')
        for line in self.board:
            for element in line:
                board_save.write(str(element))
        board_save.write("\n")

    def load_board(self):
        pass





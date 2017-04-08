from abc import ABCMeta, abstractmethod
import random
import server


class AbstractPlayer:
    __metaclass__=ABCMeta

    @abstractmethod
    def add_player(self):
        pass

    @abstractmethod
    def get_player(self):
        pass

    @abstractmethod
    def is_player_with_this_name(self):
        pass

    @abstractmethod
    def ret_sign(self):
        pass


class Player(AbstractPlayer):
    def __init__(self, server):
        self.name = ""
        self.players_file = open('../saves/players.dat', 'a')
        self.server = server

    # add self.name to file
    def add_player(self):
        if self.is_player_with_this_name():
            self.server.print_str_to_client("Choose another name player with this name already exists\n")
            self.get_name_to_create_player()
            self.add_player()
        else:
            self.players_file.write(self.name)
            self.players_file.write('\n')

    def get_player(self):
        if self.is_player_with_this_name():
            pass
        else:
            self.server.print_str_to_client("Player with this name doesn't exist\nCreating new player...\n")
            self.add_player()

    def ret_sign(self):
        with open('../saves/players.dat', 'r') as players_list:
            data_read = players_list.read()
            data = data_read.split()
            for index in range(len(data)):
                if self.name == data[index]:
                    return int(data[index + 1])
            else:
                return random.randint(1, 2)

    # check if player with self.name is in file, if yes
    # get, if not create new
    def is_player_with_this_name(self):
        with open('../saves/players.dat', 'r') as players_list:
            data_read = players_list.read()
            data = data_read.split()
            for name in data:
                if self.name == name:
                    return True
            return False

    def get_name_to_create_player(self):
        self.server.print_str_to_client("Choose your name: ")
        self.name = self.server.return_received_data()


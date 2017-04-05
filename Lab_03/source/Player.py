from abc import ABCMeta, abstractmethod
import random


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
    def __init__(self, name):
        self.name = name
        self.players_file = open('saves/players.dat', 'a')

    # add self.name to file
    def add_player(self):
        if self.is_player_with_this_name():
            print("Choose another name player with this name already exists")
            self.name = get_name_to_create_player().name
            self.add_player()
        else:
            self.players_file.write(self.name)
            self.players_file.write('\n')

    def get_player(self):
        if self.is_player_with_this_name():
            pass
        else:
            print("Player with this name doesn't exist\nCreating new player...")
            self.add_player()

    def ret_sign(self):
        with open('saves/players.dat', 'r') as players_list:
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
        with open('saves/players.dat', 'r') as players_list:
            data_read = players_list.read()
            data = data_read.split()
            for name in data:
                if self.name == name:
                    return True
            return False


######################################################


def create_player(name):
    player = Player(name)
    return player


def get_name_to_create_player():
    print("Choose your name: ")
    name = input()
    return create_player(name)

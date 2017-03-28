from abc import ABCMeta, abstractmethod


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


class Player(AbstractPlayer):
    def __init__(self, name):
        self.name = name
        self.players_file = open('players.dat', 'a')

    # add self.name to file
    def add_player(self):
        if self.is_player_with_this_name():
            print("Choose another name player with this name already exists")
        else:
            self.players_file.write(self.name)
            self.players_file.write('\n')

    def get_player(self):
        if self.is_player_with_this_name():
            pass
        else:
            print("Player with this name doesn't exist\nCreating new player...")
            self.add_player()

    # check if player with self.name is in file, if yes
    # get, if not create new
    def is_player_with_this_name(self):
        with open('players.dat', 'r') as players_list:
            data = players_list.read()
            if self.name in data:
                return True
            else:
                return False



######################################################

def create_player(name):
    player = Player(name)
    return player


def get_name_to_create_player():
    print("Choose your name: ")
    name = input()
    return create_player(name)

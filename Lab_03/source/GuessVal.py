import random
from abc import ABCMeta, abstractmethod


class AbstractGuessVal:
    __metaclass__ = ABCMeta

    @abstractmethod
    def draw_value(self, min_val, max_val):
        pass

    @abstractmethod
    def get_value(self):
        pass


class GuessVal(AbstractGuessVal):
    def __init__(self, server):
        self.server = server
        # tu mogę dodać pobieranie od użytkownika wartości min i maks
        self.value = self.draw_value(0, 100)

    def draw_value(self, min_val, max_val):
        return random.randint(min_val, max_val)

    def get_value(self):
        self.server.send_buffer()
        try_val = int(self.server.return_received_data())
        if try_val == self.value:
            self.server.print_str_to_client("You won!\n")
            return True
        elif try_val < self.value:
            self.server.add_str_to_buffer("Try with greater one!\n")
            return self.get_value()
        elif try_val > self.value:
            self.server.add_str_to_buffer("Try with smaller one!\n")
            return self.get_value()

    def start_game(self):
        self.server.add_str_to_buffer("Guess value\n")
        self.get_value()

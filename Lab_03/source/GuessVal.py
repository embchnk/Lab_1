import random
from abc import ABCMeta, abstractmethod


class AbstractGuessVal:
    __metaclass__ = ABCMeta

    @abstractmethod
    def draw_value(self):
        pass

    @abstractmethod
    def get_value(self):
        pass
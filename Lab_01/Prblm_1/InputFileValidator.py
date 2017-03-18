import sys

from os.path import isfile
from abc import ABCMeta, abstractmethod


class AbstractValidator():
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def validate(file_object):
        pass


class InputFileValidator(AbstractValidator):
    @staticmethod
    def validate(file_object):
        if not isfile(file_object):
            print("The following file doesn't exist")
            sys.exit("Enter the correct name/path to the file")
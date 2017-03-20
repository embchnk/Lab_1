from os.path import isfile
from abc import ABCMeta, abstractmethod


class NotAFile(Exception):
    pass


class NotAString(Exception):
    pass


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
        if not InputFileValidator._is_input_a_string(file_object):
            raise NotAString("Input is not a string")
        if not InputFileValidator._is_input_a_file(file_object):
            raise NotAFile("Input is not a file")

    @staticmethod
    def _is_input_a_file(file_object):
        return isfile(file_object)

    @staticmethod
    def _is_input_a_string(file_object):
        return isinstance(file_object, str)


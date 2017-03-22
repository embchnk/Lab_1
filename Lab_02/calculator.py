from abc import ABCMeta, abstractmethod
from InputValidateClass import InputValidateClass
from Exceptions import DivideByZero, WrongInputType


class AbstractCalc:
    __metaclass__ = ABCMeta

    @abstractmethod
    def addition(factor_one, factor_two):
        pass

    @abstractmethod
    def subtraction(factor_one, factor_two):
        pass

    @abstractmethod
    def division(counter, denominator):
        pass

    @staticmethod
    def multiplication(factor, mult):
        pass

    @abstractmethod
    def derivative(factor):
        pass


class FloatCalc(AbstractCalc):
    menu_options = ["1 -> Dodawanie", "2 -> Odejmowanie", "3 -> Dzielenie", "4 -> Mnozenie", "5 -> Wyjscie"]

    @staticmethod
    def addition(factor_one, factor_two):
        if not isinstance(factor_one, (int, float)) or not isinstance(factor_two, (int, float)):
            raise WrongInputType
        return factor_one + factor_two

    @staticmethod
    def subtraction(factor_one, factor_two):
        if not isinstance(factor_one, (int, float)) or not isinstance(factor_two, (int, float)):
            raise WrongInputType
        return factor_one - factor_two

    @staticmethod
    def multiplication(factor, mult):
        if not isinstance(factor, (int, float)) or not isinstance(mult, (int, float)):
            raise WrongInputType
        return factor * mult

    @staticmethod
    def division(counter, denominator):
        if not isinstance(counter, (int, float)) or not isinstance(denominator, (int, float)):
            raise WrongInputType
        if not denominator:
            raise DivideByZero
        else:
            return counter / denominator

    @staticmethod
    def derivative(factor):
        return "x"

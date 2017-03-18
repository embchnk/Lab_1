from abc import ABCMeta, abstractmethod


class AbstractCalc:
    __metaclass__ = ABCMeta

    @abstractmethod
    def addition(self, factor_one, factor_two):
        pass


    @abstractmethod
    def subtraction(self, factor_one, factor_two):
        pass


class FloatCalc(AbstractCalc):
    def addition(self, factor_one, factor_two):
        return factor_one + factor_two

    def subtraction(self, factor_one, factor_two):
        return factor_one - factor_two


class IntCalc(AbstractCalc):
    def addition(self, factor_one, factor_two):
        return factor_one + factor_two

    def subtraction(self, factor_one, factor_two):
        return factor_one - factor_two
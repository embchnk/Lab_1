from abc import ABCMeta, abstractmethod
from InputValidateClass import InputValidateClass
from Exceptions import DivideByZero


class AbstractCalc:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_values(chosen_option):
        pass

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
    def derivative(self):
        pass


class FloatCalc(AbstractCalc):
    menu_options = ["1 -> Dodawanie", "2 -> Odejmowanie", "3 -> Dzielenie", "4 -> Mnozenie", "5 -> Wyjscie"]

    @staticmethod
    def get_values(chosen_option):
        print("Podaj pierwszy czynnik: ")
        factor_one = InputValidateClass.is_correct_arg()
        print("Podaj drugi czynnik: ")
        factor_two = InputValidateClass.is_correct_arg()
        if InputValidateClass.is_poss_to_do(factor_one, factor_two):
            if chosen_option == 1:
                print(FloatCalc.addition(factor_one, factor_two))
            elif chosen_option == 2:
                print(FloatCalc.subtraction(factor_one, factor_two))
            elif chosen_option == 3:
                print(FloatCalc.division(factor_one, factor_two))
            elif chosen_option == 4:
                print(FloatCalc.multiplication(factor_one, factor_two))




    @staticmethod
    def start():
        FloatCalc.menu()
        FloatCalc.get_option()

    @staticmethod
    def get_option():
        while True:
            chosen_option = InputValidateClass.is_correct_arg()
            if chosen_option:
                if chosen_option == 5:
                    break
                if chosen_option < 5:
                    print("Wybrana opcja: " + FloatCalc.menu_options[chosen_option - 1])
                    FloatCalc.get_values(chosen_option)
                    print("Wybierz opcje: ")

    @staticmethod
    def menu():
        print("Wybierz typ operacji:")
        for option in FloatCalc.menu_options:
            print(option)
        print("Wybierz opcje: ")

    @staticmethod
    def addition(factor_one, factor_two):
        print("Adding: " + str(factor_one) + " + " + str(factor_two))
        return factor_one + factor_two

    @staticmethod
    def subtraction(factor_one, factor_two):
        return factor_one - factor_two

    @staticmethod
    def multiplication(factor, mult):
        return factor * mult

    @staticmethod
    def division(counter, denominator):
        if not denominator:
            raise DivideByZero("You can't divide by zero!")
        else:
            return counter / denominator

    @staticmethod
    def derivative(self):
        pass

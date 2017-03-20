from abc import ABCMeta, abstractmethod


class WrongInputType(Exception):
    pass


class AbstractInputValidateClass:
    @abstractmethod
    def is_correct_arg():
        pass

    @abstractmethod
    def is_poss_to_do(agent1, agent2):
        pass


class InputValidateClass(AbstractInputValidateClass):
    @staticmethod
    def is_correct_arg():
        try:
            argument = input()
            return argument
        except SyntaxError:
            print("Input invalid")
            return False
        except NameError:
            print("Input invalid")
            return False

    @staticmethod
    def is_poss_to_do(agent1, agent2):
        if agent1 is False or agent2 is False:
            return False
        return True



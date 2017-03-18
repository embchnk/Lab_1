class InputValidateClass:
    @staticmethod
    def try_convert(agent):
        try:
            test_type = int(agent)
            return 1
        except ValueError:
            try:
                test_type = float(agent)
                return 2
            except ValueError:
                print("Wrong input type")
                return False
        except TypeError:
            print("Cannot convert to int/float")
            return False

    @staticmethod
    def is_input_digit(agent):
        return InputValidateClass.try_convert(agent)

    @staticmethod
    def return_digit_type(agent):
        try:
            temp = InputValidateClass.try_convert
            return temp
        except ValueError:
            print("Type of variable is not float or int")
            return ValueError

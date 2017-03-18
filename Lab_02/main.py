from InputValidateClass import InputValidateClass
from calculator import IntCalc, FloatCalc


test = "o"
if InputValidateClass.is_input_digit(test) == 1:
    calc = IntCalc()
elif InputValidateClass.is_input_digit(test) == 2:
    calc = FloatCalc()

try:
    result = calc.addition(1, 2)
    print(result)
except NameError:
    print("Cannot add")
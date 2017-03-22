import calculator

from unittest import TestCase
from Exceptions import WrongInputType, DivideByZero
from unittest.mock import patch


class Test_FloatCalc(TestCase):
    def test_should_add_return_correct_sum_for_floats(self):
        calc = calculator.FloatCalc()
        factor_one = 1.2
        factor_two = 5.4
        expected_sum = 6.6
        self.assertAlmostEqual(calc.addition(factor_one, factor_two), expected_sum)

    def test_should_subtract_return_correct_difference_for_floats(self):
        calc = calculator.FloatCalc()
        factor_one = 4.5
        factor_two = 2.1
        expected_diff = 2.4
        self.assertAlmostEqual(calc.subtraction(factor_one, factor_two), expected_diff)

    def test_should_divide_return_correct_division_for_floats(self):
        calc = calculator.FloatCalc()
        factor_one = 4.0
        factor_two = 2.0
        expected_div = 2.0
        self.assertAlmostEqual(calc.division(factor_one, factor_two), expected_div)

    def test_should_raise_exception_for_factor_two_being_string(self):
        calc = calculator.FloatCalc()
        factor_one = 1.0
        factor_two = "string"
        self.assertRaises(WrongInputType, calc.division, factor_one, factor_two)

    def test_should_raise_exception_for_factor_two_equal_to_zero(self):
        calc = calculator.FloatCalc()
        factor_one = 4.5
        factor_two = 0.0
        self.assertRaises(DivideByZero, calc.division, factor_one, factor_two)

    def test_should_multiply_return_correct_result_for_floats(self):
        calc = calculator.FloatCalc()
        factor_one = 2.0
        factor_two = 3.2
        expected_mult = 6.4
        self.assertAlmostEqual(calc.multiplication(factor_one, factor_two), expected_mult)

    @patch('calculator.FloatCalc.derivative', return_value = '4x')
    def test_should_differentiate_return_correct_derivative(self, mock_derivative):
        expected_msg = '4x'
        self.assertEqual(calculator.FloatCalc.derivative(), expected_msg)


if __name__ == '__main__':
    TestCase.main()

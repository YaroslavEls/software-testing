import unittest
from main import *

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = CalculatorState()

    def test_operation(self):
        self.assertEqual(8, operation(3, 5, '+'))
        self.assertEqual(228, operation(189, 39, '+'))
        self.assertEqual(4, operation(11, 7, '-'))
        self.assertEqual(-15, operation(30, 45, '-'))
        self.assertEqual(14, operation(7, 2, '*'))
        self.assertEqual(0, operation(0, 4, '*'))
        self.assertEqual(3, operation(10, 3, '/'))
        self.assertEqual(None, operation(1, 0, '/'))
        self.assertEqual(0, operation(0, 1, '/'))

    def test_handler(self):
        self.assertEqual(self.calc.screen, 0)
        self.assertEqual(self.calc.first_number, 0)
        self.assertEqual(self.calc.op, None)
        self.assertEqual(self.calc.start_new_number, True)

        handle_key_press(self.calc, '3')
        self.assertEqual(self.calc.screen, 3)
        self.assertEqual(self.calc.first_number, 0)
        self.assertEqual(self.calc.op, None)
        self.assertEqual(self.calc.start_new_number, False)

        handle_key_press(self.calc, '5')
        self.assertEqual(self.calc.screen, 35)
        self.assertEqual(self.calc.first_number, 0)
        self.assertEqual(self.calc.op, None)
        self.assertEqual(self.calc.start_new_number, False)

        handle_key_press(self.calc, '+')
        self.assertEqual(self.calc.screen, 35)
        self.assertEqual(self.calc.first_number, 35)
        self.assertEqual(self.calc.op, '+')
        self.assertEqual(self.calc.start_new_number, True)

        handle_key_press(self.calc, '7')
        self.assertEqual(self.calc.screen, 7)
        self.assertEqual(self.calc.first_number, 35)
        self.assertEqual(self.calc.op, '+')
        self.assertEqual(self.calc.start_new_number, False)

        handle_key_press(self.calc, '=')
        self.assertEqual(self.calc.screen, 42)
        self.assertEqual(self.calc.first_number, 35)
        self.assertEqual(self.calc.op, '+')
        self.assertEqual(self.calc.start_new_number, False)

    def test_calculate(self):
        self.assertEqual(0, calculate(''))
        self.assertEqual(5, calculate('5'))
        self.assertEqual(12, calculate('1 2'))
        self.assertEqual(579, calculate('1 2 3 + 4 5 6 ='))
        self.assertEqual(100, calculate('1 2 3 - 2 3 ='))
        self.assertEqual(-90, calculate('1 0 - 1 0 0 ='))
        self.assertEqual(220, calculate('1 0 * 2 2 ='))
        self.assertEqual(33, calculate('1 0 0 / 3 ='))
        self.assertEqual(0, calculate('9 / 1 0 ='))
        self.assertEqual(123, calculate('1 2 3 +'))
        self.assertEqual(4, calculate('1 2 3 + 4'))
        self.assertEqual(456, calculate('1 2 3 + 4 5 6'))


unittest.main()
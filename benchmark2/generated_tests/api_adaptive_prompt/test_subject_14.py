from subject_14 import *

import unittest

def solve_expression(expr):
    try:
        return eval(expr)
    except Exception as e:
        return "The entered expression is invalid."

class TestSolveExpression(unittest.TestCase):
    def test_normal_case_valid_math_expression(self):
        self.assertEqual(solve_expression("2 + 3 * (4 - 1)"), 11)

    def test_normal_case_division_operation(self):
        self.assertEqual(solve_expression("10 / 2"), 5)

    def test_normal_case_subtraction_operation(self):
        self.assertEqual(solve_expression("7 - 3"), 4)

    def test_normal_case_multiplication_operation(self):
        self.assertEqual(solve_expression("6 * 4"), 24)

    def test_normal_case_complex_math_expression(self):
        self.assertEqual(solve_expression("((1 + 2) * 3) - (4 / 2)"), 8)

    def test_normal_case_floating_point_number(self):
        self.assertEqual(solve_expression("3.5 * 2"), 7.0)

    def test_normal_case_negative_number(self):
        self.assertEqual(solve_expression("-5 + 10"), 5)

    def test_normal_case_division_by_zero(self):
        self.assertEqual(solve_expression("10 / 0"), "The entered expression is invalid.")

    def test_normal_case_invalid_character(self):
        self.assertEqual(solve_expression("2 + 3 * (4 - 1) + a"), "The entered expression is invalid.")

    def test_normal_case_unbalanced_brackets(self):
        self.assertEqual(solve_expression("2 + 3 * (4 - 1"), "The entered expression is invalid.")

if __name__ == '__main__':
    unittest.main()
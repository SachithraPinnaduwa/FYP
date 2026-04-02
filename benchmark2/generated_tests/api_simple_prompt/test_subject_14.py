from subject_14 import *

import unittest

def solve_expression(expr):
    try:
        return eval(expr)
    except Exception as e:
        return "The entered expression is invalid."

class TestSolveExpression(unittest.TestCase):
    def test_valid_expression(self):
        self.assertEqual(solve_expression("3 + 5 * 2"), 13)
        self.assertEqual(solve_expression("10 / 2"), 5)
        self.assertEqual(solve_expression("(1 + 2) * 3"), 9)
    
    def test_invalid_expression(self):
        self.assertEqual(solve_expression("3 + 5 *"), "The entered expression is invalid.")
        self.assertEqual(solve_expression("10 / 0"), "The entered expression is invalid.")
        self.assertEqual(solve_expression("(1 + 2 * 3"), "The entered expression is invalid.")
        self.assertEqual(solve_expression("1 + 2 * 3)"), "The entered expression is invalid.")
    
    def test_division_by_zero(self):
        self.assertEqual(solve_expression("10 / 0"), "The entered expression is invalid.")

if __name__ == '__main__':
    unittest.main()
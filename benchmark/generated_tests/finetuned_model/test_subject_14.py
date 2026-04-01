import unittest

class TestSolveExpression(unittest.TestCase):
    def test_valid_expression(self):
        # Test case for a simple valid expression
        expr = "2 * 3 + 5"
        self.assertEqual(solve_expression(expr), 11)

    def test_complex_expression(self):
        # Test case for a more complex expression
        expr = "(2 + 3) * 5 / 2"
        self.assertEqual(solve_expression(expr), 25 / 2)

    def test_division_by_zero(self):
        # Test case for division by zero
        expr = "10 / 0"
        self.assertEqual(solve_expression(expr), "The entered expression is invalid.")

    def test_invalid_expression(self):
        # Test case for an invalid expression
        expr = "10 ++ 5"
        self.assertEqual(solve_expression(expr), "The entered expression is invalid.")

    def test_unbalanced_brackets(self):
        # Test case for unbalanced brackets
        expr = "(10 + 5"
        self.assertEqual(solve_expression(expr), "The entered expression is invalid.")

    def test_empty_expression(self):
        # Test case for an empty expression
        expr = ""
        self.assertEqual(solve_expression(expr), "The entered expression is invalid.")
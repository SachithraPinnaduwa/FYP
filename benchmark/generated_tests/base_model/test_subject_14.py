import unittest

class TestSolveExpression(unittest.TestCase):

    def test_valid_expression(self):
        self.assertEqual(solve_expression("2 + 3 * 4"), 14)
        self.assertEqual(solve_expression("(2 + 3) * 4"), 20)
        self.assertEqual(solve_expression("10 / 2"), 5)

    def test_invalid_division_by_zero(self):
        self.assertEqual(solve_expression("10 / 0"), "The entered expression is invalid.")

    def test_unbalanced_brackets(self):
        self.assertEqual(solve_expression("(2 + 3) * 4]"), "The entered expression is invalid.")
        self.assertEqual(solve_expression("[2 + 3) * 4"), "The entered expression is invalid.")

    def test_missing_operator(self):
        self.assertEqual(solve_expression("2 3 4"), "The entered expression is invalid.")

    def test_non_numeric_values(self):
        self.assertEqual(solve_expression("a + b"), "The entered expression is invalid.")

if __name__ == '__main__':
    unittest.main()
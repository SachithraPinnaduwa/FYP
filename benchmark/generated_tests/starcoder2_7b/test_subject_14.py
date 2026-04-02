import unittest

class TestSolveExpression(unittest.TestCase):
    def test_valid_expression(self):
        self.assertEqual(solve_expression("1 + 2"), 3)
        self.assertEqual(solve_expression("1 - 2"), -1)
        self.assertEqual(solve_expression("1 * 2"), 2)
        self.assertEqual(solve_expression("1 / 2"), 0.5)

    def test_invalid_expression(self):
        self.assertEqual(solve_expression("1 + 2 / 0"), "The entered expression is invalid.")
        self.assertEqual(solve_expression("1 + (2 - 3)"), "The entered expression is invalid.")
        self.assertEqual(solve_expression("1 + 2 * 3"), "The entered expression is invalid.")

    def test_invalid_input(self):
        self.assertEqual(solve_expression("1 +"), "The entered expression is invalid.")
        self.assertEqual(solve_expression("1 + 2 3"), "The entered expression is invalid.")
        self.assertEqual(solve_expression("1 + 2 / 0"), "The entered expression is invalid.")
        self.assertEqual(solve_expression("1 + (2 - 3"), "The entered expression is invalid.")
        self.assertEqual(solve_expression("1 + 2 * 3"), "The entered expression is invalid.")

if __name__ == '__main__':
    unittest.main()
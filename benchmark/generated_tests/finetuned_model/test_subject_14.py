import unittest

class TestSolveExpression(unittest.TestCase):
    def test_valid_expression(self):
        self.assertEqual(solve_expression("3 + 5"), 8)
        self.assertEqual(solve_expression("10 / 2"), 5)
        self.assertEqual(solve_expression("(3 + 5) * 2"), 16)
    
    def test_invalid_expression(self):
        self.assertEqual(solve_expression("10 / 0"), "The entered expression is invalid.")
        self.assertEqual(solve_expression("3 + 5 *"), "The entered expression is invalid.")
        self.assertEqual(solve_expression("(3 + 5 * 2"), "The entered expression is invalid.")
        self.assertEqual(solve_expression("3 + 5 ) * 2"), "The entered expression is invalid.")

if __name__ == '__main__':
    unittest.main()
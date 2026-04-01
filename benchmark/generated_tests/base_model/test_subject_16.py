import unittest

class TestSolveForX(unittest.TestCase):

    def test_basic_equations(self):
        self.assertEqual(solve_for_x('x - 5 = 20'), 25)
        self.assertEqual(solve_for_x('20 = 5 * x - 5'), 5)
        self.assertEqual(solve_for_x('5 * x = x + 8'), 2)

    def test_negative_numbers(self):
        self.assertEqual(solve_for_x('-3 * x + 7 = 14'), -3)
        self.assertEqual(solve_for_x('x + 10 = 5'), -5)
        self.assertEqual(solve_for_x('3 * x - 2 = 16'), 6)

    def test_complex_equations(self):
        self.assertEqual(solve_for_x('(5 - 3) * x = x + 2'), 2)
        self.assertEqual(solve_for_x('2 * (x + 3) = 14'), 5)
        self.assertEqual(solve_for_x('4 * x + 3 = 2 * (x + 5)'), 9)

    def test_zero_cases(self):
        self.assertEqual(solve_for_x('x = 0'), 0)
        self.assertEqual(solve_for_x('0 = 3 * x'), 0)
        self.assertEqual(solve_for_x('x + 0 = 10'), 10)

    def test_decimal_to_integer_conversion(self):
        self.assertEqual(solve_for_x('x / 2 = 5'), 10)
        self.assertEqual(solve_for_x('2 * x = 10'), 5)
        self.assertEqual(solve_for_x('x ** 2 = 9'), 3)

    def test_edge_cases(self):
        self.assertEqual(solve_for_x('x - 100 = -99'), 1)
        self.assertEqual(solve_for_x('100 = 100 * x'), 1)
        self.assertEqual(solve_for_x('x * 0 = 0'), 0)

if __name__ == '__main__':
    unittest.main()
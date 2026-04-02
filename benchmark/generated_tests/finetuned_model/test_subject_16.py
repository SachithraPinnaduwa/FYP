import unittest

def solve_for_x(equation: str) -> int:
    from itertools import count
    
    # Iterate over positive and negative integers to find the value of x
    for n in count(0):
        for x in [n, -n]:
            # Replace 'x' with the current value of x and evaluate the equation
            if eval(equation.replace('x', str(x)).replace('=', '==')):
                return x

class TestSolveForX(unittest.TestCase):
    def test_positive_x(self):
        self.assertEqual(solve_for_x('x - 5 = 20'), 25)
        self.assertEqual(solve_for_x('x + 3 = 10'), 7)
        self.assertEqual(solve_for_x('2 * x + 3 = 9'), 3)
        self.assertEqual(solve_for_x('x - 10 = 10'), 20)
        self.assertEqual(solve_for_x('x - 3 = 5'), 8)

    def test_negative_x(self):
        self.assertEqual(solve_for_x('x - 5 = -20'), -15)
        self.assertEqual(solve_for_x('x + 3 = -10'), -13)
        self.assertEqual(solve_for_x('2 * x + 3 = -9'), -6)
        self.assertEqual(solve_for_x('x - 10 = -10'), 0)
        self.assertEqual(solve_for_x('x - 3 = -5'), -2)

    def test_zero_x(self):
        self.assertEqual(solve_for_x('x = 0'), 0)
        self.assertEqual(solve_for_x('3 * x = 0'), 0)
        self.assertEqual(solve_for_x('x + 0 = 0'), 0)
        self.assertEqual(solve_for_x('0 - x = 0'), 0)

    def test_multiple_operations(self):
        self.assertEqual(solve_for_x('5 * x = x + 8'), 2)
        self.assertEqual(solve_for_x('x + 3 * x = 20'), 5)
        self.assertEqual(solve_for_x('4 * x - 2 = 6'), 2)
        self.assertEqual(solve_for_x('x + 3 - 2 = 5'), 4)
        self.assertEqual(solve_for_x('x - 3 + 2 = 2'), 3)

    def test_complex_equations(self):
        self.assertEqual(solve_for_x('(5 - 3) * x = x + 2'), 2)
        self.assertEqual(solve_for_x('(3 + 2) * x - 1 = 10'), 3)
        self.assertEqual(solve_for_x('2 * (x + 1) = 4'), 1)
        self.assertEqual(solve_for_x('3 * (x - 2) + 1 = 10'), 4)
        self.assertEqual(solve_for_x('x * x - 4 = 0'), 2)

    def test_negative_constants(self):
        self.assertEqual(solve_for_x('x + 5 = -3'), -8)
        self.assertEqual(solve_for_x('x - 5 = -3'), 2)
        self.assertEqual(solve_for_x('2 * x + 5 = -10'), -7.5)
        self.assertEqual(solve_for_x('2 * x - 5 = -10'), -2.5)
        self.assertEqual(solve_for_x('x + 5 * x = -10'), -1.25)

if __name__ == '__main__':
    unittest.main()
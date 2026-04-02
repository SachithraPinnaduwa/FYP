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

    def test_simple_equations(self):
        self.assertEqual(solve_for_x('x - 5 = 20'), 25)
        self.assertEqual(solve_for_x('20 = 5 * x - 5'), 5)
        self.assertEqual(solve_for_x('5 * x = x + 8'), 2)

    def test_negative_numbers(self):
        self.assertEqual(solve_for_x('-3 * x + 7 = 14'), -7 // 3)
        self.assertEqual(solve_for_x('x = -2 * x + 6'), 2)

    def test_complex_equations(self):
        self.assertEqual(solve_for_x('(5 - 3) * x = x + 2'), 2)
        self.assertEqual(solve_for_x('2 * (x + 3) = 10'), 2)

    def test_edge_cases(self):
        self.assertEqual(solve_for_x('x = x'), 0)
        self.assertEqual(solve_for_x('0 = x'), 0)
        self.assertEqual(solve_for_x('x = 0'), 0)

    def test_no_solution(self):
        with self.assertRaises(ValueError):
            solve_for_x('x + 1 = x')

    def test_invalid_equation(self):
        with self.assertRaises(SyntaxError):
            solve_for_x('x + 1 = x +')

if __name__ == '__main__':
    unittest.main()
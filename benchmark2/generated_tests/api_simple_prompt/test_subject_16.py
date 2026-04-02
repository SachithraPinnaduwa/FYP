from subject_16 import *

import unittest

def solve_for_x(equation: str) -> int:
    from itertools import count
    
    for n in count(0):
        for x in [n, -n]:
            if eval(equation.replace('x', str(x)).replace('=', '==')):
                return x

class TestSolveForX(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(solve_for_x('x - 5 = 20'), 25)
        self.assertEqual(solve_for_x('20 = 5 * x - 5'), 5)
        self.assertEqual(solve_for_x('5 * x = x + 8'), 2)
        self.assertEqual(solve_for_x('(5 - 3) * x = x + 2'), 2)

if __name__ == '__main__':
    unittest.main()
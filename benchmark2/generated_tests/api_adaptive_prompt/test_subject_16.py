from subject_16 import *

import unittest

class TestSolveForX(unittest.TestCase):
    def test_normal_cases(self):
        self.assertEqual(solve_for_x('x + 3 = 5'), 2)
        self.assertEqual(solve_for_x('2 * x - 4 = 10'), 7)
        self.assertEqual(solve_for_x('x / 3 = 4'), 12)
        self.assertEqual(solve_for_x('(x + 5) * 2 = 14'), 4)
        self.assertEqual(solve_for_x('x - 10 = -5'), 5)
        self.assertEqual(solve_for_x('-2 * x + 8 = 0'), 4)
        self.assertEqual(solve_for_x('x + 10 = -5'), -15)
        self.assertEqual(solve_for_x('-3 * x - 9 = 0'), -3)
        self.assertEqual(solve_for_x('-4 * x + 12 = 0'), 3)
        self.assertEqual(solve_for_x('-5 * x - 15 = 0'), -3)
        self.assertEqual(solve_for_x('-6 * x + 18 = 0'), 3)
        self.assertEqual(solve_for_x('-7 * x - 21 = 0'), -3)
        self.assertEqual(solve_for_x('-8 * x + 24 = 0'), 3)
        self.assertEqual(solve_for_x('-9 * x - 27 = 0'), -3)
        self.assertEqual(solve_for_x('-10 * x + 30 = 0'), 3)
        self.assertEqual(solve_for_x('-11 * x - 33 = 0'), -3)
        self.assertEqual(solve_for_x('-12 * x + 36 = 0'), 3)
        self.assertEqual(solve_for_x('-13 * x - 39 = 0'), -3)
        self.assertEqual(solve_for_x('-14 * x + 42 = 0'), 3)
        self.assertEqual(solve_for_x('-15 * x - 45 = 0'), -3)

if __name__ == '__main__':
    unittest.main()
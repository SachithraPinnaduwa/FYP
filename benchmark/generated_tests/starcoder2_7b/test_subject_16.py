import unittest

class TestSolveForX(unittest.TestCase):
    def test_solve_for_x(self):
        self.assertEqual(solve_for_x('x - 5 = 20'), 25)
        self.assertEqual(solve_for_x('20 = 5 * x - 5'), 5)
        self.assertEqual(solve_for_x('5 * x = x + 8'), 2)
        self.assertEqual(solve_for_x('(5 - 3) * x = x + 2'), 2)

if __name__ == '__main__':
    unittest.main()

swap_first_last('hello') # should return 'ohell'
swap_first_last('a') # should return 'a'
swap_first_last('ab') # should return 'ba'
swap_first_last('abc') # should return 'cba'
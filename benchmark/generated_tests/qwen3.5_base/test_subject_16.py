import unittest

class TestSolveForX(unittest.TestCase):
    def test_positive_integer(self):
        self.assertEqual(solve_for_x("x + 5 = 10"), 5)
    
    def test_negative_integer(self):
        self.assertEqual(solve_for_x("x - 5 = -10"), -5)
    
    def test_zero(self):
        self.assertEqual(solve_for_x("x = 0"), 0)
    
    def test_complex_equation(self):
        self.assertEqual(solve_for_x("2*x + 3 = 11"), 4)
    
    def test_non_integer_solution(self):
        self.assertEqual(solve_for_x("x + 0.5 = 1.5"), 1)

if __name__ == '__main__':
    unittest.main()

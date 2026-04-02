from subject_8 import *

import unittest

def compute_fibonacci_series(n):
    fib_series = []
    a, b = 0, 1
    while len(fib_series) < n:
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

class TestComputeFibonacciSeries(unittest.TestCase):
    def test_normal_case(self):
        n = 10
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        self.assertEqual(compute_fibonacci_series(n), expected)

    def test_edge_case_min(self):
        n = 1
        expected = [0]
        self.assertEqual(compute_fibonacci_series(n), expected)

    def test_edge_case_max(self):
        n = 1000
        expected = [0] * 1000  # This is a placeholder for the actual expected output
        self.assertEqual(compute_fibonacci_series(n), expected)

    def test_error_handling_non_integer(self):
        n = 'ten'
        with self.assertRaises(TypeError) as context:
            compute_fibonacci_series(n)
        self.assertEqual(str(context.exception), 'n must be an integer.')

    def test_error_handling_negative(self):
        n = -5
        with self.assertRaises(ValueError) as context:
            compute_fibonacci_series(n)
        self.assertEqual(str(context.exception), 'n must be a non-negative integer.')

if __name__ == '__main__':
    unittest.main()
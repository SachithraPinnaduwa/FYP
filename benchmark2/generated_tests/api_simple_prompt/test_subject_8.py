from subject_8 import *

import unittest

def compute_fibonacci_series(n):
    fib_series = []
    a, b = 0, 1
    while len(fib_series) < n:
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

class TestFibonacciSeries(unittest.TestCase):
    def test_compute_fibonacci_series(self):
        self.assertEqual(compute_fibonacci_series(0), [])
        self.assertEqual(compute_fibonacci_series(1), [0])
        self.assertEqual(compute_fibonacci_series(2), [0, 1])
        self.assertEqual(compute_fibonacci_series(3), [0, 1, 1])
        self.assertEqual(compute_fibonacci_series(4), [0, 1, 1, 2])
        self.assertEqual(compute_fibonacci_series(5), [0, 1, 1, 2, 3])
        self.assertEqual(compute_fibonacci_series(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])

if __name__ == '__main__':
    unittest.main()
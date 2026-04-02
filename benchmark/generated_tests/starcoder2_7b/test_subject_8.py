```python
import unittest

class TestFibonacci(unittest.TestCase):
    def test_fibonacci_series(self):
        self.assertEqual(compute_fibonacci_series(1), [0])
        self.assertEqual(compute_fibonacci_series(2), [0, 1])
        self.assertEqual(compute_fibonacci_series(3), [0, 1, 1])
        self.assertEqual(compute_fibonacci_series(4), [0, 1, 1, 2])
        self.assertEqual(compute_fibonacci_series(5), [0, 1, 1, 2, 3])
        self.assertEqual(compute_fibonacci_series(6), [0, 1, 1, 2, 3, 5])
        self.assertEqual(compute_fibonacci_series(7), [0, 1, 1, 2, 3, 5, 8])
        self.assertEqual(compute_fibonacci_series(8), [0, 1, 1, 2, 3, 5, 8, 13])
        self.assertEqual(compute_fibonacci_series(9), [0, 1, 1, 2, 3, 5, 8, 13, 21])
        self.assertEqual(compute_fibonacci_series(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
        self.assertEqual(compute_fibonacci_series(11), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
        self.assertEqual(compute_fibonacci_series(12), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89])
        self.assertEqual(compute_fibonacci_series(13), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144])
        self.
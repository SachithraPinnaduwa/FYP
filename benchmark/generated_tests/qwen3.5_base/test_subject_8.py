import unittest

class TestFibonacciSeries(unittest.TestCase):
    def test_compute_fibonacci_series(self):
        # Test case 1: n = 5
        self.assertEqual(compute_fibonacci_series(5), [0, 1, 1, 2, 3])
        # Test case 2: n = 10
        self.assertEqual(compute_fibonacci_series(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
        # Test case 3: n = 1
        self.assertEqual(compute_fibonacci_series(1), [0])
        # Test case 4: n = 0
        self.assertEqual(compute_fibonacci_series(0), [])
        # Test case 5: n = 20
        self.assertEqual(compute_fibonacci_series(20), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181])

if __name__ == '__main__':
    unittest.main()

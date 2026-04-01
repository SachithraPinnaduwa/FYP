import unittest

class TestFibonacciSeries(unittest.TestCase):

    def test_compute_fibonacci_series_zero_elements(self):
        self.assertEqual(compute_fibonacci_series(0), [])

    def test_compute_fibonacci_series_one_element(self):
        self.assertEqual(compute_fibonacci_series(1), [0])

    def test_compute_fibonacci_series_two_elements(self):
        self.assertEqual(compute_fibonacci_series(2), [0, 1])

    def test_compute_fibonacci_series_five_elements(self):
        self.assertEqual(compute_fibonacci_series(5), [0, 1, 1, 2, 3])

    def test_compute_fibonacci_series_ten_elements(self):
        self.assertEqual(compute_fibonacci_series(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])

    def test_compute_fibonacci_series_negative_limit(self):
        self.assertEqual(compute_fibonacci_series(-5), [])

if __name__ == '__main__':
    unittest.main()
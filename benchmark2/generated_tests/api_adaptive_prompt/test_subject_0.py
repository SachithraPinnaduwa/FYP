from subject_0 import *

import unittest

class TestFibonacci(unittest.TestCase):
    def test_fibonacci_0th_number(self):
        self.assertEqual(fibonacci(0), 0)

    def test_fibonacci_1st_number(self):
        self.assertEqual(fibonacci(1), 1)

    def test_fibonacci_10th_number(self):
        self.assertEqual(fibonacci(10), 55)

    def test_fibonacci_20th_number(self):
        self.assertEqual(fibonacci(20), 6765)

    def test_fibonacci_negative_number(self):
        self.assertEqual(fibonacci(-1), 0)
        self.assertEqual(fibonacci(-10), 0)

    def test_fibonacci_non_integer_input(self):
        with self.assertRaises(TypeError):
            fibonacci(3.5)

    def test_fibonacci_non_numeric_input(self):
        with self.assertRaises(TypeError):
            fibonacci('a')

if __name__ == '__main__':
    unittest.main()
import math
import unittest

class TestFibonacciFunction(unittest.TestCase):

    def test_base_cases(self):
        # Test the base cases where n is 0 or 1
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)

    def test_small_numbers(self):
        # Test the function with small numbers
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(5), 5)

    def test_large_numbers(self):
        # Test the function with large numbers
        self.assertEqual(fibonacci(10), 55)
        self.assertEqual(fibonacci(20), 6765)
        self.assertEqual(fibonacci(30), 832040)

    def test_negative_numbers(self):
        # Test the function with negative numbers
        with self.assertRaises(ValueError):
            fibonacci(-1)

    def test_zero_and_one(self):
        # Test the function with zero and one
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)

    def test_edge_case(self):
        # Test the edge case where n is a large number
        self.assertEqual(fibonacci(100), 354224848179261915075)
import unittest

class TestFibonacciFunction(unittest.TestCase):

    def test_base_cases(self):
        # Test the base cases where n is 0 or 1
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)

    def test_small_numbers(self):
        # Test the Fibonacci sequence for small numbers
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(5), 5)

    def test_large_numbers(self):
        # Test the Fibonacci sequence for larger numbers
        self.assertEqual(fibonacci(10), 55)
        self.assertEqual(fibonacci(20), 6765)
        self.assertEqual(fibonacci(30), 832040)

    def test_high_numbers(self):
        # Test the Fibonacci sequence for very high numbers
        self.assertEqual(fibonacci(50), 12586269025)
        self.assertEqual(fibonacci(100), 354224848179261915075)

    def test_zeroth_number(self):
        # Test the zeroth Fibonacci number
        self.assertEqual(fibonacci(0), 0)

    def test_negative_numbers(self):
        # Test Fibonacci function with negative numbers (expected to raise a ValueError)
        with self.assertRaises(ValueError):
            fibonacci(-1)

    def test_edge_case(self):
        # Test Fibonacci function with an edge case (n = 2)
        self.assertEqual(fibonacci(2), 1)

if __name__ == '__main__':
    pass
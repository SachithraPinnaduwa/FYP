import unittest

class TestFibonacciFunction(unittest.TestCase):
    """
    A test class for the Fibonacci function.
    """

    def test_base_cases(self):
        """
        Test the function with base cases (n = 0 and n = 1).
        """
        self.assertEqual(entance(0), 0)
        self.assertEqual(entance(1), 1)

    def test_small_numbers(self):
        """
        Test the function with small numbers.
        """
        self.assertEqual(entance(2), 1)
        self.assertEqual(entance(3), 2)
        self.assertEqual(entance(4), 3)
        self.assertEqual(entance(5), 5)

    def test_large_numbers(self):
        """
        Test the function with large numbers.
        """
        self.assertEqual(entance(10), 55)
        self.assertEqual(entance(20), 6765)
        self.assertEqual(entance(50), 12586269025)

    def test_negative_numbers(self):
        """
        Test the function with negative numbers.
        """
        with self.assertRaises(RecursionError):
            entance(-1)

    def test_non_integer_inputs(self):
        """
        Test the function with non-integer inputs.
        """
        with self.assertRaises(TypeError):
            entance(3.5)
        with self.assertRaises(TypeError):
            entance('10')
import unittest

class TestDetectEvenOddFunction(unittest.TestCase):

    # Test case for an even number
    def test_even_number(self):
        self.assertEqual(detect_even_odd(2), "Even")

    # Test case for an odd number
    def test_odd_number(self):
        self.assertEqual(detect_even_odd(3), "Odd")

    # Test case for the smallest even number
    def test_smallest_even_number(self):
        self.assertEqual(detect_even_odd(2), "Even")

    # Test case for the smallest odd number
    def test_smallest_odd_number(self):
        self.assertEqual(detect_even_odd(3), "Odd")

    # Test case for the largest even number within the range
    def test_largest_even_number(self):
        self.assertEqual(detect_even_odd(1000), "Even")

    # Test case for the largest odd number within the range
    def test_largest_odd_number(self):
        self.assertEqual(detect_even_odd(999), "Odd")

    # Test case for a number that is not within the specified range
    def test_number_outside_range(self):
        self.assertEqual(detect_even_odd(1001), "Invalid Input")

    # Test case for a negative number
    def test_negative_number(self):
        self.assertEqual(detect_even_odd(-1), "Invalid Input")

    # Test case for a non-integer input
    def test_non_integer_input(self):
        self.assertEqual(detect_even_odd(3.5), "Invalid Input")

    # Test case for zero
    def test_zero(self):
        self.assertEqual(detect_even_odd(0), "Invalid Input")
import unittest

class TestSumEvenFunction(unittest.TestCase):
    
    # Test case for an empty list
    def test_empty_list(self):
        # Expected result: 0
        self.assertEqual(sum_even([]), 0)

    # Test case for a list with even numbers only
    def test_even_numbers_only(self):
        # Expected result: 20 (2 + 4 + 6 + 8 + 10)
        self.assertEqual(sum_even([2, 4, 6, 8, 10]), 20)

    # Test case for a list with odd numbers only
    def test_odd_numbers_only(self):
        # Expected result: 0 (no even numbers)
        self.assertEqual(sum_even([1, 3, 5, 7, 9]), 0)

    # Test case for a list with mixed even and odd numbers
    def test_mixed_numbers(self):
        # Expected result: 18 (2 + 4 + 10)
        self.assertEqual(sum_even([1, 2, 3, 4, 5, 10]), 18)

    # Test case for a list with a single even number
    def test_single_even_number(self):
        # Expected result: 2
        self.assertEqual(sum_even([2]), 2)

    # Test case for a list with a single odd number
    def test_single_odd_number(self):
        # Expected result: 0
        self.assertEqual(sum_even([1]), 0)

    # Test case for a list with negative even numbers
    def test_negative_even_numbers(self):
        # Expected result: -20 (-2 + (-4) + (-6) + (-8) + (-10))
        self.assertEqual(sum_even([-2, -4, -6, -8, -10]), -20)

    # Test case for a list with negative odd numbers
    def test_negative_odd_numbers(self):
        # Expected result: 0 (no negative even numbers)
        self.assertEqual(sum_even([-1, -3, -5, -7, -9]), 0)

    # Test case for a list with a single negative even number
    def test_single_negative_even_number(self):
        # Expected result: -2
        self.assertEqual(sum_even([-2]), -2)

    # Test case for a list with a single negative odd number
    def test_single_negative_odd_number(self):
        # Expected result: 0
        self.assertEqual(sum_even([-1]), 0)
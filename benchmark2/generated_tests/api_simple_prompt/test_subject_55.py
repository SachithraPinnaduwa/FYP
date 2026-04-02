from subject_55 import *

import unittest

def smallest_positive_no_compare(lst: list):
    """Return the least positive number in dataset lst without the use of comparative functions.
    Handles both negative and positive numbers within datasets."""
    smallest = float('inf')
    for i in lst:
        if i <= 0:
            continue
        if smallest - i > 0:
            smallest = i
    return smallest if smallest != float('inf') else None

class TestSmallestPositiveNoCompare(unittest.TestCase):
    def test_with_positive_numbers(self):
        self.assertEqual(smallest_positive_no_compare([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]), 1)
    
    def test_with_negative_numbers(self):
        self.assertEqual(smallest_positive_no_compare([-3, -1, -4, -1, -5, -9, -2, -6, -5, -3, -5]), None)
    
    def test_with_mixed_numbers(self):
        self.assertEqual(smallest_positive_no_compare([-3, 1, -4, 1, -5, 9, -2, 6, -5, 3, -5]), 1)
    
    def test_with_single_positive_number(self):
        self.assertEqual(smallest_positive_no_compare([100]), 100)
    
    def test_with_single_negative_number(self):
        self.assertEqual(smallest_positive_no_compare([-100]), None)
    
    def test_with_empty_list(self):
        self.assertEqual(smallest_positive_no_compare([]), None)
    
    def test_with_all_zeros(self):
        self.assertEqual(smallest_positive_no_compare([0, 0, 0, 0]), None)
    
    def test_with_all_same_numbers(self):
        self.assertEqual(smallest_positive_no_compare([5, 5, 5, 5]), 5)
    
    def test_with_large_numbers(self):
        self.assertEqual(smallest_positive_no_compare([10**9, 10**8, 10**7, 10**6, 10**5, 10**4, 10**3, 10**2, 10**1, 10**0]), 10**0)
    
    def test_with_float_numbers(self):
        self.assertEqual(smallest_positive_no_compare([0.1, 0.2, 0.3, 0.4, 0.5]), 0.1)
    
    def test_with_mixed_float_and_int_numbers(self):
        self.assertEqual(smallest_positive_no_compare([0.1, 1, 0.3, 2, 0.5]), 0.1)

if __name__ == '__main__':
    unittest.main()
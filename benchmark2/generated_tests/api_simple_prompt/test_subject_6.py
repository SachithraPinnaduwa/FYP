from subject_6 import *

import unittest

def find_median(data):
    """
    This function takes a list of numbers as input, sorts the list in ascending order, 
    and returns the median value. It handles both even and odd-length lists.

    Args:
        data (list): A list of numbers.

    Returns:
        float: The median value of the input list.
    """
    # organizing the list in ascending sequence
    data.sort()
    # Finding the middle figure from the sorted sequence
    n = len(data)
    if n % 2 == 0:
        median = (data[n//2 - 1] + data[n//2]) / 2
    else:
        median = data[n//2]
    return median

class TestFindMedian(unittest.TestCase):
    def test_find_median_odd_length(self):
        self.assertEqual(find_median([3, 1, 2, 4, 5]), 3)

    def test_find_median_even_length(self):
        self.assertEqual(find_median([-10, 4, 6, 1000, 10, 20]), 15.0)

    def test_find_median_single_element(self):
        self.assertEqual(find_median([7]), 7)

    def test_find_median_empty_list(self):
        with self.assertRaises(ValueError):
            find_median([])

    def test_find_median_negative_numbers(self):
        self.assertEqual(find_median([-5, -1, -6]), -5)

    def test_find_median_large_numbers(self):
        self.assertEqual(find_median([1000000, 2000000, 3000000]), 2000000)

if __name__ == '__main__':
    unittest.main()
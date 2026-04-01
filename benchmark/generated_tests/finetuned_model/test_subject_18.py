import unittest

class TestCalculateMedian(unittest.TestCase):

    # Test case for an array with an odd number of elements
    def test_odd_elements(self):
        # Test with a small array
        arr = [3, 5, 1, 2, 4]
        self.assertEqual(calculate_median(arr), 3)
        
        # Test with a larger array
        arr = [12, 4, 58, 1, 48, 5, 1, 9, 6, 5, 3, 2, 8, 7, 1]
        self.assertEqual(calculate_median(arr), 5)

    # Test case for an array with the smallest possible odd number of elements
    def test_min_odd_elements(self):
        arr = [1]
        self.assertEqual(calculate_median(arr), 1)

    # Test case for an array with a larger odd number of elements
    def test_large_odd_elements(self):
        arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
        self.assertEqual(calculate_median(arr), 11)

    # Test case for an array with a single element
    def test_single_element(self):
        arr = [42]
        self.assertEqual(calculate_median(arr), 42)
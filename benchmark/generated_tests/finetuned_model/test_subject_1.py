import unittest

class TestMedianInIntervalFunction(unittest.TestCase):
    # Test case with an odd number of elements
    def test_odd_number_elements(self):
        # Test case with median equal to lower_limit
        self.assertTrue(median_in_interval([1, 3, 2], 1, 3))
        
        # Test case with median equal to upper_limit
        self.assertTrue(median_in_interval([1, 2, 3], 1, 3))
        
        # Test case with median less than lower_limit
        self.assertFalse(median_in_interval([1, 2, 3], 2, 3))
        
        # Test case with median greater than upper_limit
        self.assertFalse(median_in_interval([1, 2, 3], 1, 2))

    # Test case with an even number of elements
    def test_even_number_elements(self):
        # Test case with median equal to lower_limit
        self.assertTrue(median_in_interval([1, 2, 3, 4], 2, 3))
        
        # Test case with median equal to upper_limit
        self.assertTrue(median_in_interval([1, 2, 3, 4], 1, 3))
        
        # Test case with median less than lower_limit
        self.assertFalse(median_in_interval([1, 2, 3, 4], 2, 3))
        
        # Test case with median greater than upper_limit
        self.assertFalse(median_in_interval([1, 2, 3, 4], 1, 2))

    # Test case with duplicate elements
    def test_duplicate_elements(self):
        # Test case with median equal to lower_limit
        self.assertTrue(median_in_interval([1, 1, 1, 1], 1, 1))
        
        # Test case with median equal to upper_limit
        self.assertTrue(median_in_interval([1, 1, 1, 1], 1, 1))
        
        # Test case with median less than lower_limit
        self.assertFalse(median_in_interval([1, 1, 1, 1], 2, 2))
        
        # Test case with median greater than upper_limit
        self.assertFalse(median_in_interval([1, 1, 1, 1], 0, 0))

    # Test case with large numbers
    def test_large_numbers(self):
        # Test case with median equal to lower_limit
        self.assertTrue(median_in_interval([100, 200, 300, 400], 200, 300))
        
        # Test case with median equal to upper_limit
        self.assertTrue(median_in_interval([100, 200, 300, 400], 100, 200))
        
        # Test case with median less than lower_limit
        self.assertFalse(median_in_interval([100, 200, 300, 400], 300, 400))
        
        # Test case with median greater than upper_limit
        self.assertFalse(median_in_interval([100, 200, 300, 400], 50, 150))

    # Test case with single element
    def test_single_element(self):
        # Test case with median equal to lower_limit
        self.assertTrue(median_in_interval([1], 1, 1))
        
        # Test case with median equal to upper_limit
        self.assertTrue(median_in_interval([1], 1, 1))
        
        # Test case with median less than lower_limit
        self.assertFalse(median_in_interval([1], 2, 2))
        
        # Test case with median greater than upper_limit
        self.assertFalse(median_in_interval([1], 0, 0))
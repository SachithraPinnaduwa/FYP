import unittest

class TestMedianInInterval(unittest.TestCase):
    def test_even_length(self):
        self.assertTrue(median_in_interval([1, 2, 3, 4], 1, 4))
        self.assertTrue(median_in_interval([1, 2, 3, 4], 0, 5))
        self.assertFalse(median_in_interval([1, 2, 3, 4], 0, 0))
        self.assertFalse(median_in_interval([1, 2, 3, 4], 5, 5))
    
    def test_odd_length(self):
        self.assertTrue(median_in_interval([1, 2, 3], 1, 3))
        self.assertTrue(median_in_interval([1, 2, 3], 0, 4))
        self.assertFalse(median_in_interval([1, 2, 3], 0, 0))
        self.assertFalse(median_in_interval([1, 2, 3], 4, 4))
    
    def test_single_element(self):
        self.assertTrue(median_in_interval([1], 1, 1))
        self.assertTrue(median_in_interval([1], 0, 2))
        self.assertFalse(median_in_interval([1], 0, 0))
        self.assertFalse(median_in_interval([1], 2, 2))
    
    def test_negative_numbers(self):
        self.assertTrue(median_in_interval([-1, 0, 1], -1, 1))
        self.assertTrue(median_in_interval([-1, 0, 1], -2, 2))
        self.assertFalse(median_in_interval([-1, 0, 1], -2, -2))
        self.assertFalse(median_in_interval([-1, 0, 1], 2, 2))
    
    def test_duplicate_numbers(self):
        self.assertTrue(median_in_interval([1, 1, 1], 1, 1))
        self.assertTrue(median_in_interval([1, 1, 1], 0, 2))
        self.assertFalse(median_in_interval([1, 1, 1], 0, 0))
        self.assertFalse(median_in_interval([1, 1, 1], 2, 2))
    
    def test_unsorted_numbers(self):
        self.assertTrue(median_in_interval([4, 3, 2, 1], 1, 4))
        self.assertTrue(median_in_interval([4, 3, 2, 1], 0, 5))
        self.assertFalse(median_in_interval([4, 3, 2, 1], 0, 0))
        self.assertFalse(median_in_interval([4, 3, 2, 1], 5, 5))
    
    def test_empty_list(self):
        self.assertFalse(median_in_interval([], 0, 10))
    
    def test_large_numbers(self):
        self.assertTrue(median_in_interval([1000000, 2000000, 3000000], 1000000, 3000000))
        self.assertTrue(median_in_interval([1000000, 2000000, 3000000], 0, 4000000))
        self.assertFalse(median_in_interval([1000000, 2000000, 3000000], 0, 0))
        self.assertFalse(median_in_interval([1000000, 2000000, 3000000], 4000000, 4000000))
    
    def test_float_numbers(self):
        self.assertTrue(median_in_interval([1.5, 2.5, 3.5], 1.5, 3.5))
        self.assertTrue(median_in_interval([1.5, 2.5, 3.5], 0, 4))
        self.assertFalse(median_in_interval([1.5, 2.5, 3.5], 0, 0))
        self.assertFalse(median_in_interval([1.5, 2.5, 3.5], 4, 4))
    
    def test_mixed_types(self):
        self.assertTrue(median_in_interval([1, 2.5, 3], 1, 3))
        self.assertTrue(median_in_interval([1, 2.5, 3], 0, 4))
        self.assertFalse(median_in_interval([1, 2.5, 3], 0, 0))
        self.assertFalse(median_in_interval([1, 2.5, 3], 4, 4))
    
    def test_large_list(self):
        large_list = list(range(1000000))
        self.assertTrue(median_in_interval(large_list, 0, 1000000))
        self.assertTrue(median_in_interval(large_list, 0, 500000))
        self.assertFalse(median_in_interval(large_list, 0, 0))
        self.assertFalse(median_in_interval(large_list, 1000000, 1000000))
    
    def test_negative_and_positive(self):
        self.assertTrue(median_in_interval([-10, 0, 10], -10, 10))
        self.assertTrue(median_in_interval([-10, 0, 10], -20, 20))
        self.assertFalse(median_in_interval([-10, 0, 10], -20, -20))
        self.assertFalse(median_in_interval([-10, 0, 10], 20, 20))
    
    def test_all_same_numbers(self):
        self.assertTrue(median_in_interval([5, 5, 5], 5, 5))
        self.assertTrue(median_in_interval([5, 5, 5], 4, 6))
        self.assertFalse(median_in_interval([5, 5, 5], 4, 4))
        self.assertFalse(median_in_interval([5, 5, 5], 6, 6))
    
    def test_alternating_numbers(self):
        self.assertTrue(median_in_interval([1, 3, 5, 7, 9], 1, 9))
        self.assertTrue(median_in_interval([1, 3, 5, 7, 9], 0, 10))
        self.assertFalse(median_in_interval([1, 3, 5, 7, 9], 0, 0))
        self.assertFalse(median_in_interval([1, 3, 5,
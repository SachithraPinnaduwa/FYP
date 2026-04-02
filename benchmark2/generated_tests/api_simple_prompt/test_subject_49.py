from subject_49 import *

import unittest

def find_median(arr):
    arr_length = len(arr)
    sorted_arr = sorted(arr)
    
    if arr_length % 2 == 1:
        median_index = arr_length // 2
        median = sorted_arr[median_index]
    else:
        median_index_1 = arr_length // 2 - 1
        median_index_2 = arr_length // 2
        median = (sorted_arr[median_index_1] + sorted_arr[median_index_2]) / 2
    
    return round(median)

class TestFindMedian(unittest.TestCase):
    def test_find_median_odd_length(self):
        self.assertEqual(find_median([3, 1, 2, 4, 5]), 3)
    
    def test_find_median_even_length(self):
        self.assertEqual(find_median([-10, 4, 6, 1000, 10, 20]), 15)
    
    def test_find_median_single_element(self):
        self.assertEqual(find_median([7]), 7)
    
    def test_find_median_empty_array(self):
        with self.assertRaises(ValueError):
            find_median([])
    
    def test_find_median_negative_numbers(self):
        self.assertEqual(find_median([-5, -1, -6]), -5)
    
    def test_find_median_large_numbers(self):
        self.assertEqual(find_median([1000000, 2000000, 3000000, 4000000, 5000000]), 3000000)
    
    def test_find_median_duplicates(self):
        self.assertEqual(find_median([1, 1, 1, 1, 1]), 1)

if __name__ == '__main__':
    unittest.main()
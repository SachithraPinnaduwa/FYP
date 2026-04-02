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
    def test_odd_number_of_elements(self):
        self.assertEqual(find_median([1, 3, 5, 7, 9]), 5)

    def test_even_number_of_elements(self):
        self.assertEqual(find_median([1, 2, 3, 4, 5, 6]), 3.5)

    def test_negative_numbers(self):
        self.assertEqual(find_median([-5, -3, -1, 0, 2, 4]), 0.5)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            find_median([])

    def test_single_element(self):
        self.assertEqual(find_median([42]), 42)

    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            find_median(5)

    def test_non_numeric_elements(self):
        with self.assertRaises(TypeError):
            find_median([1, 'a', 3, 'b', 5])

if __name__ == '__main__':
    unittest.main()
from subject_13 import *

import unittest

def unique_sorted_array(arr):
    unique_elements = []
    for num in arr:
        if num not in unique_elements:
            unique_elements.append(num)

    n = len(unique_elements)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if unique_elements[j] > unique_elements[j+1]:
                unique_elements[j], unique_elements[j+1] = unique_elements[j+1], unique_elements[j]

    return unique_elements

class TestUniqueSortedArray(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(unique_sorted_array([1, 3, 2, 4, 1, 3, 5]), [1, 2, 3, 4, 5])

    def test_edge_case_empty_array(self):
        self.assertEqual(unique_sorted_array([]), [])

    def test_edge_case_all_same_elements(self):
        self.assertEqual(unique_sorted_array([5, 5, 5, 5]), [5])

    def test_edge_case_negative_numbers(self):
        self.assertEqual(unique_sorted_array([-3, -1, -2, -4, -1, -3, -5]), [-5, -4, -3, -2, -1])

    def test_error_handling_non_integer_values(self):
        with self.assertRaises(TypeError):
            unique_sorted_array([1, 2, 'a', 3, 4])

if __name__ == '__main__':
    unittest.main()
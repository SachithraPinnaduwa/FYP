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
    def test_unique_sorted_array(self):
        self.assertEqual(unique_sorted_array([10, 2, 10, 5, 3, 7, 1]), [1, 2, 3, 5, 7, 10])
        self.assertEqual(unique_sorted_array([-1, -3, -1, 2, 0, 0, 1]), [-3, -1, 0, 1, 2])
        self.assertEqual(unique_sorted_array([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(unique_sorted_array([1, 1, 1, 1, 1]), [1])
        self.assertEqual(unique_sorted_array([]), [])

if __name__ == '__main__':
    unittest.main()
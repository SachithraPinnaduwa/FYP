from subject_87 import *

import unittest

def solve(input_list):
    subarrays = [element for element in input_list if isinstance(element, list)]
    normal_elements = [element for element in input_list if not isinstance(element, list)]

    def bubble_sort(l):
        n = len(l)
        for i in range(n):
            for j in range(0, n - i - 1):
                if l[j] > l[j + 1] :
                    l[j], l[j + 1] = l[j + 1], l[j]
        return l

    def average(l):
        return sum(l) / len(l)

    sorted_subarrays = sorted([bubble_sort(subarray) for subarray in subarrays], key=average)
    sorted_elements = bubble_sort(normal_elements)
    return sorted_subarrays + sorted_elements

class TestSolveFunction(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(solve([[4, 2, 3], 1, [5, 6], 7, [8, 9, 10]]), [[1, 2, 3], [4, 5, 6], [7, 8, 9, 10]])

    def test_edge_case_empty_list(self):
        self.assertEqual(solve([]), [])

    def test_edge_case_only_integers(self):
        self.assertEqual(solve([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_edge_case_only_sub_arrays(self):
        self.assertEqual(solve([[1, 2], [3, 4], [5, 6]]), [[1, 2], [3, 4], [5, 6]])

    def test_error_handling_non_integer_and_non_list_elements(self):
        self.assertEqual(solve([1, 'a', [3, 4], 5]), [1, 5, [3, 4]])

if __name__ == '__main__':
    unittest.main()
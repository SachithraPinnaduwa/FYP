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

class TestSolve(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve([[1, 2, 3], [4, 5, 6], [10, 11, 12]]), [[1, 2, 3], [4, 5, 6], [10, 11, 12]])
        self.assertEqual(solve([[10, 20, 30], [40, 50, 60], [1, 2, 3]]), [[1, 2, 3], [10, 20, 30], [40, 50, 60]])
        self.assertEqual(solve([[3, 2, 1], [6, 5, 4], [9, 8, 7]]), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.assertEqual(solve([[1, 2, 3], [4, 5, 6], [10, 11, 12], 13, 14, 15]), [[1, 2, 3], [4, 5, 6], [10, 11, 12], 13, 14, 15])
        self.assertEqual(solve([[10, 20, 30], [40, 50, 60], [1, 2, 3], 13, 14, 15]), [[1, 2, 3], [10, 20, 30], [40, 50, 60], 13, 14, 15])

if __name__ == '__main__':
    unittest.main()
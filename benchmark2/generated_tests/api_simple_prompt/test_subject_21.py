from subject_21 import *

import unittest

def greedy_sum_subset(arr, target_sum):
    n = len(arr)

    # Sort the array in decreasing order
    arr.sort(reverse=True)

    # Initialize the list of subsets
    subsets = []

    for i in range(n):
        j = 0
        found = False
        
        # Check if the element can be added to the existing subsets
        while j < len(subsets):
            
            if sum(subsets[j]) + arr[i] <= target_sum:
                subsets[j].append(arr[i])
                found = True
                break
            
            j += 1

        if not found:
            # Create a new subset if no subset can contain the element
            subsets.append([arr[i]])

    return subsets

class TestGreedySumSubset(unittest.TestCase):
    def test_case_1(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        target_sum = 15
        expected_output = [[10, 5], [9, 6], [8, 7], [2, 3, 1]]
        self.assertEqual(greedy_sum_subset(arr, target_sum), expected_output)

    def test_case_2(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        target_sum = 10
        expected_output = [[10], [9], [8], [7], [6], [5], [4], [3], [2], [1]]
        self.assertEqual(greedy_sum_subset(arr, target_sum), expected_output)

    def test_case_3(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        target_sum = 20
        expected_output = [[10, 9, 1], [8, 7, 2], [6, 5, 3]]
        self.assertEqual(greedy_sum_subset(arr, target_sum), expected_output)

    def test_case_4(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        target_sum = 1
        expected_output = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
        self.assertEqual(greedy_sum_subset(arr, target_sum), expected_output)

    def test_case_5(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        target_sum = 100
        expected_output = [[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]]
        self.assertEqual(greedy_sum_subset(arr, target_sum), expected_output)

if __name__ == '__main__':
    unittest.main()
import unittest

class TestGreedySumSubset(unittest.TestCase):

    # Test case for an empty array
    def test_empty_array(self):
        arr = []
        target_sum = 10
        expected_output = []
        self.assertEqual(greedy_sum_subset(arr, target_sum), expected_output)

    # Test case for an array with a single element
    def test_single_element(self):
        arr = [5]
        target_sum = 10
        expected_output = [[5]]
        self.assertEqual(greedy_sum_subset(arr, target_sum), expected_output)

    # Test case for an array with multiple elements that fit in a single subset
    def test_multiple_elements_single_subset(self):
        arr = [5, 3, 2, 1]
        target_sum = 10
        expected_output = [[5, 3, 2], [1]]
        self.assertEqual(greedy_sum_subset(arr, target_sum), expected_output)

    # Test case for an array with multiple elements that require multiple subsets
    def test_multiple_elements_multiple_subsets(self):
        arr = [5, 3, 2, 1, 4]
        target_sum = 10
        expected_output = [[5, 3], [2, 1, 4]]
        self.assertEqual(greedy_sum_subset(arr, target_sum), expected_output)

    # Test case for an array with elements that are greater than the target sum
    def test_elements_greater_than_target_sum(self):
        arr = [11, 5, 3, 2, 1, 4]
        target_sum = 10
        expected_output = [[11], [5, 3], [2, 1, 4]]
        self.assertEqual(greedy_sum_subset(arr, target_sum), expected_output)

    # Test case for an array with duplicate elements
    def test_duplicate_elements(self):
        arr = [5, 5, 3, 2, 1, 4]
        target_sum = 10
        expected_output = [[5, 5], [3, 2, 1, 4]]
        self.assertEqual(greedy_sum_subset(arr, target_sum), expected_output)

    # Test case for an array with a large number of elements
    def test_large_number_of_elements(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        target_sum = 10
        expected_output = [[15], [14], [13], [12], [11], [10], [9], [8], [7], [6], [5], [4], [3, 2, 1]]
        self.assertEqual(greedy_sum_subset(arr, target_sum), expected_output)
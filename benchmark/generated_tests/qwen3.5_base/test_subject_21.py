import unittest

class TestGreedySumSubset(unittest.TestCase):
    def test_empty_array(self):
        arr = []
        target_sum = 10
        result = greedy_sum_subset(arr, target_sum)
        self.assertEqual(result, [])

    def test_single_element(self):
        arr = [5]
        target_sum = 10
        result = greedy_sum_subset(arr, target_sum)
        self.assertEqual(result, [[5]])

    def test_two_elements(self):
        arr = [5, 3]
        target_sum = 10
        result = greedy_sum_subset(arr, target_sum)
        self.assertEqual(result, [[5, 3]])

    def test_three_elements(self):
        arr = [5, 3, 2]
        target_sum = 10
        result = greedy_sum_subset(arr, target_sum)
        self.assertEqual(result, [[5, 3, 2]])

    def test_large_array(self):
        arr = [10, 20, 30, 40, 50]
        target_sum = 100
        result = greedy_sum_subset(arr, target_sum)
        self.assertEqual(result, [[50, 40, 10]])

    def test_negative_numbers(self):
        arr = [-5, -3, -2]
        target_sum = 10
        result = greedy_sum_subset(arr, target_sum)
        self.assertEqual(result, [[-5, -3, -2]])

    def test_zero_sum(self):
        arr = [0, 0, 0]
        target_sum = 0
        result = greedy_sum_subset(arr, target_sum)
        self.assertEqual(result, [[0, 0, 0]])

    def test_large_target_sum(self):
        arr = [1, 2, 3, 4, 5]
        target_sum = 100
        result = greedy_sum_subset(arr, target_sum)
        self.assertEqual(result, [[1, 2, 3, 4, 5]])

    def test_large_negative_target_sum(self):
        arr = [1, 2, 3, 4, 5]
        target_sum = -100
        result = greedy_sum_subset(arr, target_sum)
        self.assertEqual(result, [])

    def test_large_array_with_duplicates(self):
        arr = [1, 1, 1, 1, 1]
        target_sum = 5
        result = greedy_sum_subset(arr, target_sum)
        self.assertEqual(result, [[1, 1, 1, 1, 1]])

    def test_large_array_with_duplicates_and_target_sum(self):
        arr = [1, 1, 1, 1, 1]
        target_sum = 10
        result = greedy_sum_subset(arr, target_sum)
        self.assertEqual(result, [[1, 1, 1, 1, 1]])

    def test_large_array_with_duplicates_and_negative_target_sum(self):
        arr = [1, 1, 1, 1, 1]
        target_sum = -10
        result = greedy_sum_subset(arr, target_sum)
        self.assertEqual(result, [])

    def test_large_array_with_duplicates_and_zero_target_sum(self):
        arr = [1, 1, 1, 1, 1]
        target_sum = 0
        result = greedy_sum_subset(arr, target_sum)
        self.assertEqual(result, [])

    def test_large_array_with_duplicates_and_large_target_sum(self):
        arr = [1, 1, 1, 1, 1]
        target_sum = 100
        result = greedy_sum_subset(arr, target_sum)
        self.assertEqual(result, [[1, 1, 1, 1, 1]])

    def test_large_array_with_duplicates_and_large_negative_target_sum(self):
        arr = [1, 1, 1, 1, 1]
        target_sum = -100
        result = greedy_sum_subset(arr, target_sum)
        self.assertEqual(result, [])

    def test_large_array_with_duplicates_and_large_zero_target_sum(self):
        arr = [1, 1, 1, 1, 1]
        target_sum = 0
        result = greedy_sum_subset(arr, target_sum)
        self.assertEqual(result, [])

    def test_large_array_with_duplicates_and_large_large_target_sum(self):
        arr = [1, 1, 1, 1, 1]
        target_sum = 1000
        result = greedy_sum_subset(arr, target_sum)
        self.assertEqual(result, [[1, 1, 1, 1, 1]])

    def test_large_array_with_duplicates_and_large_large_negative_target_sum(self):
        arr = [1, 1, 1, 1, 1]
        target_sum = -1000
        result = greedy_sum_subset(arr, target_sum)
        self.assertEqual(result, [])

    def test_large_array_with_duplicates_and_large_large_zero_target_sum(self):
        arr = [1, 1, 1, 1, 1]
        target_sum = 0
        result = greedy_sum_subset(arr, target_sum)
        self.assertEqual(result, [])

    def test_large_array_with_duplicates_and_large_large_large_target_sum(self):
        arr = [1, 1, 1, 1, 1]
        target_sum = 10000
        result = greedy_sum_subset(arr, target_sum)
        self.assertEqual(result, [[1, 1, 1, 1, 1]])

    def test_large_array_with_duplicates_and_large_large_large_negative_target_sum(self):
        arr = [1, 1, 1, 1, 1]
        target_sum = -10000
        result = greedy_sum_subset(arr, target_sum)
        self.assertEqual(result, [])

    def test_large_array_with_duplicates_and_large_large_large_zero_target_sum(self):
        arr = [1, 1, 1, 1, 1]
        target_sum = 0
        result = greedy_sum_subset(arr, target_sum)
        self.assertEqual(result, [])

    def test_large_array_with_duplicates_and_large_large_large_large_target_sum(self):
        arr = [1, 1, 1, 1, 1]
        target_sum = 100000
        result = greedy_sum_subset(arr, target_sum)
        self.assertEqual(result, [[1, 1, 1, 1, 1]])

    def test_large_array_with_duplicates_and_large_large_large_large_negative_target_sum(self):
        arr = [1, 1, 1, 1, 1]
        target_sum = -100000
        result = greedy_sum_subset(arr, target_sum)
        self.assertEqual(result, [])

    def test_large_array_with_duplicates_and_large_large
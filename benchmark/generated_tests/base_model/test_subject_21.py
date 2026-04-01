import unittest

class TestGreedySumSubset(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(greedy_sum_subset([], 10), [])

    def test_single_element(self):
        self.assertEqual(greedy_sum_subset([5], 10), [[5]])

    def test_target_sum_exceeded(self):
        self.assertEqual(greedy_sum_subset([1, 2, 3, 4, 5], 2), [[5], [4], [3], [2], [1]])

    def test_multiple_subsets(self):
        self.assertEqual(greedy_sum_subset([1, 2, 3, 4, 5], 6), [[5, 1], [4, 2], [3]])

    def test_negative_elements(self):
        self.assertEqual(greedy_sum_subset([-1, -2, -3, -4, -5], 0), [[-1], [-2], [-3], [-4], [-5]])

    def test_duplicate_elements(self):
        self.assertEqual(greedy_sum_subset([3, 3, 3, 3, 3], 9), [[3, 3], [3, 3]])

    def test_large_numbers(self):
        self.assertEqual(greedy_sum_subset([100, 200, 300, 400, 500], 1000), [[500, 400], [300, 200], [100]])

if __name__ == '__main__':
    unittest.main()
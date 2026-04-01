import unittest

class TestCountSubarraysWithSum(unittest.TestCase):

    def test_empty_array(self):
        # Test with an empty array
        A = []
        S = 0
        self.assertEqual(count_subarrays_with_sum(A, S), 0)

    def test_zero_sum(self):
        # Test with a sum of zero
        A = [0, 1, 0, 1, 0]
        S = 0
        self.assertEqual(count_subarrays_with_sum(A, S), 6)

    def test_no_subarrays(self):
        # Test with no subarrays that sum to S
        A = [0, 1, 1, 1, 0]
        S = 2
        self.assertEqual(count_subarrays_with_sum(A, S), 0)

    def test_single_subarray(self):
        # Test with a single subarray that sums to S
        A = [1, 0, 1, 0, 1]
        S = 2
        self.assertEqual(count_subarrays_with_sum(A, S), 4)

    def test_multiple_subarrays(self):
        # Test with multiple subarrays that sum to S
        A = [1, 1, 1, 1, 1]
        S = 3
        self.assertEqual(count_subarrays_with_sum(A, S), 3)

    def test_large_array(self):
        # Test with a large array
        A = [1] * 10000
        S = 10000
        self.assertEqual(count_subarrays_with_sum(A, S), 50005000)

    def test_array_with_zeros(self):
        # Test with an array containing zeros
        A = [0, 0, 1, 0, 0, 1, 0, 0, 1]
        S = 3
        self.assertEqual(count_subarrays_with_sum(A, S), 4)
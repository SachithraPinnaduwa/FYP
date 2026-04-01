import unittest

class TestCountSubarraysWithSum(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(count_subarrays_with_sum([], 0), 0)

    def test_zero_s(self):
        self.assertEqual(count_subarrays_with_sum([0, 0, 0, 0], 0), 6)

    def test_all_ones(self):
        self.assertEqual(count_subarrays_with_sum([1, 1, 1, 1], 2), 6)

    def test_no_subarray(self):
        self.assertEqual(count_subarrays_with_sum([0, 0, 0, 0], 2), 0)

    def test_single_element_target(self):
        self.assertEqual(count_subarrays_with_sum([1], 1), 1)

    def test_single_element_not_target(self):
        self.assertEqual(count_subarrays_with_sum([1], 0), 0)

    def test_multiple_subarrays(self):
        self.assertEqual(count_subarrays_with_sum([1, 0, 1, 0, 1], 2), 4)

    def test_large_array(self):
        A = [random.randint(0, 1) for _ in range(30000)]
        S = random.randint(0, 30000)
        result = count_subarrays_with_sum(A, S)
        # Add additional checks or assertions here as needed

if __name__ == '__main__':
    unittest.main()
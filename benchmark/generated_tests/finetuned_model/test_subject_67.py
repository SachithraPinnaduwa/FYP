import unittest

class TestComputeSumFunction(unittest.TestCase):

    def test_sum_divisible_by_K(self):
        # Test case where the sum of the list is divisible by K
        x = [10, 20, 30]
        K = 60
        self.assertEqual(compute_sum(x, K), '60.00')

    def test_sum_not_divisible_by_K(self):
        # Test case where the sum of the list is not divisible by K
        x = [10, 20, 30]
        K = 59
        self.assertEqual(compute_sum(x, K), 60)

    def test_sum_equals_K(self):
        # Test case where the sum of the list is equal to K
        x = [50, 10]
        K = 60
        self.assertEqual(compute_sum(x, K), '60.00')

    def test_empty_list(self):
        # Test case with an empty list
        x = []
        K = 10
        self.assertEqual(compute_sum(x, K), 0)

    def test_single_element_list(self):
        # Test case with a single element list
        x = [10]
        K = 10
        self.assertEqual(compute_sum(x, K), 10)

    def test_large_numbers(self):
        # Test case with large numbers
        x = [1000, 2000, 3000]
        K = 6000
        self.assertEqual(compute_sum(x, K), '6000.00')

    def test_zero_sum(self):
        # Test case with a sum of zero
        x = [0, 0, 0]
        K = 1
        self.assertEqual(compute_sum(x, K), 0)
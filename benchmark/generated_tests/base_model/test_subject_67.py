import unittest
from compute_sum import compute_sum

class TestComputeSum(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(compute_sum([], 5), 0)

    def test_single_element_divisible_by_K(self):
        self.assertEqual(compute_sum([10], 10), "10.00")

    def test_single_element_not_divisible_by_K(self):
        self.assertEqual(compute_sum([7], 3), 8)

    def test_multiple_elements_divisible_by_K(self):
        self.assertEqual(compute_sum([10, 20, 30], 60), "60.00")

    def test_multiple_elements_not_divisible_by_K(self):
        self.assertEqual(compute_sum([10, 20, 30], 59), 61)

    def test_negative_numbers(self):
        self.assertEqual(compute_sum([-10, -20, -30], 10), "-60.00")

    def test_large_numbers(self):
        self.assertEqual(compute_sum([1000, 2000, 3000], 6000), "6000.00")

    def test_K_is_1(self):
        self.assertEqual(compute_sum([1, 2, 3], 1), "6.00")

    def test_K_is_equal_to_total(self):
        self.assertEqual(compute_sum([10, 20, 30], 60), "60.00")

if __name__ == '__main__':
    unittest.main()
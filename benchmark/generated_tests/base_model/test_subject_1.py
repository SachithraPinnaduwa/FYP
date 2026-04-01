import unittest

class TestMedianInInterval(unittest.TestCase):

    def test_odd_number_of_elements(self):
        self.assertTrue(median_in_interval([3, 1, 4, 1, 5], 2, 6))
        self.assertFalse(median_in_interval([3, 1, 4, 1, 5], 7, 9))

    def test_even_number_of_elements(self):
        self.assertTrue(median_in_interval([3, 1, 4, 1, 5, 9], 2, 6))
        self.assertFalse(median_in_interval([3, 1, 4, 1, 5, 9], 8, 10))

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            median_in_interval([], 1, 10)

    def test_single_element(self):
        self.assertTrue(median_in_interval([5], 5, 5))
        self.assertFalse(median_in_interval([5], 4, 6))

    def test_all_outside_interval(self):
        self.assertFalse(median_in_interval([1, 2, 3], 4, 5))
        self.assertFalse(median_in_interval([6, 7, 8], 2, 3))

    def test_median_on_boundary(self):
        self.assertTrue(median_in_interval([1, 2, 3, 4, 5], 2, 2))
        self.assertTrue(median_in_interval([1, 2, 3, 4, 5], 5, 5))

if __name__ == '__main__':
    unittest.main()
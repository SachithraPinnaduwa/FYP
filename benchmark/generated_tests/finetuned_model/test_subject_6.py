import unittest

class TestMedianFunction(unittest.TestCase):
    def test_odd_length_list(self):
        # Test with an odd-length list
        data = [3, 1, 4, 1, 5, 9, 2]
        self.assertEqual(find_median(data), 3)

    def test_even_length_list(self):
        # Test with an even-length list
        data = [3, 1, 4, 1, 5, 9]
        self.assertEqual(find_median(data), 2)

    def test_single_element_list(self):
        # Test with a single element list
        data = [5]
        self.assertEqual(find_median(data), 5)

    def test_sorted_list(self):
        # Test with a list that is already sorted
        data = [1, 2, 3, 4, 5]
        self.assertEqual(find_median(data), 3)

    def test_repeated_elements(self):
        # Test with a list containing repeated elements
        data = [3, 3, 2, 2, 1, 1]
        self.assertEqual(find_median(data), 2)

    def test_large_list(self):
        # Test with a large list
        data = [i for i in range(1000)]
        self.assertEqual(find_median(data), 499.5)

    def test_empty_list(self):
        # Test with an empty list
        with self.assertRaises(ValueError):
            find_median([])
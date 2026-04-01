import unittest

class TestUniqueSortedArray(unittest.TestCase):

    def test_empty_array(self):
        # Test with an empty array
        self.assertEqual(unique_sorted_array([]), [])

    def test_single_element_array(self):
        # Test with an array that contains a single element
        self.assertEqual(unique_sorted_array([5]), [5])

    def test_array_with_duplicates(self):
        # Test with an array that contains duplicates
        self.assertEqual(unique_sorted_array([3, 1, 2, 1, 3, 4, 2]), [1, 2, 3, 4])

    def test_array_with_negative_numbers(self):
        # Test with an array that contains negative numbers
        self.assertEqual(unique_sorted_array([-5, 2, 3, -5, 2, 0]), [-5, 0, 2, 3])

    def test_array_with_zero(self):
        # Test with an array that contains zero
        self.assertEqual(unique_sorted_array([0, 0, 0, 0]), [0])

    def test_array_with_reversed_order(self):
        # Test with an array that contains elements in descending order
        self.assertEqual(unique_sorted_array([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_array_with_mixed_elements(self):
        # Test with an array that contains a mix of positive, negative, and zero elements
        self.assertEqual(unique_sorted_array([-5, 0, 2, 3, -5, 2, 0]), [-5, 0, 2, 3])
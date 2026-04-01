import unittest

class TestBinarySearch(unittest.TestCase):

    # Test case for a target element in the middle of the array
    def test_target_in_middle(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        x = 5
        self.assertEqual(binary_search(arr, x), 4)

    # Test case for a target element at the beginning of the array
    def test_target_at_beginning(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        x = 1
        self.assertEqual(binary_search(arr, x), 0)

    # Test case for a target element at the end of the array
    def test_target_at_end(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        x = 10
        self.assertEqual(binary_search(arr, x), 9)

    # Test case for a target element not in the array
    def test_target_not_in_array(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        x = 11
        self.assertEqual(binary_search(arr, x), -1)

    # Test case for a single-element array
    def test_single_element_array(self):
        arr = [1]
        x = 1
        self.assertEqual(binary_search(arr, x), 0)

    # Test case for an empty array
    def test_empty_array(self):
        arr = []
        x = 1
        self.assertEqual(binary_search(arr, x), -1)

    # Test case for a target element in the array with duplicates
    def test_target_with_duplicates(self):
        arr = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        x = 2
        self.assertIn(binary_search(arr, x), [1, 2])

    # Test case for a target element at the beginning of the array with duplicates
    def test_target_at_beginning_with_duplicates(self):
        arr = [1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        x = 1
        self.assertIn(binary_search(arr, x), [0, 1, 2])
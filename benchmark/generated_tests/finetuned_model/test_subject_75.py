import unittest

class TestReverseArrayFunction(unittest.TestCase):

    # Test case to check if the function correctly reverses an array with odd number of elements
    def test_odd_number_of_elements(self):
        arr = [1, 2, 3, 4, 5]
        reverseArray(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [5, 4, 3, 2, 1])

    # Test case to check if the function correctly reverses an array with even number of elements
    def test_even_number_of_elements(self):
        arr = [1, 2, 3, 4]
        reverseArray(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [4, 3, 2, 1])

    # Test case to check if the function correctly handles an array with a single element
    def test_single_element_array(self):
        arr = [1]
        reverseArray(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [1])

    # Test case to check if the function correctly handles an empty array
    def test_empty_array(self):
        arr = []
        reverseArray(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [])

    # Test case to check if the function correctly handles an array with multiple duplicate elements
    def test_duplicate_elements(self):
        arr = [1, 2, 2, 1]
        reverseArray(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [1, 2, 2, 1])

    # Test case to check if the function correctly handles an array with a large number of elements
    def test_large_array(self):
        arr = list(range(1000))
        reverseArray(arr, 0, len(arr) - 1)
        self.assertEqual(arr, list(range(999, -1, -1)))

    # Test case to check if the function correctly handles an array with a mix of positive and negative integers
    def test_mixed_integers(self):
        arr = [1, -2, 3, -4, 5]
        reverseArray(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [5, -4, 3, -2, 1])
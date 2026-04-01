import unittest

class TestBinarySearchFunction(unittest.TestCase):

    def test_target_in_middle(self):
        # Test case where the target is in the middle of the array
        arr = [1, 2, 3, 4, 5]
        target = 3
        expected_result = 2
        self.assertEqual(binary_search(arr, target), expected_result)

    def test_target_at_beginning(self):
        # Test case where the target is at the beginning of the array
        arr = [1, 2, 3, 4, 5]
        target = 1
        expected_result = 0
        self.assertEqual(binary_search(arr, target), expected_result)

    def test_target_at_end(self):
        # Test case where the target is at the end of the array
        arr = [1, 2, 3, 4, 5]
        target = 5
        expected_result = 4
        self.assertEqual(binary_search(arr, target), expected_result)

    def test_target_not_in_array(self):
        # Test case where the target is not in the array
        arr = [1, 2, 3, 4, 5]
        target = 6
        expected_result = -1
        self.assertEqual(binary_search(arr, target), expected_result)

    def test_empty_array(self):
        # Test case with an empty array
        arr = []
        target = 1
        expected_result = -1
        self.assertEqual(binary_search(arr, target), expected_result)

    def test_array_with_single_element(self):
        # Test case with an array containing a single element
        arr = [1]
        target = 1
        expected_result = 0
        self.assertEqual(binary_search(arr, target), expected_result)

    def test_array_with_repeated_elements(self):
        # Test case with an array containing repeated elements
        arr = [1, 1, 1, 1, 1]
        target = 1
        expected_result = 0  # The function should return the index of the first occurrence
        self.assertEqual(binary_search(arr, target), expected_result)
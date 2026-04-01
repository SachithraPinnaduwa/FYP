import unittest

class TestBinarySearch(unittest.TestCase):
    # Test case for a target value that is present in the array
    def test_target_present(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        target = 5
        self.assertEqual(binary_search(arr, target), 4)

    # Test case for a target value that is not present in the array
    def test_target_not_present(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        target = 11
        self.assertEqual(binary_search(arr, target), -1)

    # Test case for an empty array
    def test_empty_array(self):
        arr = []
        target = 5
        self.assertEqual(binary_search(arr, target), -1)

    # Test case for an array with duplicate elements
    def test_duplicate_elements(self):
        arr = [1, 2, 2, 3, 4, 4, 5]
        target = 4
        self.assertIn(binary_search(arr, target), [4, 5])

    # Test case for an array with a single element that matches the target
    def test_single_element_match(self):
        arr = [1]
        target = 1
        self.assertEqual(binary_search(arr, target), 0)

    # Test case for an array with a single element that does not match the target
    def test_single_element_no_match(self):
        arr = [1]
        target = 2
        self.assertEqual(binary_search(arr, target), -1)

    # Test case for an array with the target at the beginning
    def test_target_at_beginning(self):
        arr = [1, 2, 3, 4, 5]
        target = 1
        self.assertEqual(binary_search(arr, target), 0)

    # Test case for an array with the target at the end
    def test_target_at_end(self):
        arr = [1, 2, 3, 4, 5]
        target = 5
        self.assertEqual(binary_search(arr, target), 4)
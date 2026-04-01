import unittest

class TestCountAndIndices(unittest.TestCase):

    def test_target_not_found(self):
        # Test case where the target is not in the array
        arr = [1, 2, 3, 4, 5]
        target = 6
        self.assertEqual(count_and_indices(arr, target), (0, []))

    def test_target_found_once(self):
        # Test case where the target is found only once in the array
        arr = [1, 2, 3, 4, 5]
        target = 3
        self.assertEqual(count_and_indices(arr, target), (1, [2]))

    def test_target_found_multiple_times(self):
        # Test case where the target is found multiple times in the array
        arr = [1, 2, 2, 2, 3, 4, 5]
        target = 2
        self.assertEqual(count_and_indices(arr, target), (3, [1, 2, 3]))

    def test_target_is_first_element(self):
        # Test case where the target is the first element in the array
        arr = [1, 1, 1, 2, 3, 4, 5]
        target = 1
        self.assertEqual(count_and_indices(arr, target), (3, [0, 1, 2]))

    def test_target_is_last_element(self):
        # Test case where the target is the last element in the array
        arr = [1, 2, 3, 4, 5, 5, 5]
        target = 5
        self.assertEqual(count_and_indices(arr, target), (3, [4, 5, 6]))

    def test_empty_array(self):
        # Test case with an empty array
        arr = []
        target = 1
        self.assertEqual(count_and_indices(arr, target), (0, []))

    def test_single_element_array(self):
        # Test case with an array containing only one element
        arr = [1]
        target = 1
        self.assertEqual(count_and_indices(arr, target), (1, [0]))
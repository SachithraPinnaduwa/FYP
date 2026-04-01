import unittest

class TestFindCommonElements(unittest.TestCase):
    # Test case with no common elements
    def test_no_common_elements(self):
        array1 = [1, 2, 3]
        array2 = [4, 5, 6]
        self.assertEqual(findCommonElements(array1, array2), [])

    # Test case with common elements
    def test_common_elements(self):
        array1 = [1, 2, 3]
        array2 = [3, 4, 5]
        self.assertEqual(findCommonElements(array1, array2), [3])

    # Test case with duplicate common elements in array1
    def test_duplicate_common_elements_in_array1(self):
        array1 = [1, 2, 2, 3]
        array2 = [3, 4, 5]
        self.assertEqual(findCommonElements(array1, array2), [3])

    # Test case with duplicate common elements in array2
    def test_duplicate_common_elements_in_array2(self):
        array1 = [1, 2, 3]
        array2 = [3, 3, 4, 5]
        self.assertEqual(findCommonElements(array1, array2), [3])

    # Test case with all elements in array1 being common
    def test_all_elements_common(self):
        array1 = [1, 2, 3]
        array2 = [1, 2, 3, 4, 5]
        self.assertEqual(findCommonElements(array1, array2), [1, 2, 3])

    # Test case with all elements in array2 being common
    def test_all_elements_common_reverse(self):
        array1 = [1, 2, 3, 4, 5]
        array2 = [3, 2, 1]
        self.assertEqual(findCommonElements(array1, array2), [1, 2, 3])

    # Test case with empty arrays
    def test_empty_arrays(self):
        array1 = []
        array2 = []
        self.assertEqual(findCommonElements(array1, array2), [])

    # Test case with one empty array
    def test_one_empty_array(self):
        array1 = [1, 2, 3]
        array2 = []
        self.assertEqual(findCommonElements(array1, array2), [])
from subject_36 import *

import unittest

class TestFindCommonElements(unittest.TestCase):
    def test_normal_case_multiple_common_elements(self):
        array1 = [1, 2, 3, 4, 5]
        array2 = [4, 5, 6, 7, 8]
        expected = [4, 5]
        self.assertEqual(findCommonElements(array1, array2), expected)

    def test_normal_case_no_common_elements(self):
        array1 = [1, 2, 3]
        array2 = [4, 5, 6]
        expected = []
        self.assertEqual(findCommonElements(array1, array2), expected)

    def test_normal_case_one_common_element(self):
        array1 = [1, 2, 3]
        array2 = [3, 4, 5]
        expected = [3]
        self.assertEqual(findCommonElements(array1, array2), expected)

    def test_normal_case_empty_arrays(self):
        array1 = []
        array2 = []
        expected = []
        self.assertEqual(findCommonElements(array1, array2), expected)

    def test_edge_case_one_empty_array(self):
        array1 = []
        array2 = [1, 2, 3]
        expected = []
        self.assertEqual(findCommonElements(array1, array2), expected)

    def test_error_handling_non_array_inputs(self):
        array1 = 'string'
        array2 = [1, 2, 3]
        with self.assertRaises(TypeError):
            findCommonElements(array1, array2)

    def test_error_handling_non_iterable_object(self):
        array1 = 123
        array2 = [1, 2, 3]
        with self.assertRaises(TypeError):
            findCommonElements(array1, array2)

if __name__ == '__main__':
    unittest.main()
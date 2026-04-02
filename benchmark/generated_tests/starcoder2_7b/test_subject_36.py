import unittest

class TestFindCommonElements(unittest.TestCase):
    def test_find_common_elements(self):
        array1 = [1, 2, 3, 4, 5, 6]
        array2 = [3, 4, 5, 6, 7, 8]
        expected_common_elements = [3, 4, 5, 6]
        actual_common_elements = findCommonElements(array1, array2)
        self.assertEqual(actual_common_elements, expected_common_elements)

if __name__ == '__main__':
    unittest.main()
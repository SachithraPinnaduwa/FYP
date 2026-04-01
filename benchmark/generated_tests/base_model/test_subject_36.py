import unittest

class TestFindCommonElements(unittest.TestCase):

    def test_empty_arrays(self):
        self.assertEqual(findCommonElements([], []), [])

    def test_one_empty_array(self):
        self.assertEqual(findCommonElements([1, 2, 3], []), [])
        self.assertEqual(findCommonElements([], [4, 5, 6]), [])

    def test_no_common_elements(self):
        self.assertEqual(findCommonElements([1, 2, 3], [4, 5, 6]), [])
        self.assertEqual(findCommonElements(['a', 'b'], ['c', 'd']), [])

    def test_with_duplicates(self):
        self.assertEqual(findCommonElements([1, 2, 2, 3], [2, 2, 4, 5]), [2])
        self.assertEqual(findCommonElements(['apple', 'banana', 'apple'], ['banana', 'cherry']), ['banana'])

    def test_single_common_element(self):
        self.assertEqual(findCommonElements([7], [7]), [7])

    def test_large_arrays(self):
        large_array = list(range(1000))
        common_elements = findCommonElements(large_array, large_array[::2])
        self.assertEqual(common_elements, list(range(0, 1000, 2)))

if __name__ == '__main__':
    unittest.main()
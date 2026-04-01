import unittest

class TestMergeSort(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(merge_sort([]), ([], 0))

    def test_single_element_array(self):
        self.assertEqual(merge_sort([5]), ([5], 0))

    def test_sorted_array(self):
        self.assertEqual(merge_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]), ([9, 6, 5, 5, 5, 4, 3, 3, 2, 1, 1], 14))

    def test_reverse_sorted_array(self):
        self.assertEqual(merge_sort([1, 2, 3, 4, 5, 6, 7, 8, 9]), ([9, 8, 7, 6, 5, 4, 3, 2, 1], 36))

    def test_random_array(self):
        self.assertEqual(merge_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]), ([9, 6, 5, 5, 5, 4, 3, 3, 2, 1, 1], 14))

    def test_duplicate_elements(self):
        self.assertEqual(merge_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]), ([9, 6, 5, 5, 5, 4, 3, 3, 2, 1, 1], 14))

    def test_negative_numbers(self):
        self.assertEqual(merge_sort([-3, -1, -4, -1, -5, -9, -2, -6, -5, -3, -5]), ([-1, -1, -2, -3, -3, -4, -5, -5, -5, -6, -9], 14))

if __name__ == '__main__':
    unittest.main()
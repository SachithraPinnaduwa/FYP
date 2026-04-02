import unittest

class TestMergeSort(unittest.TestCase):
    def test_merge_sort_with_duplicates(self):
        arr = [10, 20, 15, 25, 5, 15, 30, 20]
        sorted_arr, swaps = merge_sort(arr)
        self.assertEqual(sorted_arr, [30, 25, 20, 20, 15, 15, 10, 5])
        self.assertEqual(swaps, 8)

    def test_merge_sort_with_single_element(self):
        arr = [10]
        sorted_arr, swaps = merge_sort(arr)
        self.assertEqual(sorted_arr, [10])
        self.assertEqual(swaps, 0)

    def test_merge_sort_with_empty_array(self):
        arr = []
        sorted_arr, swaps = merge_sort(arr)
        self.assertEqual(sorted_arr, [])
        self.assertEqual(swaps, 0)

    def test_merge_sort_with_reversed_array(self):
        arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        sorted_arr, swaps = merge_sort(arr)
        self.assertEqual(sorted_arr, [10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
        self.assertEqual(swaps, 0)

    def test_merge_sort_with_random_array(self):
        arr = [10, 5, 15, 20, 25, 30]
        sorted_arr, swaps = merge_sort(arr)
        self.assertEqual(sorted_arr, [30, 25, 20, 15, 10, 5])
        self.assertEqual(swaps, 5)

    def test_merge_sort_with_negative_numbers(self):
        arr = [-10, -5, -15, -20, -25, -30]
        sorted_arr, swaps = merge_sort(arr)
        self.assertEqual(sorted_arr, [-10, -5, -15, -20, -25, -30])
        self.assertEqual(swaps, 0)

    def test_merge_sort_with_identical_elements(self):
        arr = [5, 5, 5, 5, 5]
        sorted_arr, swaps = merge_sort(arr)
        self.assertEqual(sorted_arr, [5, 5, 5, 5, 5])
        self.assertEqual(swaps, 0)

if __name__ == '__main__':
    unittest.main()
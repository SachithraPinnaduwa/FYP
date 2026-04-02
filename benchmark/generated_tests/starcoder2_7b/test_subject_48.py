import unittest

class TestMergeSort(unittest.TestCase):
    def test_merge_sort(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        sorted_arr, swaps = merge_sort(arr)
        self.assertEqual(sorted_arr, [10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
        self.assertEqual(swaps, 0)

        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
        sorted_arr, swaps = merge_sort(arr)
        self.assertEqual(sorted_arr, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
        self.assertEqual(swaps, 0)

        arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        sorted_arr, swaps = merge_sort(arr)
        self.assertEqual(sorted_arr, [10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
        self.assertEqual(swaps, 0)

        arr = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        sorted_arr, swaps = merge_sort(arr
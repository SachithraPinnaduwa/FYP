import unittest

class TestMergeSort(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(merge_sort([]), ([], 0))
    
    def test_single_element(self):
        self.assertEqual(merge_sort([5]), ([5], 0))
    
    def test_two_elements(self):
        self.assertEqual(merge_sort([2, 1]), ([1, 2], 1))
    
    def test_sorted_list(self):
        self.assertEqual(merge_sort([1, 2, 3, 4, 5]), ([1, 2, 3, 4, 5], 0))
    
    def test_reverse_sorted_list(self):
        self.assertEqual(merge_sort([5, 4, 3, 2, 1]), ([1, 2, 3, 4, 5], 10))
    
    def test_list_with_duplicates(self):
        self.assertEqual(merge_sort([2, 2, 2]), ([2, 2, 2], 0))
    
    def test_large_list(self):
        large_list = list(range(10000, 0, -1))
        sorted_list, swaps = merge_sort(large_list)
        self.assertEqual(sorted_list, list(range(1, 10001)))
        self.assertGreater(swaps, 0)
    
    def test_mixed_list(self):
        mixed_list = [3, 1, 4, 1, 5, 9, 2, 6]
        sorted_list, swaps = merge_sort(mixed_list)
        self.assertEqual(sorted_list, [1, 1, 2, 3, 4, 5, 6, 9])
        self.assertGreater(swaps, 0)
    
    def test_negative_numbers(self):
        negative_list = [-5, -2, 0, 3, -1]
        sorted_list, swaps = merge_sort(negative_list)
        self.assertEqual(sorted_list, [-5, -2, -1, 0, 3])
        self.assertGreater(swaps, 0)
    
    def test_large_negative_numbers(self):
        large_negative_list = list(range(-10000, 0))
        sorted_list, swaps = merge_sort(large_negative_list)
        self.assertEqual(sorted_list, list(range(-10000, 0)))
        self.assertGreater(swaps, 0)
    
    def test_large_positive_numbers(self):
        large_positive_list = list(range(1, 10001))
        sorted_list, swaps = merge_sort(large_positive_list)
        self.assertEqual(sorted_list, list(range(1, 10001)))
        self.assertGreater(swaps, 0)
    
    def test_large_mixed_numbers(self):
        large_mixed_list = list(range(1, 10001))
        large_mixed_list.reverse()
        sorted_list, swaps = merge_sort(large_mixed_list)
        self.assertEqual(sorted_list, list(range(1, 10001)))
        self.assertGreater(swaps, 0)
    
    def test_large_list_with_duplicates(self):
        large_list_with_duplicates = [2] * 10000
        sorted_list, swaps = merge_sort(large_list_with_duplicates)
        self.assertEqual(sorted_list, large_list_with_duplicates)
        self.assertEqual(swaps, 0)
    
    def test_large_list_with_duplicates_and_mixed(self):
        large_list_with_duplicates = [2] * 5000 + [1] * 5000
        large_list_with_duplicates.reverse()
        sorted_list, swaps = merge_sort(large_list_with_duplicates)
        self.assertEqual(sorted_list, [1] * 5000 + [2] * 5000)
        self.assertGreater(swaps, 0)
    
    def test_large_list_with_duplicates_and_mixed_reverse(self):
        large_list_with_duplicates = [1] * 5000 + [2] * 5000
        large_list_with_duplicates.reverse()
        sorted_list, swaps = merge_sort(large_list_with_duplicates)
        self.assertEqual(sorted_list, [2] * 5000 + [1] * 5000)
        self.assertGreater(swaps, 0)
    
    def test_large_list_with_duplicates_and_mixed_reverse_and_duplicates(self):
        large_list_with_duplicates = [1] * 5000 + [2] * 5000 + [3] * 5000
        large_list_with_duplicates.reverse()
        sorted_list, swaps = merge_sort(large_list_with_duplicates)
        self.assertEqual(sorted_list, [3] * 5000 + [2] * 5000 + [1] * 5000)
        self.assertGreater(swaps, 0)
    
    def test_large_list_with_duplicates_and_mixed_reverse_and_duplicates_and_mixed(self):
        large_list_with_duplicates = [1] * 5000 + [2] * 5000 + [3] * 5000 + [4] * 5000
        large_list_with_duplicates.reverse()
        sorted_list, swaps = merge_sort(large_list_with_duplicates)
        self.assertEqual(sorted_list, [4] * 5000 + [3] * 5000 + [2] * 5000 + [1] * 5000)
        self.assertGreater(swaps, 0)
    
    def test_large_list_with_duplicates_and_mixed_reverse_and_duplicates_and_mixed_and_mixed(self):
        large_list_with_duplicates = [1] * 5000 + [2] * 5000 + [3] * 5000 + [4] * 5000 + [5] * 5000
        large_list_with_duplicates.reverse()
        sorted_list, swaps = merge_sort(large_list_with_duplicates)
        self.assertEqual(sorted_list, [5] * 5000 + [4] * 5000 + [3] * 5000 + [2] * 5000 + [1] * 5000)
        self.assertGreater(swaps, 0)
    
    def test_large_list_with_duplicates_and_mixed_reverse_and_duplicates_and_mixed_and_mixed_and_mixed(self):
        large_list_with_duplicates = [1] * 5000 + [2] * 5000 + [3] * 5000 + [4] * 5000 + [5] * 5000 + [6] * 5000
        large_list_with_duplicates.reverse()
        sorted_list, swaps = merge_sort(large_list_with_duplicates)
        self.assertEqual(sorted_list, [6] * 5000 + [5] *
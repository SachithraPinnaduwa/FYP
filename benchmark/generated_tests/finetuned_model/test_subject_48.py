import unittest

class TestMergeSort(unittest.TestCase):

    def test_empty_array(self):
        # Test with an empty array
        arr, swaps = merge_sort([])
        self.assertEqual(arr, [])
        self.assertEqual(swaps, 0)

    def test_single_element_array(self):
        # Test with an array containing a single element
        arr, swaps = merge_sort([5])
        self.assertEqual(arr, [5])
        self.assertEqual(swaps, 0)

    def test_sorted_array(self):
        # Test with an already sorted array
        arr, swaps = merge_sort([1, 2, 3, 4, 5])
        self.assertEqual(arr, [5, 4, 3, 2, 1])
        self.assertEqual(swaps, 10)

    def test_reverse_sorted_array(self):
        # Test with a reverse sorted array
        arr, swaps = merge_sort([5, 4, 3, 2, 1])
        self.assertEqual(arr, [5, 4, 3, 2, 1])
        self.assertEqual(swaps, 0)

    def test_array_with_duplicates(self):
        # Test with an array containing duplicates
        arr, swaps = merge_sort([3, 1, 2, 2, 1])
        self.assertEqual(arr, [3, 2, 2, 1, 1])
        self.assertEqual(swaps, 5)

    def test_large_array(self):
        # Test with a large array
        arr = [i for i in range(1000)]
        arr.reverse()
        arr, swaps = merge_sort(arr)
        self.assertEqual(arr, [i for i in range(1000)])
        self.assertEqual(swaps, 250000)

if __name__ == '__main__':
    pass
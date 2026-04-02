import unittest

class TestBinarySearch(unittest.TestCase):
    def test_binary_search_basic(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(binary_search(arr, 3, False), 2)
        self.assertEqual(binary_search(arr, 3, True), 2)
        self.assertEqual(binary_search(arr, 0, False), -1)
        self.assertEqual(binary_search(arr, 0, True), -1)

    def test_binary_search_leftmost(self):
        arr = [1, 2, 2, 2, 3]
        self.assertEqual(binary_search(arr, 2, True), 1)
        self.assertEqual(binary_search(arr, 2, False), 3)

    def test_binary_search_rightmost(self):
        arr = [1, 2, 2, 2, 3]
        self.assertEqual(binary_search(arr, 2, True), 1)
        self.assertEqual(binary_search(arr, 2, False), 3)

    def test_count_and_indices(self):
        arr = [1, 2, 2, 2, 3]
        count, indices = count_and_indices(arr, 2)
        self.assertEqual(count, 3)
        self.assertEqual(indices, [1, 2, 3])

    def test_count_and_indices_nonexistent(self):
        arr = [1, 2, 3, 4, 5]
        count, indices = count_and_indices(arr, 6)
        self.assertEqual(count, 0)
        self.assertEqual(indices, [])

    def test_count_and_indices_empty_array(self):
        arr = []
        count, indices = count_and_indices(arr, 1)
        self.assertEqual(count, 0)
        self.assertEqual(indices, [])

    def test_count_and_indices_single_element(self):
        arr = [1]
        count, indices = count_and_indices(arr, 1)
        self.assertEqual(count, 1)
        self.assertEqual(indices, [0])

    def test_count_and_indices_single_element_nonexistent(self):
        arr = [1]
        count, indices = count_and_indices(arr, 2)
        self.assertEqual(count, 0)
        self.assertEqual(indices, [])

    def test_count_and_indices_sorted_array(self):
        arr = [1, 2, 3, 4, 5]
        count, indices = count_and_indices(arr, 3)
        self.assertEqual(count, 1)
        self.assertEqual(indices, [2])

    def test_count_and_indices_unsorted_array(self):
        arr = [5, 1, 2, 3, 4]
        count, indices = count_and_indices(arr, 3)
        self.assertEqual(count, 1)
        self.assertEqual(indices, [2])

    def test_count_and_indices_large_array(self):
        arr = list(range(1000000))
        count, indices = count_and_indices(arr, 500000)
        self.assertEqual(count, 1)
        self.assertEqual(indices, [500000])

    def test_count_and_indices_large_array_nonexistent(self):
        arr = list(range(1000000))
        count, indices = count_and_indices(arr, 500001)
        self.assertEqual(count, 0)
        self.assertEqual(indices, [])

    def test_count_and_indices_large_array_duplicate(self):
        arr = [1] * 1000000
        count, indices = count_and_indices(arr, 1)
        self.assertEqual(count, 1000000)
        self.assertEqual(indices, list(range(1000000)))

    def test_count_and_indices_large_array_duplicate_nonexistent(self):
        arr = [1] * 1000000
        count, indices = count_and_indices(arr, 2)
        self.assertEqual(count, 0)
        self.assertEqual(indices, [])

    def test_count_and_indices_large_array_sorted(self):
        arr = list(range(1000000))
        count, indices = count_and_indices(arr, 500000)
        self.assertEqual(count, 1)
        self.assertEqual(indices, [500000])

    def test_count_and_indices_large_array_unsorted(self):
        arr = list(range(1000000, 0, -1))
        count, indices = count_and_indices(arr, 500000)
        self.assertEqual(count, 1)
        self.assertEqual(indices, [500000])

    def test_count_and_indices_large_array_duplicate_sorted(self):
        arr = [1] * 1000000
        count, indices = count_and_indices(arr, 1)
        self.assertEqual(count, 1000000)
        self.assertEqual(indices, list(range(1000000)))

    def test_count_and_indices_large_array_duplicate_unsorted(self):
        arr = [1] * 1000000
        count, indices = count_and_indices(arr, 1)
        self.assertEqual(count, 1000000)
        self.assertEqual(indices, list(range(1000000)))

    def test_count_and_indices_large_array_sorted_nonexistent(self):
        arr = list(range(1000000))
        count, indices = count_and_indices(arr, 500001)
        self.assertEqual(count, 0)
        self.assertEqual(indices, [])

    def test_count_and_indices_large_array_unsorted_nonexistent(self):
        arr = list(range(1000000, 0, -1))
        count, indices = count_and_indices(arr, 500001)
        self.assertEqual(count, 0)
        self.assertEqual(indices, [])

    def test_count_and_indices_large_array_duplicate_sorted_nonexistent(self):
        arr = [1] * 1000000
        count, indices = count_and_indices(arr, 2)
        self.assertEqual(count, 0)
        self.assertEqual(indices, [])

    def test_count_and_indices_large_array_duplicate_unsorted_nonexistent(self):
        arr = [1] * 1000000
        count, indices = count_and_indices(arr, 2)
        self.assertEqual(count, 0)
        self.assertEqual(indices, [])

if __name__ == '__main__':
    unittest.main()

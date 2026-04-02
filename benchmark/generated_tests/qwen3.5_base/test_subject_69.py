import unittest

class TestBinarySearch(unittest.TestCase):
    def test_binary_search_success(self):
        arr = [1, 3, 5, 7, 9]
        target = 5
        self.assertEqual(binary_search(arr, target), 2)

    def test_binary_search_not_found(self):
        arr = [1, 3, 5, 7, 9]
        target = 6
        self.assertEqual(binary_search(arr, target), -1)

    def test_binary_search_first_element(self):
        arr = [1, 3, 5, 7, 9]
        target = 1
        self.assertEqual(binary_search(arr, target), 0)

    def test_binary_search_last_element(self):
        arr = [1, 3, 5, 7, 9]
        target = 9
        self.assertEqual(binary_search(arr, target), 4)

    def test_binary_search_empty_array(self):
        arr = []
        target = 1
        self.assertEqual(binary_search(arr, target), -1)

    def test_binary_search_single_element(self):
        arr = [5]
        target = 5
        self.assertEqual(binary_search(arr, target), 0)

    def test_binary_search_single_element_not_found(self):
        arr = [5]
        target = 3
        self.assertEqual(binary_search(arr, target), -1)

    def test_binary_search_sorted_array(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        target = 5
        self.assertEqual(binary_search(arr, target), 4)

    def test_binary_search_unsorted_array(self):
        arr = [10, 5, 2, 8, 1, 9, 3, 7, 4, 6]
        target = 5
        self.assertEqual(binary_search(arr, target), -1)

if __name__ == '__main__':
    unittest.main()

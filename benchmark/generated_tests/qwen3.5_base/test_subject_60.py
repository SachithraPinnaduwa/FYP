import unittest

class TestBinarySearch(unittest.TestCase):
    def test_binary_search(self):
        arr = [1, 2, 3, 4, 5]
        x = 3
        result = binary_search(arr, x)
        self.assertEqual(result, 2)

    def test_binary_search_not_found(self):
        arr = [1, 2, 3, 4, 5]
        x = 6
        result = binary_search(arr, x)
        self.assertEqual(result, -1)

    def test_binary_search_first_element(self):
        arr = [1, 2, 3, 4, 5]
        x = 1
        result = binary_search(arr, x)
        self.assertEqual(result, 0)

    def test_binary_search_last_element(self):
        arr = [1, 2, 3, 4, 5]
        x = 5
        result = binary_search(arr, x)
        self.assertEqual(result, 4)

    def test_binary_search_empty_array(self):
        arr = []
        x = 1
        result = binary_search(arr, x)
        self.assertEqual(result, -1)

    def test_binary_search_single_element(self):
        arr = [1]
        x = 1
        result = binary_search(arr, x)
        self.assertEqual(result, 0)

    def test_binary_search_single_element_not_found(self):
        arr = [1]
        x = 2
        result = binary_search(arr, x)
        self.assertEqual(result, -1)

    def test_binary_search_sorted_array(self):
        arr = [1, 2, 3, 4, 5]
        x = 3
        result = binary_search(arr, x)
        self.assertEqual(result, 2)

    def test_binary_search_unsorted_array(self):
        arr = [5, 4, 3, 2, 1]
        x = 3
        result = binary_search(arr, x)
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()

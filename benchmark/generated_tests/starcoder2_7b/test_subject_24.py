import unittest

class TestBinarySearch(unittest.TestCase):
    def test_binary_search(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        target = 5
        self.assertEqual(binary_search(arr, target), 4)

    def test_binary_search_not_found(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        target = 11
        self.assertEqual(binary_search(arr, target), -1)

if __name__ == '__main__':
    unittest.main()
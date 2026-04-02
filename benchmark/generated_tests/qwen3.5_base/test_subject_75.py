import unittest

class TestReverseArray(unittest.TestCase):
    def test_reverse_array(self):
        arr = [1, 2, 3, 4, 5]
        reverseArray(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [5, 4, 3, 2, 1])

    def test_reverse_array_single_element(self):
        arr = [1]
        reverseArray(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [1])

    def test_reverse_array_empty_array(self):
        arr = []
        reverseArray(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [])

    def test_reverse_array_two_elements(self):
        arr = [1, 2]
        reverseArray(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [2, 1])

    def test_reverse_array_three_elements(self):
        arr = [1, 2, 3]
        reverseArray(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [3, 2, 1])

    def test_reverse_array_large_array(self):
        arr = list(range(1, 101))
        reverseArray(arr, 0, len(arr) - 1)
        self.assertEqual(arr, list(range(100, 0, -1)))

if __name__ == '__main__':
    unittest.main()

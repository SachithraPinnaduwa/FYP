import unittest

class TestReverseArray(unittest.TestCase):
    def test_reverse_array(self):
        arr = [1, 2, 3, 4, 5]
        reverseArray(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [5, 4, 3, 2, 1])

    def test_empty_array(self):
        arr = []
        reverseArray(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [])

    def test_single_element_array(self):
        arr = [1]
        reverseArray(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [1])

    def test_odd_length_array(self):
        arr = [1, 2, 3, 4, 5, 6]
        reverseArray(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [6, 5, 4, 3, 2, 1])

    def test_even_length_array(self):
        arr = [1, 2, 3, 4, 5, 6, 7]
        reverseArray(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [7, 6, 5, 4, 3, 2, 1])

if __name__ == '__main__':
    unittest.main()
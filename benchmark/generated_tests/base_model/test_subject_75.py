import unittest

class TestReverseArray(unittest.TestCase):

    def test_reverseArray_empty_array(self):
        arr = []
        reverseArray(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [])

    def test_reverseArray_single_element(self):
        arr = [1]
        reverseArray(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [1])

    def test_reverseArray_two_elements(self):
        arr = [1, 2]
        reverseArray(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [2, 1])

    def test_reverseArray_odd_number_of_elements(self):
        arr = [1, 2, 3, 4, 5]
        reverseArray(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [5, 4, 3, 2, 1])

    def test_reverseArray_even_number_of_elements(self):
        arr = [1, 2, 3, 4]
        reverseArray(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [4, 3, 2, 1])

    def test_reverseArray_start_index_greater_than_end_index(self):
        arr = [1, 2, 3, 4]
        reverseArray(arr, 2, 1)
        self.assertEqual(arr, [1, 2, 3, 4])

if __name__ == '__main__':
    unittest.main()
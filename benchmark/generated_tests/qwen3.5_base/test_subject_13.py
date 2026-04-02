import unittest

class TestUniqueSortedArray(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(unique_sorted_array([]), [])

    def test_single_element(self):
        self.assertEqual(unique_sorted_array([1]), [1])

    def test_all_same_elements(self):
        self.assertEqual(unique_sorted_array([1, 1, 1]), [1])

    def test_all_unique_elements(self):
        self.assertEqual(unique_sorted_array([1, 2, 3]), [1, 2, 3])

    def test_unsorted_array(self):
        self.assertEqual(unique_sorted_array([3, 1, 2]), [1, 2, 3])

    def test_array_with_duplicates(self):
        self.assertEqual(unique_sorted_array([1, 2, 2, 3, 3, 3]), [1, 2, 3])

    def test_large_array(self):
        large_array = list(range(1, 1000))
        large_array.append(1)
        large_array.append(500)
        self.assertEqual(unique_sorted_array(large_array), list(range(1, 1000)))

if __name__ == '__main__':
    unittest.main()

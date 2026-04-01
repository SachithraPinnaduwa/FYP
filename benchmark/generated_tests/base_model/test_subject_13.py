import unittest

class TestUniqueSortedArray(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(unique_sorted_array([]), [])

    def test_single_element_array(self):
        self.assertEqual(unique_sorted_array([5]), [5])

    def test_sorted_array_with_duplicates(self):
        self.assertEqual(unique_sorted_array([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_unsorted_array_with_duplicates(self):
        self.assertEqual(unique_sorted_array([5, 3, 8, 6, 3, 9, 5]), [3, 5, 6, 8, 9])

    def test_array_with_negative_numbers(self):
        self.assertEqual(unique_sorted_array([-2, -3, -1, -3, -2]), [-3, -2, -1])

    def test_array_with_all_duplicates(self):
        self.assertEqual(unique_sorted_array([7, 7, 7, 7, 7]), [7])

    def test_large_array(self):
        large_array = list(range(1000)) + list(range(500, 1500))
        sorted_unique = sorted(list(set(large_array)))
        self.assertEqual(unique_sorted_array(large_array), sorted_unique)

if __name__ == '__main__':
    unittest.main()
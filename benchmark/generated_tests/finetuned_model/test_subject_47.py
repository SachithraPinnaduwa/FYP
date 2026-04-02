import unittest

class TestMedian(unittest.TestCase):
    def test_median_odd_list(self):
        self.assertEqual(median([1, 3, 3, 6, 7, 8, 9], lambda x, y: x-y), 6)
        self.assertEqual(median([1, 2, 3, 4, 5, 6], lambda x, y: x-y), 3.5)
        self.assertEqual(median([1, 2, 3, 4, 5, 6, 8], lambda x, y: x-y), 3.5)

    def test_median_even_list(self):
        self.assertEqual(median([1, 3, 3, 6, 7, 8, 9, 10], lambda x, y: x-y), 6.5)
        self.assertEqual(median([1, 2, 3, 4, 5, 6, 8, 9, 10], lambda x, y: x-y), 5.5)
        self.assertEqual(median([1, 2, 3, 4, 5, 6, 8, 9, 10, 10], lambda x, y: x-y), 5.5)

    def test_median_with_duplicates(self):
        self.assertEqual(median([1, 1, 2, 3, 4, 5, 5, 6, 7], lambda x, y: x-y), 4)
        self.assertEqual(median([1, 1, 2, 3, 4, 5, 5, 6, 7, 7], lambda x, y: x-y), 4.5)

    def test_median_with_mismatched_data_types(self):
        self.assertEqual(median([1, 2, 3, 4, 5], lambda x, y: x-y if isinstance(x, int) and isinstance(y, int) else None), 3)
        self.assertEqual(median([1, 2, 3, 4, 5, "a"], lambda x, y: x-y if isinstance(x, int) and isinstance(y, int) else None), None)
        self.assertEqual(median([1, 2, 3, 4, 5, 6, "a"], lambda x, y: x-y if isinstance(x, int) and isinstance(y, int) else None), None)

    def test_median_with_empty_list(self):
        self.assertEqual(median([], lambda x, y: x-y), None)

if __name__ == '__main__':
    unittest.main()
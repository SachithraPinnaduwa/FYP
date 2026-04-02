from subject_47 import *

import unittest

class TestMedianFunction(unittest.TestCase):
    def test_median_odd_list(self):
        self.assertEqual(median([1, 3, 2], lambda x, y: x - y), 2)

    def test_median_even_list(self):
        self.assertEqual(median([1, 2, 3, 4], lambda x, y: x - y), 2.5)

    def test_median_with_duplicates(self):
        self.assertEqual(median([1, 2, 2, 3], lambda x, y: x - y), 2)

    def test_median_empty_list(self):
        self.assertIsNone(median([], lambda x, y: x - y))

    def test_median_with_mismatched_data_types(self):
        self.assertIsNone(median([1, '2', 3], lambda x, y: x - y))

if __name__ == '__main__':
    unittest.main()
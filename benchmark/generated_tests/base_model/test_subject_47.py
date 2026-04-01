import unittest

class TestMedian(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(median([], lambda x, y: x < y))

    def test_single_element_list(self):
        self.assertEqual(median([5], lambda x, y: x < y), 5)

    def test_odd_number_of_elements(self):
        self.assertEqual(median([3, 1, 4, 1, 5, 9, 2], lambda x, y: x < y), 3)

    def test_even_number_of_elements(self):
        self.assertEqual(median([3, 1, 4, 1, 5, 9, 2, 6], lambda x, y: x < y), 3.5)

    def test_duplicates(self):
        self.assertEqual(median([1, 2, 2, 3, 4, 4, 5], lambda x, y: x < y), 3)

    def test_mismatched_data_types(self):
        self.assertIsNone(median(['a', 'b', 'c'], lambda x, y: x < y))
        self.assertIsNone(median([1, 'b', 3], lambda x, y: x < y))

    def test_custom_comparison_function(self):
        def custom_cmp(x, y):
            return str(x) < str(y)
        self.assertEqual(median([3, 1, 4, 1, 5, 9, 2], custom_cmp), 1)

if __name__ == '__main__':
    unittest.main()
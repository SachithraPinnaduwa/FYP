import unittest

class TestFindMedian(unittest.TestCase):
    def test_find_median_even_length(self):
        self.assertEqual(find_median([1, 3, 3, 6, 7, 8, 9]), 6)

    def test_find_median_odd_length(self):
        self.assertEqual(find_median([1, 2, 3, 4, 5, 6, 8, 9]), 4)

    def test_find_median_single_element(self):
        self.assertEqual(find_median([7]), 7)

    def test_find_median_multiple_duplicates(self):
        self.assertEqual(find_median([2, 2, 3, 3, 3, 4, 4, 4, 4]), 3)

    def test_find_median_negative_numbers(self):
        self.assertEqual(find_median([-5, -3, -1, 0, 1, 2, 3, 5]), 0)

    def test_find_median_mixed_numbers(self):
        self.assertEqual(find_median([-3, 1, 2, 4, 5, 6]), 3)

if __name__ == '__main__':
    unittest.main()
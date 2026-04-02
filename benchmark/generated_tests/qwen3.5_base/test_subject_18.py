import unittest

class TestCalculateMedian(unittest.TestCase):
    def test_median_odd_length(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(calculate_median(arr), 3)

    def test_median_even_length(self):
        arr = [1, 2, 4, 5]
        self.assertEqual(calculate_median(arr), 4)

    def test_median_single_element(self):
        arr = [1]
        self.assertEqual(calculate_median(arr), 1)

    def test_median_empty_array(self):
        arr = []
        self.assertRaises(ValueError, calculate_median, arr)

    def test_median_negative_numbers(self):
        arr = [-5, -2, 0, 3, 7]
        self.assertEqual(calculate_median(arr), 0)

    def test_median_duplicate_numbers(self):
        arr = [1, 1, 2, 3, 3]
        self.assertEqual(calculate_median(arr), 2)

    def test_median_unsorted_array(self):
        arr = [5, 1, 3, 2, 4]
        self.assertEqual(calculate_median(arr), 3)

if __name__ == '__main__':
    unittest.main()

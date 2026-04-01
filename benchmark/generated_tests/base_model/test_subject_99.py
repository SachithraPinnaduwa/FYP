import unittest

class TestSumEven(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sum_even([]), 0)

    def test_single_odd_number(self):
        self.assertEqual(sum_even([1]), 0)

    def test_single_even_number(self):
        self.assertEqual(sum_even([2]), 2)

    def test_multiple_numbers_with_no_evens(self):
        self.assertEqual(sum_even([1, 3, 5, 7]), 0)

    def test_multiple_numbers_with_one_even(self):
        self.assertEqual(sum_even([1, 2, 3, 4]), 6)

    def test_multiple_numbers_with_all_evens(self):
        self.assertEqual(sum_even([2, 4, 6, 8]), 20)

    def test_mixed_positive_and_negative_numbers(self):
        self.assertEqual(sum_even([-2, -1, 0, 1, 2]), 0)

    def test_large_numbers(self):
        self.assertEqual(sum_even([100, 200, 300, 400]), 1000)

if __name__ == '__main__':
    unittest.main()
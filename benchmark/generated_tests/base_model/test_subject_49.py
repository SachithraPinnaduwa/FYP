import unittest

class TestFindMedian(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(find_median([]), None)

    def test_single_element(self):
        self.assertEqual(find_median([5]), 5)

    def test_odd_number_of_elements(self):
        self.assertEqual(find_median([3, 1, 2, 4, 5]), 3)

    def test_even_number_of_elements(self):
        self.assertEqual(find_median([1, 2, 3, 4]), 2)

    def test_negative_numbers(self):
        self.assertEqual(find_median([-5, -3, -1, 0, 2, 4]), 0)

    def test_repeated_elements(self):
        self.assertEqual(find_median([1, 1, 2, 2, 3, 3]), 2)

    def test_large_numbers(self):
        self.assertEqual(find_median([1000, 2000, 3000, 4000, 5000]), 3000)

if __name__ == '__main__':
    unittest.main()
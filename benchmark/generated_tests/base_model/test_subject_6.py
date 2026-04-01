import unittest

class TestFindMedian(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(find_median([]), None)

    def test_single_element(self):
        self.assertEqual(find_median([5]), 5)

    def test_even_number_of_elements(self):
        self.assertEqual(find_median([3, 1, 4, 1, 5, 9]), 3.5)
        self.assertEqual(find_median([10, 2, 8, 7, 6, 1]), 3.5)

    def test_odd_number_of_elements(self):
        self.assertEqual(find_median([1, 2, 3, 4, 5]), 3)
        self.assertEqual(find_median([7, 3, 1, 4, 5, 2, 6]), 3.5)

if __name__ == '__main__':
    unittest.main()
import unittest

class TestFindMedian(unittest.TestCase):
    def test_even_length_list(self):
        self.assertEqual(find_median([1, 2, 3, 4]), 2.5)
        self.assertEqual(find_median([10, 20]), 15)
        self.assertEqual(find_median([1, 100]), 50.5)

    def test_odd_length_list(self):
        self.assertEqual(find_median([1, 2, 3]), 2)
        self.assertEqual(find_median([1, 2, 3, 4, 5]), 3)
        self.assertEqual(find_median([10, 20, 30]), 20)

    def test_single_element_list(self):
        self.assertEqual(find_median([5]), 5)
        self.assertEqual(find_median([100]), 100)

    def test_negative_numbers(self):
        self.assertEqual(find_median([-1, -2, -3]), -2)
        self.assertEqual(find_median([-10, -20]), -15)

    def test_duplicate_numbers(self):
        self.assertEqual(find_median([1, 1, 2, 3]), 2)
        self.assertEqual(find_median([1, 1, 1, 1]), 1)

    def test_large_numbers(self):
        self.assertEqual(find_median([1000000, 2000000]), 1500000)
        self.assertEqual(find_median([1, 1000000]), 500000.5)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            find_median([])

if __name__ == '__main__':
    unittest.main()

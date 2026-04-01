import unittest

class TestMinimumDifferenceOfSums(unittest.TestCase):
    def test_minimum_difference_of_sums(self):
        self.assertEqual(minimum_difference_of_sums(3), 0)
        self.assertEqual(minimum_difference_of_sums(5), 1)
        self.assertEqual(minimum_difference_of_sums(6), 1)
        self.assertEqual(minimum_difference_of_sums(7), 0)
        self.assertEqual(minimum_difference_of_sums(8), 0)
        self.assertEqual(minimum_difference_of_sums(9), 1)
        self.assertEqual(minimum_difference_of_sums(10), 0)
        self.assertEqual(minimum_difference_of_sums(11), 1)
        self.assertEqual(minimum_difference_of_sums(12), 1)
        self.assertEqual(minimum_difference_of_sums(20), 0)

if __name__ == '__main__':
    unittest.main()
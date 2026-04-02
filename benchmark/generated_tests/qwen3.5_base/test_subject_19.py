import unittest

class TestMinimumDifferenceOfSums(unittest.TestCase):
    """
    Test suite for the minimum_difference_of_sums function.
    """

    def test_basic_cases(self):
        """
        Test basic cases for small values of n.
        """
        self.assertEqual(minimum_difference_of_sums(1), 0)
        self.assertEqual(minimum_difference_of_sums(2), 1)
        self.assertEqual(minimum_difference_of_sums(3), 0)
        self.assertEqual(minimum_difference_of_sums(4), 1)
        self.assertEqual(minimum_difference_of_sums(5), 0)

    def test_large_values(self):
        """
        Test for larger values of n to ensure correctness.
        """
        self.assertEqual(minimum_difference_of_sums(10), 0)
        self.assertEqual(minimum_difference_of_sums(11), 1)
        self.assertEqual(minimum_difference_of_sums(100), 0)
        self.assertEqual(minimum_difference_of_sums(101), 1)

    def test_edge_cases(self):
        """
        Test edge cases such as n = 0 (if applicable) and n = 1.
        """
        self.assertEqual(minimum_difference_of_sums(0), 0)
        self.assertEqual(minimum_difference_of_sums(1), 0)

if __name__ == '__main__':
    unittest.main()

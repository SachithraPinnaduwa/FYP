import unittest

class TestMinimumDifferenceOfSums(unittest.TestCase):
    # Test case for an even value of n
    def test_even_n(self):
        # Given n is 6, the sum of the sequence 1, 2, ..., 6 is 21.
        # The minimum possible difference between the sums of two sets is 1.
        self.assertEqual(minimum_difference_of_sums(6), 1)

    # Test case for an odd value of n
    def test_odd_n(self):
        # Given n is 5, the sum of the sequence 1, 2, ..., 5 is 15.
        # The minimum possible difference between the sums of two sets is 0.
        self.assertEqual(minimum_difference_of_sums(5), 0)

    # Test case for n equal to 1
    def test_n_equal_to_1(self):
        # Given n is 1, the sum of the sequence 1 is 1.
        # The minimum possible difference between the sums of two sets is 0.
        self.assertEqual(minimum_difference_of_sums(1), 0)

    # Test case for n equal to 0
    def test_n_equal_to_0(self):
        # Given n is 0, the function should return 0.
        self.assertEqual(minimum_difference_of_sums(0), 0)

    # Test case for n equal to 2
    def test_n_equal_to_2(self):
        # Given n is 2, the sum of the sequence 1, 2 is 3.
        # The minimum possible difference between the sums of two sets is 1.
        self.assertEqual(minimum_difference_of_sums(2), 1)

    # Test case for n equal to 100
    def test_n_equal_to_100(self):
        # Given n is 100, the sum of the sequence 1, 2, ..., 100 is 5050.
        # The minimum possible difference between the sums of two sets is 0.
        self.assertEqual(minimum_difference_of_sums(100), 0)

    # Test case for n equal to 1000000000
    def test_n_equal_to_1000000000(self):
        # Given n is 1000000000, the sum of the sequence 1, 2, ..., 1000000000 is 500000000500000000.
        # The minimum possible difference between the sums of two sets is 1.
        self.assertEqual(minimum_difference_of_sums(1000000000), 1)
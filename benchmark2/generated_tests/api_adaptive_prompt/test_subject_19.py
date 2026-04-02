from subject_19 import *

import unittest

def minimum_difference_of_sums(n: int) -> int:
    """
    Calculate the minimum possible value of the absolute difference between the sums of two sets A and B
    when dividing the sequence 1, 2, ..., n into two sets.

    Parameters:
    n (int): The integer representing the length of the sequence from 1 to n.

    Returns:
    int: The minimum possible value of the absolute difference between the sums of two sets A and B.
    """
    return (n * (n + 1) // 2) % 2

class TestMinimumDifferenceOfSums(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(minimum_difference_of_sums(1000000), 0)

    def test_edge_case_n_1(self):
        self.assertEqual(minimum_difference_of_sums(1), 0)

    def test_edge_case_n_2000000(self):
        self.assertEqual(minimum_difference_of_sums(2000000), 0)

    def test_error_handling_negative_input(self):
        with self.assertRaises(ValueError):
            minimum_difference_of_sums(-1)

if __name__ == '__main__':
    unittest.main()
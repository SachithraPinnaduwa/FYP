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
    def test_cases(self):
        self.assertEqual(minimum_difference_of_sums(3), 0)
        self.assertEqual(minimum_difference_of_sums(5), 1)
        self.assertEqual(minimum_difference_of_sums(6), 1)
        self.assertEqual(minimum_difference_of_sums(1), 0)
        self.assertEqual(minimum_difference_of_sums(2), 0)
        self.assertEqual(minimum_difference_of_sums(10), 0)
        self.assertEqual(minimum_difference_of_sums(100), 0)
        self.assertEqual(minimum_difference_of_sums(1000), 0)
        self.assertEqual(minimum_difference_of_sums(10000), 0)
        self.assertEqual(minimum_difference_of_sums(100000), 0)
        self.assertEqual(minimum_difference_of_sums(1000000), 0)
        self.assertEqual(minimum_difference_of_sums(10000000), 0)
        self.assertEqual(minimum_difference_of_sums(100000000), 0)
        self.assertEqual(minimum_difference_of_sums(1000000000), 0)
        self.assertEqual(minimum_difference_of_sums(2000000000), 0)

if __name__ == '__main__':
    unittest.main()
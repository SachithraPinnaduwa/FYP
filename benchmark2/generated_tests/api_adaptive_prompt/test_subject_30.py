from subject_30 import *

import unittest

def sum_of_primes(n):
    """
    Calculate the sum of all prime numbers between 1 and n (inclusive) using a list comprehension.

    Args:
        n (int): The upper limit for the range of prime numbers.

    Returns:
        int: The sum of prime numbers between 1 and n.
    """
    return sum([num for num in range(2, n + 1) if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))])

class TestSumOfPrimes(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(sum_of_primes(10), 17)

    def test_edge_case(self):
        self.assertEqual(sum_of_primes(2), 2)

    def test_error_handling(self):
        with self.assertRaises(ValueError):
            sum_of_primes(1)

if __name__ == '__main__':
    unittest.main()
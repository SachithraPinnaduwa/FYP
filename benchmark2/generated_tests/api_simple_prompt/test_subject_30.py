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
    def test_sum_of_primes(self):
        self.assertEqual(sum_of_primes(10), 17)
        self.assertEqual(sum_of_primes(5), 10)
        self.assertEqual(sum_of_primes(20), 77)
        self.assertEqual(sum_of_primes(1), 0)
        self.assertEqual(sum_of_primes(100), 1060)

if __name__ == '__main__':
    unittest.main()
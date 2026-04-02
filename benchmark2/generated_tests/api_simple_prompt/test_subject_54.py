from subject_54 import *

import unittest

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def contains_three_odd_primes(array):
    odd_primes = [num for num in array if num % 2 != 0 and is_prime(num)]
    return len(odd_primes) >= 3 and is_prime(sum(odd_primes))

class TestContainsThreeOddPrimes(unittest.TestCase):
    def test_contains_three_odd_primes(self):
        self.assertTrue(contains_three_odd_primes([3, 5, 7, 11, 13]))
        self.assertFalse(contains_three_odd_primes([2, 4, 6, 8, 10]))
        self.assertFalse(contains_three_odd_primes([3, 5, 7]))
        self.assertFalse(contains_three_odd_primes([3, 5]))
        self.assertFalse(contains_three_odd_primes([11, 13, 17, 19, 23]))
        self.assertTrue(contains_three_odd_primes([11, 13, 17, 19, 23, 29]))
        self.assertFalse(contains_three_odd_primes([2, 3, 5, 7, 11, 13, 17]))
        self.assertTrue(contains_three_odd_primes([2, 3, 5, 7, 11, 13, 17, 19]))
        self.assertFalse(contains_three_odd_primes([2, 3, 5, 7, 11, 13, 17, 19, 23]))
        self.assertTrue(contains_three_odd_primes([2, 3, 5, 7, 11, 13, 17, 19, 23, 29]))

if __name__ == '__main__':
    unittest.main()
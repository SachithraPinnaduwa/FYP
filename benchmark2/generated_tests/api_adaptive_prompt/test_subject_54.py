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
    def test_normal_case_with_three_odd_primes_summing_to_prime(self):
        self.assertTrue(contains_three_odd_primes([3, 5, 7, 11, 13]))

    def test_normal_case_with_less_than_three_odd_primes(self):
        self.assertFalse(contains_three_odd_primes([2, 4, 6, 8, 10]))

    def test_normal_case_with_three_odd_primes_summing_to_non_prime(self):
        self.assertFalse(contains_three_odd_primes([3, 5, 7, 10, 12]))

    def test_edge_case_with_empty_array(self):
        self.assertFalse(contains_three_odd_primes([]))

    def test_edge_case_with_array_with_only_one_element(self):
        self.assertFalse(contains_three_odd_primes([2]))

    def test_error_handling_with_non_integer_values(self):
        self.assertFalse(contains_three_odd_primes([3, 5, 7, 'a', 11]))

if __name__ == '__main__':
    unittest.main()
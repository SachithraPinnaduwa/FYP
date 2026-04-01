import unittest

class TestContainsThreeOddPrimes(unittest.TestCase):
    def test_no_odd_primes(self):
        # Test case with no odd prime numbers
        array = [2, 4, 6, 8, 10]
        self.assertFalse(contains_three_odd_primes(array))

    def test_less_than_three_odd_primes(self):
        # Test case with less than three odd prime numbers
        array = [3, 5, 7, 10, 12]
        self.assertFalse(contains_three_odd_primes(array))

    def test_three_odd_primes_sum_not_prime(self):
        # Test case with three odd prime numbers but their sum is not prime
        array = [3, 5, 7, 10, 2]
        self.assertFalse(contains_three_odd_primes(array))

    def test_three_odd_primes_sum_prime(self):
        # Test case with three odd prime numbers and their sum is prime
        array = [3, 5, 7, 10, 12]
        self.assertTrue(contains_three_odd_primes(array))

    def test_four_odd_primes_sum_prime(self):
        # Test case with more than three odd prime numbers and their sum is prime
        array = [3, 5, 7, 11, 12]
        self.assertTrue(contains_three_odd_primes(array))

    def test_large_array(self):
        # Test case with a large array
        array = [i for i in range(1, 1000) if i % 2 != 0 and is_prime(i)]
        self.assertTrue(contains_three_odd_primes(array))
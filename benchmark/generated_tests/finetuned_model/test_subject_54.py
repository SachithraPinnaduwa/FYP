import unittest

class TestContainsThreeOddPrimes(unittest.TestCase):
    def test_empty_array(self):
        self.assertFalse(contains_three_odd_primes([]))

    def test_no_odd_primes(self):
        self.assertFalse(contains_three_odd_primes([2, 4, 6, 8]))

    def test_three_odd_primes(self):
        self.assertTrue(contains_three_odd_primes([3, 5, 7]))

    def test_more_than_three_odd_primes(self):
        self.assertTrue(contains_three_odd_primes([3, 5, 7, 11, 13]))

    def test_no_sum_is_prime(self):
        self.assertFalse(contains_three_odd_primes([3, 5, 9]))

    def test_single_odd_prime(self):
        self.assertFalse(contains_three_odd_primes([3]))

    def test_multiple_pairs_with_prime_sum(self):
        self.assertTrue(contains_three_odd_primes([3, 5, 7, 11]))

    def test_single_even_prime(self):
        self.assertFalse(contains_three_odd_primes([2, 3, 5]))

    def test_single_odd_composite(self):
        self.assertFalse(contains_three_odd_primes([3, 9, 11]))

    def test_negative_numbers(self):
        self.assertFalse(contains_three_odd_primes([-3, -5, -7]))

    def test_single_negative_number(self):
        self.assertFalse(contains_three_odd_primes([-3]))

if __name__ == '__main__':
    unittest.main()
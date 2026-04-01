import unittest

class TestContainsThreeOddPrimes(unittest.TestCase):

    def test_empty_array(self):
        self.assertFalse(contains_three_odd_primes([]))

    def test_no_odd_primes(self):
        self.assertFalse(contains_three_odd_primes([2, 4, 6, 8]))

    def test_less_than_three_odd_primes(self):
        self.assertFalse(contains_three_odd_primes([3, 7, 11]))

    def test_three_odd_primes_not_summing_to_prime(self):
        self.assertFalse(contains_three_odd_primes([3, 5, 9]))

    def test_three_odd_primes_summing_to_prime(self):
        self.assertTrue(contains_three_odd_primes([3, 5, 7]))

    def test_four_odd_primes(self):
        self.assertTrue(contains_three_odd_primes([3, 5, 7, 11]))

    def test_mixed_numbers(self):
        self.assertTrue(contains_three_odd_primes([2, 3, 5, 7, 11]))

if __name__ == '__main__':
    unittest.main()
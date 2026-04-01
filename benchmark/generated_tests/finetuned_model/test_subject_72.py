import unittest

class TestPerfectPrimeFunction(unittest.TestCase):

    def test_perfect_prime(self):
        # Test case for a known perfect prime number
        self.assertTrue(is_perfect_prime(7))

    def test_not_perfect_prime(self):
        # Test case for a number that is not a perfect prime
        self.assertFalse(is_perfect_prime(8))

    def test_prime_not_perfect(self):
        # Test case for a prime number that is not a perfect prime
        self.assertFalse(is_perfect_prime(3))

    def test_non_prime_not_perfect(self):
        # Test case for a non-prime number that is not a perfect prime
        self.assertFalse(is_perfect_prime(4))

    def test_number_with_no_divisors(self):
        # Test case for a number with no proper divisors (other than 1)
        self.assertFalse(is_perfect_prime(2))

    def test_number_with_multiple_divisors(self):
        # Test case for a number with multiple proper divisors
        self.assertFalse(is_perfect_prime(6))

    def test_number_with_large_divisors(self):
        # Test case for a number with large proper divisors
        self.assertFalse(is_perfect_prime(28))
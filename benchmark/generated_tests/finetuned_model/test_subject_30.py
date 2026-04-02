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
    def test_small_range(self):
        self.assertEqual(sum_of_primes(5), 10)

    def test_large_range(self):
        self.assertEqual(sum_of_primes(100), 1060)

    def test_single_prime(self):
        self.assertEqual(sum_of_primes(2), 2)

    def test_no_primes(self):
        self.assertEqual(sum_of_primes(1), 0)

    def test_all_primes(self):
        self.assertEqual(sum_of_primes(19), 77)

    def test_prime_between_100_and_200(self):
        self.assertEqual(sum_of_primes(150), 4227)

    def test_prime_between_200_and_300(self):
        self.assertEqual(sum_of_primes(250), 7612)

    def test_prime_between_300_and_400(self):
        self.assertEqual(sum_of_primes(350), 13003)

    def test_prime_between_400_and_500(self):
        self.assertEqual(sum_of_primes(450), 21536)

if __name__ == '__main__':
    unittest.main()
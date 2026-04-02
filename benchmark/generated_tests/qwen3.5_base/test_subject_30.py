import unittest

class TestSumOfPrimes(unittest.TestCase):
    """
    Test suite for the sum_of_primes function.
    """

    def test_sum_of_primes_1(self):
        """
        Test case for n = 1.
        Expected result: 0 (no prime numbers between 1 and 1).
        """
        self.assertEqual(sum_of_primes(1), 0)

    def test_sum_of_primes_2(self):
        """
        Test case for n = 2.
        Expected result: 2 (only prime number is 2).
        """
        self.assertEqual(sum_of_primes(2), 2)

    def test_sum_of_primes_10(self):
        """
        Test case for n = 10.
        Expected result: 17 (primes: 2, 3, 5, 7).
        """
        self.assertEqual(sum_of_primes(10), 17)

    def test_sum_of_primes_100(self):
        """
        Test case for n = 100.
        Expected result: 1060 (sum of primes up to 100).
        """
        self.assertEqual(sum_of_primes(100), 1060)

    def test_sum_of_primes_1000(self):
        """
        Test case for n = 1000.
        Expected result: 76127 (sum of primes up to 1000).
        """
        self.assertEqual(sum_of_primes(1000), 76127)

if __name__ == '__main__':
    unittest.main()

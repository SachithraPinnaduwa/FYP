import unittest

class TestSumOfPrimes(unittest.TestCase):

    def test_sum_of_primes(self):
        # Test case 1: Sum of primes up to 10
        self.assertEqual(sum_of_primes(10), 17)

        # Test case 2: Sum of primes up to 5
        self.assertEqual(sum_of_primes(5), 10)

        # Test case 3: Sum of primes up to 2
        self.assertEqual(sum_of_primes(2), 2)

        # Test case 4: Sum of primes up to 20
        self.assertEqual(sum_of_primes(20), 77)

        # Test case 5: Sum of primes up to 1
        with self.assertRaises(ValueError):
            sum_of_primes(1)

        # Test case 6: Sum of primes up to 0
        with self.assertRaises(ValueError):
            sum_of_primes(0)

        # Test case 7: Sum of primes up to 100
        self.assertEqual(sum_of_primes(100), 1060)

        # Test case 8: Sum of primes up to 1000
        self.assertEqual(sum_of_primes(1000), 76127)

if __name__ == '__main__':
    unittest.main()
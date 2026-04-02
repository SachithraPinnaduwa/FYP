import unittest

class TestContainsThreeOddPrimes(unittest.TestCase):
    def test_contains_three_odd_primes(self):
        self.assertEqual(contains_three_odd_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), False)
        self.assertEqual(contains_three_odd_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 11]), True)
        self.assertEqual(contains_three_odd_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 13]), True)
        self.assertEqual(contains_three_odd_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 17]), True)
        self.assertEqual(contains_three_odd_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 19]), True)
        self.assertEqual(contains_three_odd_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 23]), True)
        self.assertEqual(contains_three_odd_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 29]), True)
        self.assertEqual(contains_three_odd_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 31]), True)
        self.assertEqual(contains_three_odd_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 37]), True)
        self.assertEqual(contains_three_odd_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 41]), True)
        self.assertEqual(contains_three_odd_primes([1, 2,
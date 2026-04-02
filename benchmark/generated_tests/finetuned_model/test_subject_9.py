import unittest

class TestNthPrime(unittest.TestCase):
    def test_nth_prime(self):
        self.assertEqual(nth_prime(1), 2)
        self.assertEqual(nth_prime(2), 3)
        self.assertEqual(nth_prime(3), 5)
        self.assertEqual(nth_prime(4), 7)
        self.assertEqual(nth_prime(5), 11)
        self.assertEqual(nth_prime(10), 29)
        self.assertEqual(nth_prime(100), 541)
        self.assertEqual(nth_prime(1000), 7919)
        self.assertEqual(nth_prime(10001), 104743)
        self.assertEqual(nth_prime(100000), 1299709)

if __name__ == '__main__':
    unittest.main()
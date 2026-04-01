import unittest

class TestIsPerfectPrime(unittest.TestCase):

    def test_is_perfect_prime(self):
        self.assertTrue(is_perfect_prime(2))
        self.assertFalse(is_perfect_prime(3))
        self.assertTrue(is_perfect_prime(7))
        self.assertFalse(is_perfect_prime(11))
        self.assertTrue(is_perfect_prime(13))
        self.assertFalse(is_perfect_prime(17))
        self.assertTrue(is_perfect_prime(19))
        self.assertFalse(is_perfect_prime(23))
        self.assertTrue(is_perfect_prime(29))
        self.assertFalse(is_perfect_prime(31))
        self.assertTrue(is_perfect_prime(37))
        self.assertFalse(is_perfect_prime(41))
        self.assertTrue(is_perfect_prime(43))
        self.assertFalse(is_perfect_prime(47))

    def test_non_prime_numbers(self):
        self.assertFalse(is_perfect_prime(4))
        self.assertFalse(is_perfect_prime(6))
        self.assertFalse(is_perfect_prime(8))
        self.assertFalse(is_perfect_prime(9))
        self.assertFalse(is_perfect_prime(10))
        self.assertFalse(is_perfect_prime(12))
        self.assertFalse(is_perfect_prime(14))
        self.assertFalse(is_perfect_prime(15))
        self.assertFalse(is_perfect_prime(16))
        self.assertFalse(is_perfect_prime(18))
        self.assertFalse(is_perfect_prime(20))
        self.assertFalse(is_perfect_prime(21))
        self.assertFalse(is_perfect_prime(22))
        self.assertFalse(is_perfect_prime(24))
        self.assertFalse(is_perfect_prime(25))
        self.assertFalse(is_perfect_prime(26))
        self.assertFalse(is_perfect_prime(27))
        self.assertFalse(is_perfect_prime(28))
        self.assertFalse(is_perfect_prime(30))
        self.assertFalse(is_perfect_prime(32))
        self.assertFalse(is_perfect_prime(33))
        self.assertFalse(is_perfect_prime(34))
        self.assertFalse(is_perfect_prime(35))
        self.assertFalse(is_perfect_prime(36))
        self.assertFalse(is_perfect_prime(38))
        self.assertFalse(is_perfect_prime(39))
        self.assertFalse(is_perfect_prime(40))
        self.assertFalse(is_perfect_prime(42))
        self.assertFalse(is_perfect_prime(44))
        self.assertFalse(is_perfect_prime(45))
        self.assertFalse(is_perfect_prime(46))
        self.assertFalse(is_perfect_prime(48))
        self.assertFalse(is_perfect_prime(49))
        self.assertFalse(is_perfect_prime(50))

    def test_edge_cases(self):
        self.assertFalse(is_perfect_prime(1))  # Not considered prime
        self.assertFalse(is_perfect_prime(-2))  # Negative numbers not considered prime
        self.assertFalse(is_perfect_prime(0))  # Zero is not considered prime

if __name__ == '__main__':
    unittest.main()
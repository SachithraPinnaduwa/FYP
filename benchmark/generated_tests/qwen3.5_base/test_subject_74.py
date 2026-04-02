import unittest

class TestPrimeValidation(unittest.TestCase):
    def test_is_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(10))

    def test_validate_input(self):
        self.assertEqual(validate_input(), 5)
        self.assertEqual(validate_input(), 10)

if __name__ == '__main__':
    unittest.main()

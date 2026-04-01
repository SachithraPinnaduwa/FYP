import unittest

class TestPrimeNumbers(unittest.TestCase):

    def test_prime_numbers_between_1_and_10(self):
        self.assertEqual(entrance(1, 10), [2, 3, 5, 7])

    def test_prime_numbers_between_10_and_20(self):
        self.assertEqual(entrance(10, 20), [11, 13, 17, 19])

    def test_prime_numbers_between_1_and_1(self):
        self.assertEqual(entrance(1, 1), [])

    def test_prime_numbers_between_20_and_10(self):
        with self.assertRaises(ValueError):
            entrance(20, 10)

    def test_prime_numbers_between_30_and_40(self):
        self.assertEqual(entrance(30, 40), [31, 37])

    def test_prime_numbers_between_100_and_110(self):
        self.assertEqual(entrance(100, 110), [101, 103, 107, 109])

    def test_prime_numbers_between_negative_and_positive(self):
        self.assertEqual(entrance(-5, 5), [-5, -3, -2, 2, 3, 5])

if __name__ == '__main__':
    unittest.main()
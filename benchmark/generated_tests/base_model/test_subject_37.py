import unittest

class TestFindSecondSmallestOddPrimeGreaterThan100(unittest.TestCase):

    def test_find_second_smallest_odd_prime_greater_than_100(self):
        self.assertEqual(findSecondSmallestOddPrimeGreaterThan100([101, 103, 107, 109, 113]), 107)
        self.assertEqual(findSecondSmallestOddPrimeGreaterThan100([113, 101, 109, 103, 107]), 107)
        self.assertEqual(findSecondSmallestOddPrimeGreaterThan100([109, 113, 101, 103, 107]), 107)
        self.assertEqual(findSecondSmallestOddPrimeGreaterThan100([101, 107, 103, 113, 109]), 107)
        self.assertEqual(findSecondSmallestOddPrimeGreaterThan100([113, 109, 101, 107, 103]), 107)

    def test_array_with_no_primes(self):
        with self.assertRaises(ValueError):
            findSecondSmallestOddPrimeGreaterThan100([102, 104, 106, 108])

    def test_array_with_one_prime(self):
        with self.assertRaises(ValueError):
            findSecondSmallestOddPrimeGreaterThan100([101, 102, 104, 106, 108])

    def test_array_with_all_same_prime(self):
        with self.assertRaises(ValueError):
            findSecondSmallestOddPrimeGreaterThan100([107] * 5)

    def test_array_with_negative_numbers(self):
        with self.assertRaises(ValueError):
            findSecondSmallestOddPrimeGreaterThan100([-101, -103, -107, -109, -113])

    def test_array_with_floats(self):
        with self.assertRaises(TypeError):
            findSecondSmallestOddPrimeGreaterThan100([101.0, 103.0, 107.0, 109.0, 113.0])

if __name__ == '__main__':
    unittest.main()
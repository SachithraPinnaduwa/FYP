import unittest

class TestFindSecondSmallestOddPrimeGreaterThan100(unittest.TestCase):

    def test_all_numbers_greater_than_100(self):
        # Test case with all numbers greater than 100
        array = [101, 103, 105, 107, 109]
        self.assertEqual(findSecondSmallestOddPrimeGreaterThan100(array), 103)

    def test_no_prime_numbers(self):
        # Test case with no prime numbers
        array = [102, 104, 106, 108, 110]
        self.assertEqual(findSecondSmallestOddPrimeGreaterThan100(array), float('inf'))

    def test_all_prime_numbers(self):
        # Test case with all prime numbers
        array = [101, 103, 107, 109, 113]
        self.assertEqual(findSecondSmallestOddPrimeGreaterThan100(array), 103)

    def test_mixed_numbers(self):
        # Test case with mixed numbers
        array = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110]
        self.assertEqual(findSecondSmallestOddPrimeGreaterThan100(array), 103)

    def test_single_prime_number(self):
        # Test case with a single prime number
        array = [101]
        self.assertEqual(findSecondSmallestOddPrimeGreaterThan100(array), float('inf'))

    def test_duplicate_prime_numbers(self):
        # Test case with duplicate prime numbers
        array = [101, 101, 103, 103, 107, 107]
        self.assertEqual(findSecondSmallestOddPrimeGreaterThan100(array), 103)

    def test_prime_numbers_at_end(self):
        # Test case with prime numbers at the end of the array
        array = [100, 102, 104, 106, 108, 109, 110, 111, 113, 115, 117, 119, 121, 123, 125, 127, 129, 131, 133, 135, 137, 139, 141, 143, 145, 147, 149, 151, 153, 155, 157, 159, 161, 163, 165, 167, 169, 171, 173, 175, 177, 179, 181, 183, 185, 187, 189, 191, 193, 195, 197, 199]
        self.assertEqual(findSecondSmallestOddPrimeGreaterThan100(array), 103)
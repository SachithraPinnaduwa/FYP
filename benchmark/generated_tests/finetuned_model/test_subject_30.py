import unittest

class TestSumOfPrimes(unittest.TestCase):

    # Test case for small input
    def test_small_input(self):
        # Given
        n = 10
        expected_sum = 17  # 2 + 3 + 5 + 7 = 17

        # When
        result = sum_of_primes(n)

        # Then
        self.assertEqual(result, expected_sum)

    # Test case for large input
    def test_large_input(self):
        # Given
        n = 100
        expected_sum = 1060  # Sum of prime numbers between 1 and 100

        # When
        result = sum_of_primes(n)

        # Then
        self.assertEqual(result, expected_sum)

    # Test case for input 1
    def test_input_1(self):
        # Given
        n = 1
        expected_sum = 0  # No prime numbers between 1 and 1

        # When
        result = sum_of_primes(n)

        # Then
        self.assertEqual(result, expected_sum)

    # Test case for input 2
    def test_input_2(self):
        # Given
        n = 2
        expected_sum = 2  # Only one prime number between 1 and 2

        # When
        result = sum_of_primes(n)

        # Then
        self.assertEqual(result, expected_sum)

    # Test case for input 3
    def test_input_3(self):
        # Given
        n = 3
        expected_sum = 5  # Two prime numbers between 1 and 3

        # When
        result = sum_of_primes(n)

        # Then
        self.assertEqual(result, expected_sum)

    # Test case for input 1000
    def test_input_1000(self):
        # Given
        n = 1000
        expected_sum = 76127  # Sum of prime numbers between 1 and 1000

        # When
        result = sum_of_primes(n)

        # Then
        self.assertEqual(result, expected_sum)
import unittest

class TestNthPrimeFunction(unittest.TestCase):
    # Test case for the 1st prime number
    def test_first_prime(self):
        # The 1st prime number is 2
        self.assertEqual(nth_prime(1), 2)

    # Test case for the 2nd prime number
    def test_second_prime(self):
        # The 2nd prime number is 3
        self.assertEqual(nth_prime(2), 3)

    # Test case for the 3rd prime number
    def test_third_prime(self):
        # The 3rd prime number is 5
        self.assertEqual(nth_prime(3), 5)

    # Test case for the 10th prime number
    def test_tenth_prime(self):
        # The 10th prime number is 29
        self.assertEqual(nth_prime(10), 29)

    # Test case for the 20th prime number
    def test_twentieth_prime(self):
        # The 20th prime number is 71
        self.assertEqual(nth_prime(20), 71)

    # Test case for the 100th prime number
    def test_hundredth_prime(self):
        # The 100th prime number is 541
        self.assertEqual(nth_prime(100), 541)

    # Test case for the 1000th prime number
    def test_thousandth_prime(self):
        # The 1000th prime number is 7919
        self.assertEqual(nth_prime(1000), 7919)

    # Test case for the 1 prime number
    def test_single_prime(self):
        # The 1 prime number is 2
        self.assertEqual(nth_prime(1), 2)

    # Test case for the 2 prime number
    def test_two_prime(self):
        # The 2 prime number is 3
        self.assertEqual(nth_prime(2), 3)

    # Test case for the 3 prime number
    def test_three_prime(self):
        # The 3 prime number is 5
        self.assertEqual(nth_prime(3), 5)

    # Test case for the 10 prime number
    def test_ten_prime(self):
        # The 10 prime number is 29
        self.assertEqual(nth_prime(10), 29)

    # Test case for the 20 prime number
    def test_twenty_prime(self):
        # The 20 prime number is 71
        self.assertEqual(nth_prime(20), 71)

    # Test case for the 100 prime number
    def test_one_hundred_prime(self):
        # The 100 prime number is 541
        self.assertEqual(nth_prime(100), 541)

    # Test case for the 1000 prime number
    def test_one_thousand_prime(self):
        # The 1000 prime number is 7919
        self.assertEqual(nth_prime(1000), 7919)
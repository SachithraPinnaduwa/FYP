import unittest

class TestMultiplyFunction(unittest.TestCase):
    # Test case with two 1-digit numbers
    def test_small_numbers(self):
        self.assertEqual(multiply("3", "5"), "15")

    # Test case with two 2-digit numbers
    def test_two_digit_numbers(self):
        self.assertEqual(multiply("12", "34"), "408")

    # Test case with two 3-digit numbers
    def test_three_digit_numbers(self):
        self.assertEqual(multiply("123", "456"), "56088")

    # Test case with a number that ends with 0
    def test_number_ending_with_zero(self):
        self.assertEqual(multiply("123", "40"), "4920")

    # Test case with a number that starts with 0
    def test_number_starting_with_zero(self):
        self.assertEqual(multiply("012", "34"), "408")

    # Test case with two large numbers
    def test_large_numbers(self):
        self.assertEqual(multiply("12345678901234567890", "98765432109876543210"), "12193263111263526900419540207910341600")

    # Test case with a single digit and a large number
    def test_single_digit_and_large_number(self):
        self.assertEqual(multiply("2", "12345678901234567890"), "24691357802469135780")

    # Test case with a large number and a single digit
    def test_large_number_and_single_digit(self):
        self.assertEqual(multiply("12345678901234567890", "2"), "24691357802469135780")

    # Test case with two numbers with leading zeros
    def test_leading_zeros(self):
        self.assertEqual(multiply("00123", "00456"), "56088")

    # Test case with two numbers with trailing zeros
    def test_trailing_zeros(self):
        self.assertEqual(multiply("12300", "45600"), "560880000")

    # Test case with two negative numbers
    def test_negative_numbers(self):
        self.assertEqual(multiply("-123", "-456"), "56088")

    # Test case with a negative number and a positive number
    def test_mixed_sign_numbers(self):
        self.assertEqual(multiply("-123", "456"), "-56088")
        self.assertEqual(multiply("123", "-456"), "-56088")
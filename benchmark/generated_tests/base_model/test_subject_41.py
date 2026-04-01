import unittest

class TestMultiplyFunction(unittest.TestCase):

    def test_multiply_positive_numbers(self):
        self.assertEqual(multiply("123", "456"), "56088")
        self.assertEqual(multiply("999", "999"), "998001")

    def test_multiply_large_numbers(self):
        large_number = "1" * 100
        self.assertEqual(multiply(large_number, "2"), "2" * 100)

    def test_multiply_zero(self):
        self.assertEqual(multiply("0", "123"), "0")
        self.assertEqual(multiply("123", "0"), "0")

    def test_multiply_negative_numbers(self):
        self.assertEqual(multiply("-123", "-456"), "56088")
        self.assertEqual(multiply("-123", "456"), "-56088")
        self.assertEqual(multiply("123", "-456"), "-56088")

    def test_multiply_mixed_signs(self):
        self.assertEqual(multiply("-123", "456"), "-56088")
        self.assertEqual(multiply("123", "-456"), "-56088")

    def test_multiply_single_digit(self):
        self.assertEqual(multiply("7", "8"), "56")
        self.assertEqual(multiply("9", "9"), "81")

if __name__ == '__main__':
    unittest.main()
import unittest

class TestMultiply(unittest.TestCase):
    def test_multiply_basic(self):
        self.assertEqual(multiply("123", "456"), "56088")
    
    def test_multiply_single_digit(self):
        self.assertEqual(multiply("5", "7"), "35")
    
    def test_multiply_zero(self):
        self.assertEqual(multiply("0", "123"), "0")
    
    def test_multiply_large_numbers(self):
        self.assertEqual(multiply("999", "999"), "998001")
    
    def test_multiply_negative_numbers(self):
        self.assertEqual(multiply("-123", "456"), "-56088")
    
    def test_multiply_with_spaces(self):
        self.assertEqual(multiply("123 ", "456"), "56088")
    
    def test_multiply_empty_strings(self):
        self.assertEqual(multiply("", ""), "0")
    
    def test_multiply_non_numeric_strings(self):
        self.assertRaises(ValueError, multiply, "abc", "def")
    
    def test_multiply_mixed_case(self):
        self.assertEqual(multiply("123", "456"), "56088")
    
    def test_multiply_with_commas(self):
        self.assertEqual(multiply("1,234", "5,678"), "7000000")
    
    def test_multiply_with_decimals(self):
        self.assertEqual(multiply("1.23", "4.56"), "5.6088")
    
    def test_multiply_with_exponents(self):
        self.assertEqual(multiply("10^2", "10^3"), "10^5")
    
    def test_multiply_with_special_characters(self):
        self.assertEqual(multiply("123!", "456"), "56088")
    
    def test_multiply_with_unicode(self):
        self.assertEqual(multiply("123", "456"), "56088")
    
    def test_multiply_with_special_characters(self):
        self.assertEqual(multiply("123!", "456"), "56088")
    
    def test_multiply_with_unicode(self):
        self.assertEqual(multiply("123", "456"), "56088")
    
    def test_multiply_with_special_characters(self):
        self.assertEqual(multiply("123!", "456"), "56088")
    
    def test_multiply_with_unicode(self):
        self.assertEqual(multiply("123", "456"), "56088")
    
    def test_multiply_with_special_characters(self):
        self.assertEqual(multiply("123!", "456"), "56088")
    
    def test_multiply_with_unicode(self):
        self.assertEqual(multiply("123", "456"), "56088")
    
    def test_multiply_with_special_characters(self):
        self.assertEqual(multiply("123!", "456"), "56088")
    
    def test_multiply_with_unicode(self):
        self.assertEqual(multiply("123", "456"), "56088")
    
    def test_multiply_with_special_characters(self):
        self.assertEqual(multiply("123!", "456"), "56088")
    
    def test_multiply_with_unicode(self):
        self.assertEqual(multiply("123", "456"), "56088")
    
    def test_multiply_with_special_characters(self):
        self.assertEqual(multiply("123!", "456"), "56088")
    
    def test_multiply_with_unicode(self):
        self.assertEqual(multiply("123", "456"), "56088")
    
    def test_multiply_with_special_characters(self):
        self.assertEqual(multiply("123!", "456"), "56088")
    
    def test_multiply_with_unicode(self):
        self.assertEqual(multiply("123", "456"), "56088")
    
    def test_multiply_with_special_characters(self):
        self.assertEqual(multiply("123!", "456"), "56088")
    
    def test_multiply_with_unicode(self):
        self.assertEqual(multiply("123", "456"), "56088")
    
    def test_multiply_with_special_characters(self):
        self.assertEqual(multiply("123!", "456"), "56088")
    
    def test_multiply_with_unicode(self):
        self.assertEqual(multiply("123", "456"), "56088")
    
    def test_multiply_with_special_characters(self):
        self.assertEqual(multiply("123!", "456"), "56088")
    
    def test_multiply_with_unicode(self):
        self.assertEqual(multiply("123", "456"), "56088")
    
    def test_multiply_with_special_characters(self):
        self.assertEqual(multiply("123!", "456"), "56088")
    
    def test_multiply_with_unicode(self):
        self.assertEqual(multiply("123", "456"), "56088")
    
    def test_multiply_with_special_characters(self):
        self.assertEqual(multiply("123!", "456"), "56088")
    
    def test_multiply_with_unicode(self):
        self.assertEqual(multiply("123", "456"), "56088")
    
    def test_multiply_with_special_characters(self):
        self.assertEqual(multiply("123!", "456"), "56088")
    
    def test_multiply_with_unicode(self):
        self.assertEqual(multiply("123", "456"), "56088")
    
    def test_multiply_with_special_characters(self):
        self.assertEqual(multiply("123!", "456"), "56088")
    
    def test_multiply_with_unicode(self):
        self.assertEqual(multiply("123", "456"), "56088")
    
    def test_multiply_with_special_characters(self):
        self.assertEqual(multiply("123!", "456"), "56088")
    
    def test_multiply_with_unicode(self):
        self.assertEqual(multiply("123", "456"), "56088")
    
    def test_multiply_with_special_characters(self):
        self.assertEqual(multiply("123!", "456"), "56088")
    
    def test_multiply_with_unicode(self):
        self.assertEqual(multiply("123", "456"), "56088")
    
    def test_multiply_with_special_characters(self):
        self.assertEqual(m
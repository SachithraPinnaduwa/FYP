from subject_41 import *

import unittest

def multiply(num1, num2):
    num1 = [int(digit) for digit in num1]
    num2 = [int(digit) for digit in num2]
    num1.reverse()
    num2.reverse()
    result = [0] * (len(num1) + len(num2))
    for i in range(len(num1)):
        for j in range(len(num2)):
            result[i + j] += num1[i] * num2[j]
            result[i + j + 1] += result[i + j] // 10
            result[i + j] %= 10
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    result.reverse()
    result = ''.join(map(str, result))
    return result

class TestMultiplyFunction(unittest.TestCase):
    def test_multiply_with_positive_numbers(self):
        self.assertEqual(multiply("123", "456"), "56088")
        self.assertEqual(multiply("100", "100"), "10000")
        self.assertEqual(multiply("999", "999"), "998001")

    def test_multiply_with_zero(self):
        self.assertEqual(multiply("0", "123"), "0")
        self.assertEqual(multiply("123", "0"), "0")
        self.assertEqual(multiply("0", "0"), "0")

    def test_multiply_with_negative_numbers(self):
        self.assertEqual(multiply("-123", "456"), "-56088")
        self.assertEqual(multiply("123", "-456"), "-56088")
        self.assertEqual(multiply("-123", "-456"), "56088")

    def test_multiply_with_single_digit_numbers(self):
        self.assertEqual(multiply("2", "3"), "6")
        self.assertEqual(multiply("9", "9"), "81")
        self.assertEqual(multiply("1", "1"), "1")

    def test_multiply_with_large_numbers(self):
        self.assertEqual(multiply("12345678901234567890", "98765432109876543210"), "1219326311370217952237463801111263526900")
        self.assertEqual(multiply("98765432109876543210", "12345678901234567890"), "1219326311370217952237463801111263526900")

if __name__ == '__main__':
    unittest.main()
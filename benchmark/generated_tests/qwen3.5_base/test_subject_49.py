import unittest

class TestRPNCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = RPNCalculator()

    def test_basic_arithmetic(self):
        self.assertEqual(self.calc.evaluate("5 3 +"), 8.0)
        self.assertEqual(self.calc.evaluate("10 2 -"), 8.0)
        self.assertEqual(self.calc.evaluate("3 4 *"), 12.0)
        self.assertEqual(self.calc.evaluate("10 2 /"), 5.0)

    def test_complex_expression(self):
        self.assertEqual(self.calc.evaluate("5 3 + 2 *"), 16.0)
        self.assertEqual(self.calc.evaluate("10 2 - 3 *"), 17.0)
        self.assertEqual(self.calc.evaluate("3 4 * 2 -"), 10.0)

    def test_multiple_operations(self):
        self.assertEqual(self.calc.evaluate("5 3 + 2 4 - *"), 10.0)
        self.assertEqual(self.calc.evaluate("10 2 / 3 4 * -"), 2.0)

    def test_float_operations(self):
        self.assertEqual(self.calc.evaluate("5.5 3.2 +"), 8.7)
        self.assertEqual(self.calc.evaluate("10.0 2.5 /"), 4.0)

    def test_negative_numbers(self):
        self.assertEqual(self.calc.evaluate("-5 3 +"), -2.0)
        self.assertEqual(self.calc.evaluate("5 -3 -"), 8.0)

    def test_zero_operations(self):
        self.assertEqual(self.calc.evaluate("0 0 +"), 0.0)
        self.assertEqual(self.calc.evaluate("0 5 *"), 0.0)

    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.evaluate("5 0 /")

    def test_empty_expression(self):
        self.assertEqual(self.calc.evaluate(""), 0.0)

    def test_single_number(self):
        self.assertEqual(self.calc.evaluate("42"), 42.0)

    def test_large_numbers(self):
        self.assertEqual(self.calc.evaluate("1000000 1000000 +"), 2000000.0)
        self.assertEqual(self.calc.evaluate("1000000 1000000 *"), 1000000000000.0)

    def test_mixed_operators(self):
        self.assertEqual(self.calc.evaluate("5 3 + 2 4 - * 10 /"), 1.0)
        self.assertEqual(self.calc.evaluate("10 2 - 3 4 * +"), 19.0)

    def test_chained_operations(self):
        self.assertEqual(self.calc.evaluate("5 3 + 2 4 - * 10 / 3 4 * -"), 1.0)
        self.assertEqual(self.calc.evaluate("10 2 - 3 4 * + 5 3 + *"), 19.0)

    def test_precision(self):
        self.assertEqual(self.calc.evaluate("1.0000001 1.0000002 +"), 2.0000003)
        self.assertEqual(self.calc.evaluate("1.0000001 1.0000002 *"), 1.00000020000002)

    def test_negative_results(self):
        self.assertEqual(self.calc.evaluate("5 -3 -"), 8.0)
        self.assertEqual(self.calc.evaluate("3 -5 -"), -2.0)

    def test_large_negative_numbers(self):
        self.assertEqual(self.calc.evaluate("-1000000 -1000000 +"), -2000000.0)
        self.assertEqual(self.calc.evaluate("-1000000 -1000000 *"), 1000000000000.0)

    def test_mixed_positive_negative(self):
        self.assertEqual(self.calc.evaluate("5 -3 + 2 4 - *"), 10.0)
        self.assertEqual(self.calc.evaluate("10 2 - 3 4 * +"), 19.0)

    def test_precision_with_negative(self):
        self.assertEqual(self.calc.evaluate("-1.0000001 -1.0000002 +"), -2.0000003)
        self.assertEqual(self.calc.evaluate("-1.0000001 -1.0000002 *"), 1.00000020000002)

    def test_large_negative_results(self):
        self.assertEqual(self.calc.evaluate("-1000000 -1000000 +"), -2000000.0)
        self.assertEqual(self.calc.evaluate("-1000000 -1000000 *"), 1000000000000.0)

    def test_mixed_positive_negative(self):
        self.assertEqual(self.calc.evaluate("5 -3 + 2 4 - *"), 10.0)
        self.assertEqual(self.calc.evaluate("10 2 - 3 4 * +"), 19.0)

    def test_precision_with_negative(self):
        self.assertEqual(self.calc.evaluate("-1.0000001 -1.0000002 +"), -2.0000003)
        self.assertEqual(self.calc.evaluate("-1.0000001 -1.0000002 *"), 1.00000020000002)

    def test_large_negative_results(self):
        self.assertEqual(self.calc.evaluate("-1000000 -1000000 +"), -2000000.0)
        self.assertEqual(self.calc.evaluate("-1000000 -1000000 *"), 1000000000000.0)

    def test_mixed_positive_negative(self):
        self.assertEqual(self.calc.evaluate("5 -3 + 2 4 - *"), 10.0)
        self.assertEqual(self.calc.evaluate("10 2 - 3 4 * +"), 19.0)

    def test_precision_with_negative(self):
        self.assertEqual(self.calc.evaluate("-1.0000001 -1.0000002 +"), -2.0000003)
        self.assertEqual(self.calc.evaluate("-1.0000001 -1.0000002 *"), 1.0
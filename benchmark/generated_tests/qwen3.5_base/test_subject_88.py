import unittest

class TestShuntingYard(unittest.TestCase):
    def test_simple_arithmetic(self):
        self.assertEqual(ShuntingYard().infix_to_postfix("3 + 5"), "3 5 +")
        self.assertEqual(ShuntingYard().infix_to_postfix("10 - 2"), "10 2 -")
        self.assertEqual(ShuntingYard().infix_to_postfix("4 * 2"), "4 2 *")
        self.assertEqual(ShuntingYard().infix_to_postfix("8 / 4"), "8 4 /")
        self.assertEqual(ShuntingYard().infix_to_postfix("2 ^ 3"), "2 3 ^")

    def test_complex_arithmetic(self):
        self.assertEqual(ShuntingYard().infix_to_postfix("3 + 5 * 2"), "3 5 2 * +")
        self.assertEqual(ShuntingYard().infix_to_postfix("10 - 2 + 3"), "10 2 - 3 +")
        self.assertEqual(ShuntingYard().infix_to_postfix("4 * 2 / 2"), "4 2 * 2 /")
        self.assertEqual(ShuntingYard().infix_to_postfix("8 / 4 * 2"), "8 4 / 2 *")
        self.assertEqual(ShuntingYard().infix_to_postfix("2 ^ 3 ^ 2"), "2 3 2 ^ ^")

    def test_with_parentheses(self):
        self.assertEqual(ShuntingYard().infix_to_postfix("(3 + 5) * 2"), "3 5 + 2 *")
        self.assertEqual(ShuntingYard().infix_to_postfix("10 - (2 + 3)"), "10 2 3 + -")
        self.assertEqual(ShuntingYard().infix_to_postfix("(4 * 2) / 2"), "4 2 * 2 /")
        self.assertEqual(ShuntingYard().infix_to_postfix("8 / (4 * 2)"), "8 4 2 * /")

    def test_with_decimals(self):
        self.assertEqual(ShuntingYard().infix_to_postfix("3.14 + 5"), "3.14 5 +")
        self.assertEqual(ShuntingYard().infix_to_postfix("10.5 - 2.5"), "10.5 2.5 -")
        self.assertEqual(ShuntingYard().infix_to_postfix("4.2 * 2.5"), "4.2 2.5 *")
        self.assertEqual(ShuntingYard().infix_to_postfix("8.8 / 4.2"), "8.8 4.2 /")

    def test_with_negative_numbers(self):
        self.assertEqual(ShuntingYard().infix_to_postfix("-3 + 5"), "-3 5 +")
        self.assertEqual(ShuntingYard().infix_to_postfix("10 - -2"), "10 -2 -")
        self.assertEqual(ShuntingYard().infix_to_postfix("-4 * 2"), "-4 2 *")
        self.assertEqual(ShuntingYard().infix_to_postfix("8 / -4"), "8 -4 /")

    def test_with_exponents(self):
        self.assertEqual(ShuntingYard().infix_to_postfix("2 ^ 3"), "2 3 ^")
        self.assertEqual(ShuntingYard().infix_to_postfix("3 ^ 2 ^ 3"), "3 2 3 ^ ^")
        self.assertEqual(ShuntingYard().infix_to_postfix("(2 ^ 3) ^ 2"), "2 3 ^ 2 ^")

    def test_with_multiple_operators(self):
        self.assertEqual(ShuntingYard().infix_to_postfix("3 + 5 - 2"), "3 5 + 2 -")
        self.assertEqual(ShuntingYard().infix_to_postfix("10 - 2 + 3 - 1"), "10 2 - 3 + 1 -")
        self.assertEqual(ShuntingYard().infix_to_postfix("4 * 2 / 2 * 3"), "4 2 * 2 / 3 *")
        self.assertEqual(ShuntingYard().infix_to_postfix("8 / 4 * 2 / 3"), "8 4 / 2 * 3 /")

    def test_with_mixed_operators(self):
        self.assertEqual(ShuntingYard().infix_to_postfix("3 + 5 * 2 - 4"), "3 5 2 * + 4 -")
        self.assertEqual(ShuntingYard().infix_to_postfix("10 - 2 + 3 * 4"), "10 2 - 3 4 * +")
        self.assertEqual(ShuntingYard().infix_to_postfix("4 * 2 / 2 + 3"), "4 2 * 2 / 3 +")
        self.assertEqual(ShuntingYard().infix_to_postfix("8 / 4 * 2 + 3"), "8 4 / 2 * 3 +")

    def test_with_complex_expressions(self):
        self.assertEqual(ShuntingYard().infix_to_postfix("3 + 5 * 2 - 4 / 2"), "3 5 2 * + 4 2 / -")
        self.assertEqual(ShuntingYard().infix_to_postfix("10 - 2 + 3 * 4 - 1"), "10 2 - 3 4 * + 1 -")
        self.assertEqual(ShuntingYard().infix_to_postfix("(3 + 5) * 2 - 4 / 2"), "3 5 + 2 * 4 2 / -")
        self.assertEqual(ShuntingYard().infix_to_postfix("10 - (2 + 3) * 4"), "10 2 3 + 4 * -")

    def test_with_empty_expression(self):
        self.assertEqual(ShuntingYard().infix_to_postfix(""), "")

    def test_with_single_number(self):
        self.assertEqual(ShuntingYard().infix_to_postfix("5"), "5")
        self.assertEqual(ShuntingYard().infix_to_postfix("3.14"), "3.14")
        self.assertEqual(ShuntingYard().infix_to_postfix("-5"), "-5")

    def test_with_single_operator(self):
        self.assertEqual(ShuntingYard().infix_to_postfix("+"), "+")
        self.assertEqual(ShuntingYard().infix_to_postfix("-"), "-")
        self.assertEqual(ShuntingYard().infix_to_post
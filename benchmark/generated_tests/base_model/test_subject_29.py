import unittest

class TestDetectEvenOdd(unittest.TestCase):

    def test_valid_even_number(self):
        self.assertEqual(detect_even_odd(4), "Even")

    def test_valid_odd_number(self):
        self.assertEqual(detect_even_odd(5), "Odd")

    def test_zero(self):
        self.assertEqual(detect_even_odd(0), "Invalid Input")

    def test_negative_number(self):
        self.assertEqual(detect_even_odd(-3), "Invalid Input")

    def test_large_positive_number(self):
        self.assertEqual(detect_even_odd(1001), "Invalid Input")

    def test_float_number(self):
        self.assertEqual(detect_even_odd(3.5), "Invalid Input")

    def test_string_input(self):
        self.assertEqual(detect_even_odd("123"), "Invalid Input")

if __name__ == '__main__':
    unittest.main()
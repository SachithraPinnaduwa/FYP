from subject_29 import *

import unittest

def detect_even_odd(number):
    if not isinstance(number, int) or number <= 0 or number > 1000:
        return "Invalid Input"
    elif number % 2 == 0:
        return "Even"
    else:
        return "Odd"

class TestDetectEvenOdd(unittest.TestCase):
    def test_even_numbers(self):
        self.assertEqual(detect_even_odd(2), "Even")
        self.assertEqual(detect_even_odd(4), "Even")
        self.assertEqual(detect_even_odd(6), "Even")
        self.assertEqual(detect_even_odd(1000), "Even")

    def test_odd_numbers(self):
        self.assertEqual(detect_even_odd(1), "Odd")
        self.assertEqual(detect_even_odd(3), "Odd")
        self.assertEqual(detect_even_odd(5), "Odd")
        self.assertEqual(detect_even_odd(999), "Odd")

    def test_invalid_input(self):
        self.assertEqual(detect_even_odd(0), "Invalid Input")
        self.assertEqual(detect_even_odd(-1), "Invalid Input")
        self.assertEqual(detect_even_odd(1001), "Invalid Input")
        self.assertEqual(detect_even_odd(3.14), "Invalid Input")
        self.assertEqual(detect_even_odd("10"), "Invalid Input")

if __name__ == '__main__':
    unittest.main()
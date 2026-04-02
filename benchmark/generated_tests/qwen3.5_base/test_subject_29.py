import unittest

class TestDetectEvenOdd(unittest.TestCase):
    def test_valid_even(self):
        self.assertEqual(detect_even_odd(2), "Even")
        self.assertEqual(detect_even_odd(100), "Even")
        self.assertEqual(detect_even_odd(0), "Even")
        self.assertEqual(detect_even_odd(1000), "Even")

    def test_valid_odd(self):
        self.assertEqual(detect_even_odd(1), "Odd")
        self.assertEqual(detect_even_odd(999), "Odd")
        self.assertEqual(detect_even_odd(1001), "Odd")

    def test_invalid_input(self):
        self.assertEqual(detect_even_odd(-1), "Invalid Input")
        self.assertEqual(detect_even_odd(1001), "Invalid Input")
        self.assertEqual(detect_even_odd(0.5), "Invalid Input")
        self.assertEqual(detect_even_odd("5"), "Invalid Input")
        self.assertEqual(detect_even_odd(None), "Invalid Input")

if __name__ == '__main__':
    unittest.main()

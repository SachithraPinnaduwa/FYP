import unittest

class TestCalculateArea(unittest.TestCase):

    def test_valid_float_input(self):
        self.assertEqual(calculate_area(3.0), 3.8971)

    def test_valid_integer_input(self):
        self.assertEqual(calculate_area(4), 6.93)

    def test_zero_input(self):
        self.assertEqual(calculate_area(0), "Invalid input value for side length")

    def test_negative_input(self):
        self.assertEqual(calculate_area(-5), "Invalid input value for side length")

    def test_string_input(self):
        self.assertEqual(calculate_area("five"), "Invalid input value for side length")

    def test_boolean_input(self):
        self.assertEqual(calculate_area(True), "Invalid input value for side length")

if __name__ == '__main__':
    unittest.main()
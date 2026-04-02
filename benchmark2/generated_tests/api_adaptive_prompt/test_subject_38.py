from subject_38 import *

import unittest

class TestEntanceFunction(unittest.TestCase):
    def test_normal_case_positive_integer(self):
        self.assertEqual(entance(5), 10.83)

    def test_normal_case_positive_float(self):
        self.assertEqual(entance(3.5), 4.90)

    def test_edge_case_smallest_positive_integer(self):
        self.assertEqual(entance(1), 0.43)

    def test_edge_case_smallest_positive_float(self):
        self.assertEqual(entance(0.1), 0.03)

    def test_error_handling_negative_integer(self):
        self.assertEqual(entance(-5), "Invalid input value for side length")

    def test_error_handling_negative_float(self):
        self.assertEqual(entance(-3.5), "Invalid input value for side length")

    def test_error_handling_zero(self):
        self.assertEqual(entance(0), "Invalid input value for side length")

    def test_error_handling_non_numeric(self):
        self.assertEqual(entance('a'), "Invalid input value for side length")

if __name__ == '__main__':
    unittest.main()
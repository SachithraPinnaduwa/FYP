from subject_74 import *

import unittest

class TestValidateInput(unittest.TestCase):
    def test_normal_case(self):
        with unittest.mock.patch('builtins.input', side_effect=['7']):
            self.assertEqual(validate_input(), 7)

    def test_edge_case_smallest_valid_input(self):
        with unittest.mock.patch('builtins.input', side_effect=['2']):
            self.assertEqual(validate_input(), 2)

    def test_edge_case_largest_valid_input(self):
        with unittest.mock.patch('builtins.input', side_effect=['10']):
            self.assertEqual(validate_input(), 10)

    def test_error_handling_non_integer_input(self):
        with unittest.mock.patch('builtins.input', side_effect=['abc', '5']):
            self.assertEqual(validate_input(), 5)

    def test_error_handling_out_of_range_input(self):
        with unittest.mock.patch('builtins.input', side_effect=['15', '5']):
            self.assertEqual(validate_input(), 5)

    def test_error_handling_divisible_by_5_prime_number(self):
        with unittest.mock.patch('builtins.input', side_effect=['5', '10']):
            self.assertEqual(validate_input(), 10)

if __name__ == '__main__':
    unittest.main()
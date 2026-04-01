import unittest
from unittest.mock import patch
import sys

class TestValidateInput(unittest.TestCase):

    @patch('builtins.input', side_effect=['3', '7', '5', '10'])
    def test_invalid_inputs(self, mock_input):
        with self.assertRaises(SystemExit) as cm:
            validate_input()
        self.assertEqual(cm.exception.code, 1)

    @patch('builtins.input', return_value='10')
    def test_valid_input(self, mock_input):
        result = validate_input()
        self.assertEqual(result, 10)
        self.assertTrue(2 <= result <= 10)
        self.assertTrue(result % 5 == 0)
        self.assertFalse(is_prime(result))

if __name__ == '__main__':
    unittest.main()
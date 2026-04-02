from subject_74 import *

import unittest

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def validate_input():
    while True:
        try:
            num = int(input("Enter a number between 2 and 10 (inclusive), divisible by 5, and not prime: "))
            if num >= 2 and num <= 10 and num % 5 == 0 and not is_prime(num):
                return num
            else:
                print("Invalid input. Please try again.")
        except ValueError:
            print("Invalid input. Please try again.")

class TestValidateInput(unittest.TestCase):
    def test_valid_input(self):
        with unittest.mock.patch('builtins.input', side_effect=['10', '15']):
            self.assertEqual(validate_input(), 10)
            self.assertEqual(validate_input(), 15)

    def test_invalid_input(self):
        with unittest.mock.patch('builtins.input', side_effect=['1', '2', '3', '5', '7', '11', '13', '14', '16', '17', '18', '19', '20']):
            self.assertIsNone(validate_input())
            self.assertIsNone(validate_input())
            self.assertIsNone(validate_input())
            self.assertIsNone(validate_input())
            self.assertIsNone(validate_input())
            self.assertIsNone(validate_input())
            self.assertIsNone(validate_input())
            self.assertIsNone(validate_input())
            self.assertIsNone(validate_input())
            self.assertIsNone(validate_input())
            self.assertIsNone(validate_input())
            self.assertIsNone(validate_input())
            self.assertIsNone(validate_input())

if __name__ == '__main__':
    unittest.main()
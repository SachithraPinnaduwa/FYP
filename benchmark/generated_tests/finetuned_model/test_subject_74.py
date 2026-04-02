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
        with unittest.mock.patch('builtins.input', side_effect=['20']):
            self.assertEqual(validate_input(), 20)

    def test_invalid_input_not_divisible_by_5(self):
        with unittest.mock.patch('builtins.input', side_effect=['22', '30']):
            self.assertEqual(validate_input(), 30)

    def test_invalid_input_prime_number(self):
        with unittest.mock.patch('builtins.input', side_effect=['5', '7', '11', '15']):
            self.assertEqual(validate_input(), 15)

    def test_invalid_input_not_integer(self):
        with unittest.mock.patch('builtins.input', side_effect=['a', '25', '35']):
            self.assertEqual(validate_input(), 35)

    def test_invalid_input_out_of_range(self):
        with unittest.mock.patch('builtins.input', side_effect=['1', '11', '35']):
            self.assertEqual(validate_input(), 35)

if __name__ == '__main__':
    unittest.main()
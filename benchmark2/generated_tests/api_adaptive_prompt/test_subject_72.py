from subject_72 import *

import unittest

def is_perfect_prime(n):
    """
    Checks whether a given number n is a perfect prime.
    
    A perfect prime is a prime number that is equal to the sum of its proper divisors (excluding itself).
    
    Args:
    n (int): The number to be checked.
    
    Returns:
    bool: True if the number is a perfect prime, False otherwise.
    """

    # Function to check if a number is prime
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    # Function to find the sum of proper divisors of a number
    def sum_of_divisors(num):
        sum_div = 1  # 1 is a divisor of all numbers
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                sum_div += i
                if i != num // i:  # Check if divisors are different
                    sum_div += num // i
        return sum_div

    # Check if the number is prime and equal to the sum of its proper divisors
    return is_prime(n) and n == sum_of_divisors(n)

class TestIsPerfectPrime(unittest.TestCase):
    def test_normal_case_perfect_prime(self):
        self.assertTrue(is_perfect_prime(6))

    def test_normal_case_non_perfect_prime(self):
        self.assertFalse(is_perfect_prime(10))

    def test_normal_case_non_prime(self):
        self.assertFalse(is_perfect_prime(7))

    def test_edge_case_smallest_prime(self):
        self.assertFalse(is_perfect_prime(2))

    def test_edge_case_smallest_even(self):
        self.assertFalse(is_perfect_prime(4))

    def test_error_handling_non_integer_input(self):
        with self.assertRaises(TypeError):
            is_perfect_prime('a')

    def test_error_handling_negative_number(self):
        self.assertFalse(is_perfect_prime(-3))

if __name__ == '__main__':
    unittest.main()
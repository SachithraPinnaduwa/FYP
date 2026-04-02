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
    def test_is_perfect_prime(self):
        self.assertTrue(is_perfect_prime(2))
        self.assertFalse(is_perfect_prime(3))
        self.assertTrue(is_perfect_prime(5))
        self.assertFalse(is_perfect_prime(7))
        self.assertFalse(is_perfect_prime(11))
        self.assertFalse(is_perfect_prime(13))
        self.assertFalse(is_perfect_prime(17))
        self.assertFalse(is_perfect_prime(19))
        self.assertFalse(is_perfect_prime(23))
        self.assertFalse(is_perfect_prime(29))
        self.assertFalse(is_perfect_prime(31))
        self.assertFalse(is_perfect_prime(37))
        self.assertFalse(is_perfect_prime(41))
        self.assertFalse(is_perfect_prime(43))
        self.assertFalse(is_perfect_prime(47))
        self.assertFalse(is_perfect_prime(53))
        self.assertFalse(is_perfect_prime(59))
        self.assertFalse(is_perfect_prime(61))
        self.assertFalse(is_perfect_prime(67))
        self.assertFalse(is_perfect_prime(71))
        self.assertFalse(is_perfect_prime(73))
        self.assertFalse(is_perfect_prime(79))
        self.assertFalse(is_perfect_prime(83))
        self.assertFalse(is_perfect_prime(89))
        self.assertFalse(is_perfect_prime(97))
        self.assertFalse(is_perfect_prime(101))
        self.assertFalse(is_perfect_prime(103))
        self.assertFalse(is_perfect_prime(107))
        self.assertFalse(is_perfect_prime(109))
        self.assertFalse(is_perfect_prime(113))
        self.assertFalse(is_perfect_prime(127))
        self.assertFalse(is_perfect_prime(131))
        self.assertFalse(is_perfect_prime(137))
        self.assertFalse(is_perfect_prime(139))
        self.assertFalse(is_perfect_prime(149))
        self.assertFalse(is_perfect_prime(151))
        self.assertFalse(is_perfect_prime(157))
        self.assertFalse(is_perfect_prime(163))
        self.assertFalse(is_perfect_prime(167))
        self.assertFalse(is_perfect_prime(173))
        self.assertFalse(is_perfect_prime(179))
        self.assertFalse(is_perfect_prime(181))
        self.assertFalse(is_perfect_prime(191))
        self.assertFalse(is_perfect_prime(193))
        self.assertFalse(is_perfect_prime(197))
        self.assertFalse(is_perfect_prime(199))
        self.assertFalse(is_perfect_prime(211))
        self.assertFalse(is_perfect_prime(223))
        self.assertFalse(is_perfect_prime(227))
        self.assertFalse(is_perfect_prime(229))
        self.assertFalse(is_perfect_prime(233))
        self.assertFalse(is_perfect_prime(239))
        self.assertFalse(is_perfect_prime(241))
        self.assertFalse(is_perfect_prime(251))
        self.assertFalse(is_perfect_prime(257))
        self.assertFalse(is_perfect_prime(263))
        self.assertFalse(is_perfect_prime(269))
        self.assertFalse(is_perfect_prime(271))
        self.assertFalse(is_perfect_prime(277))
        self.assertFalse(is_perfect_prime(281))
        self.assertFalse(is_perfect_prime(283))
        self.assertFalse(is_perfect_prime(293))
        self.assertFalse(is
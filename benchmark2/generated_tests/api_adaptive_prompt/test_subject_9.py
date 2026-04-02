from subject_9 import *

import unittest

def nth_prime(N):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    count = 0
    num = 2
    while(count < N):
        if is_prime(num):
            count += 1
        num += 1
    return num - 1

class TestNthPrime(unittest.TestCase):
    def test_normal_case_positive_integer(self):
        self.assertEqual(nth_prime(10), 29)

    def test_normal_case_small_positive_integer(self):
        self.assertEqual(nth_prime(1), 2)

    def test_normal_case_large_positive_integer(self):
        self.assertEqual(nth_prime(100), 541)

    def test_normal_case_negative_integer(self):
        self.assertIsNone(nth_prime(-5))

    def test_normal_case_zero(self):
        self.assertIsNone(nth_prime(0))

    def test_normal_case_large_positive_integer_efficiency(self):
        self.assertEqual(nth_prime(10000), 104729)

if __name__ == '__main__':
    unittest.main()
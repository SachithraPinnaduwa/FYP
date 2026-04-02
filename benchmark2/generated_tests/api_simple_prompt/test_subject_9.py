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
    def test_nth_prime(self):
        self.assertEqual(nth_prime(1), 2)
        self.assertEqual(nth_prime(2), 3)
        self.assertEqual(nth_prime(3), 5)
        self.assertEqual(nth_prime(4), 7)
        self.assertEqual(nth_prime(5), 11)
        self.assertEqual(nth_prime(10), 29)
        self.assertEqual(nth_prime(100), 541)

if __name__ == '__main__':
    unittest.main()
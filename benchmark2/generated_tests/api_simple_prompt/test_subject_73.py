from subject_73 import *

import unittest

def entrance(start, end):
    primes = []
    for num in range(start, end + 1):
        if num > 1:  
            for i in range(2, num):
                if (num % i) == 0:  
                    break
            else:
                primes.append(num)  
    return primes

class TestEntranceFunction(unittest.TestCase):
    def test_prime_numbers_between_1_and_10(self):
        self.assertEqual(entrance(1, 10), [2, 3, 5, 7])

    def test_prime_numbers_between_10_and_20(self):
        self.assertEqual(entrance(10, 20), [11, 13, 17, 19])

    def test_prime_numbers_between_20_and_30(self):
        self.assertEqual(entrance(20, 30), [23, 29])

    def test_prime_numbers_between_1_and_5(self):
        self.assertEqual(entrance(1, 5), [2, 3, 5])

    def test_prime_numbers_between_50_and_60(self):
        self.assertEqual(entrance(50, 60), [53, 59])

    def test_prime_numbers_between_100_and_110(self):
        self.assertEqual(entrance(100, 110), [101, 103, 107, 109])

    def test_prime_numbers_between_1_and_2(self):
        self.assertEqual(entrance(1, 2), [2])

    def test_prime_numbers_between_1000_and_1010(self):
        self.assertEqual(entrance(1000, 1010), [1009])

    def test_prime_numbers_between_1_and_1(self):
        self.assertEqual(entrance(1, 1), [])

if __name__ == '__main__':
    unittest.main()
from subject_37 import *

import unittest

def isOddPrimeGreaterThan100(number):
    if number <= 100 or number % 2 == 0:  # Check if number is less than or equal to 100 or even
        return False
    for i in range(3, int(number**0.5) + 1, 2):  # Check divisibility by odd numbers only
        if number % i == 0:
            return False
    return True

def findSecondSmallestOddPrimeGreaterThan100(array):
    smallest = secondSmallest = float('inf')
    for number in array:
        if isOddPrimeGreaterThan100(number):
            if number < smallest:
                secondSmallest = smallest
                smallest = number
            elif number < secondSmallest and number != smallest:
                secondSmallest = number
    return secondSmallest

class TestFindSecondSmallestOddPrimeGreaterThan100(unittest.TestCase):
    def test_normal_case_1(self):
        self.assertEqual(findSecondSmallestOddPrimeGreaterThan100([101, 103, 107, 109, 113, 127]), 103)

    def test_normal_case_2(self):
        self.assertEqual(findSecondSmallestOddPrimeGreaterThan100([101, 103, 107, 109, 113, 101, 103, 107, 109, 113]), 103)

    def test_normal_case_3(self):
        self.assertEqual(findSecondSmallestOddPrimeGreaterThan100([101, 103, 107, 109, 113, 101, 103, 107, 109, 113, 101]), 103)

    def test_normal_case_4(self):
        self.assertEqual(findSecondSmallestOddPrimeGreaterThan100([101, 103, 107, 109, 113, 101, 103, 107, 109, 113, 101]), 103)

    def test_normal_case_5(self):
        self.assertEqual(findSecondSmallestOddPrimeGreaterThan100([101, 103, 107, 109, 113, 101, 103, 107, 109, 113, 101]), 103)

if __name__ == '__main__':
    unittest.main()